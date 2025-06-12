import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
// import { useAuth } from '@/hooks/useAuth'; // Bir sonraki adımda oluşturacağız
import { Shield } from 'lucide-react';

export default function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();
  // const { login } = useAuth();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    try {
      // login(username, password); // Bu servisi daha sonra bağlayacağız
      // Şimdilik başarılı bir login'i taklit edelim:
      localStorage.setItem('authToken', 'fake_token'); // Tarayıcı hafızasına sahte token kaydet
      navigate('/dashboard'); // Başarılı olunca dashboard'a yönlendir
    } catch (err) {
      setError('Invalid username or password.');
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-cyber-dark cyber-grid">
      <Card className="w-full max-w-sm glass-morphism">
        <CardHeader className="text-center">
          <Shield className="mx-auto h-12 w-12 text-cyber-primary" />
          <CardTitle className="text-2xl terminal-text">CyberShield SOC</CardTitle>
          <CardDescription>Enter your credentials to access the simulation platform.</CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="username">Username</Label>
              <Input id="username" value={username} onChange={(e) => setUsername(e.target.value)} required />
            </div>
            <div className="space-y-2">
              <Label htmlFor="password">Password</Label>
              <Input id="password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
            </div>
            {error && <p className="text-sm text-red-500">{error}</p>}
            <Button type="submit" className="w-full bg-cyber-primary text-cyber-dark hover:bg-cyber-primary/80">
              Login
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}