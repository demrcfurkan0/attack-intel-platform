import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Shield, Loader2 } from 'lucide-react';
import { login } from '@/services/authService'; // Yeni servisi import et

export default function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setIsLoading(true);
    try {
      // Backend'e login isteği gönder
      const data = await login(username, password);
      
      // Başarılı olursa, dönen token'ı tarayıcı hafızasına kaydet
      if (data.access_token) {
        localStorage.setItem('authToken', data.access_token);
        // Dashboard'a yönlendir
        navigate('/dashboard', { replace: true });
      } else {
        throw new Error('No token received');
      }
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Invalid username or password.';
      setError(errorMessage);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-cyber-dark cyber-grid">
      <Card className="w-full max-w-sm glass-morphism">
        <CardHeader className="text-center">
          <Shield className="mx-auto h-12 w-12 text-cyber-primary" />
          <CardTitle className="text-2xl terminal-text">CyberShield SOC</CardTitle>
          <CardDescription>Enter your credentials to access the platform.</CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="username">Username</Label>
              <Input id="username" value={username} onChange={(e) => setUsername(e.target.value)} required disabled={isLoading} />
            </div>
            <div className="space-y-2">
              <Label htmlFor="password">Password</Label>
              <Input id="password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required disabled={isLoading} />
            </div>
            {error && <p className="text-sm text-red-500 text-center">{error}</p>}
            <Button type="submit" className="w-full bg-cyber-primary text-cyber-dark hover:bg-cyber-primary/80" disabled={isLoading}>
              {isLoading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
              Login
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}