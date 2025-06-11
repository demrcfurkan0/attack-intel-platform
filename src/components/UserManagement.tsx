import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from '@/components/ui/dialog';
import { Users, UserPlus, Loader2 } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';
import { getUsers, createUser, deleteUser, updateUser } from '@/services/userService';
import { User, UserCreatePayload } from '../types/apiTypes';

const UserManagement = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [newUser, setNewUser] = useState<UserCreatePayload>({
    username: '', email: '', role: 'SOC Operator', password: ''
  });
  const { toast } = useToast();
  
  const fetchUsers = async () => {
    setIsLoading(true);
    try {
      const response = await getUsers();
      const rawUsers: any[] = response.data || []; 
      
      // Gelen veriyi, 'id' alanı garanti olan bir formata dönüştür
      const processedUsers: User[] = rawUsers.map(rawUser => {
        const userId = rawUser.id || (rawUser._id ? String(rawUser._id) : '');
        return {
          id: userId,
          username: rawUser.username,
          email: rawUser.email,
          role: rawUser.role,
          status: rawUser.status,
        };
      }).filter(user => user.id); // ID'si olmayanları filtrele

      setUsers(processedUsers);
      
    } catch (error) {
      toast({ variant: "destructive", title: "Failed to load users." });
      setUsers([]);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const handleAddUser = async () => {
    if (!newUser.username || !newUser.email || !newUser.password || !newUser.role) {
      toast({ title: "Validation Error", description: "Please fill all fields.", variant: "destructive" });
      return;
    }
    try {
      await createUser(newUser);
      toast({ title: "User Created", description: `User ${newUser.username} has been created.` });
      setIsDialogOpen(false);
      setNewUser({ username: '', email: '', role: 'SOC Operator', password: '' });
      await fetchUsers();
    } catch (error: any) {
      toast({ variant: "destructive", title: "Failed to create user", description: error.response?.data?.detail });
    }
  };

  const handleDeleteUser = async (userId: string, username: string) => {
    if (!window.confirm(`Are you sure you want to delete user ${username}?`)) return;
    try {
      await deleteUser(userId);
      toast({ title: "User Deleted" });
      await fetchUsers();
    } catch (error: any) {
      toast({ variant: "destructive", title: "Failed to delete user", description: error.response?.data?.detail });
    }
  };

  const handleToggleStatus = async (userId: string, currentStatus: 'active' | 'inactive') => {
    const newStatus = currentStatus === 'active' ? 'inactive' : 'active';
    try {
      await updateUser(userId, { status: newStatus });
      toast({ title: "Status Updated" });
      await fetchUsers();
    } catch (error: any) {
      toast({ variant: "destructive", title: "Failed to update status", description: error.response?.data?.detail });
    }
  };

  return (
    <div className="space-y-6">
      <Card className="glass-morphism">
        <CardHeader>
          <CardTitle className="flex items-center justify-between">
            <div className="flex items-center space-x-2"><Users /><span>User Management</span></div>
            <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
              <DialogTrigger asChild><Button><UserPlus className="w-4 h-4 mr-2" />Add User</Button></DialogTrigger>
              <DialogContent>
                <DialogHeader><DialogTitle>Create New User</DialogTitle></DialogHeader>
                <div className="space-y-4 py-4">
                  <div><Label>Username</Label><Input value={newUser.username} onChange={(e) => setNewUser({...newUser, username: e.target.value})} /></div>
                  <div><Label>Email</Label><Input type="email" value={newUser.email} onChange={(e) => setNewUser({...newUser, email: e.target.value})} /></div>
                  <div><Label>Password</Label><Input type="password" value={newUser.password} onChange={(e) => setNewUser({...newUser, password: e.target.value})} /></div>
                  <div><Label>Role</Label><Select value={newUser.role} onValueChange={(value) => setNewUser({...newUser, role: value})}><SelectTrigger><SelectValue/></SelectTrigger><SelectContent><SelectItem value="Administrator">Administrator</SelectItem><SelectItem value="Security Analyst">Security Analyst</SelectItem><SelectItem value="SOC Operator">SOC Operator</SelectItem></SelectContent></Select></div>
                </div>
                <DialogFooter><Button variant="outline" onClick={() => setIsDialogOpen(false)}>Cancel</Button><Button onClick={handleAddUser}>Create User</Button></DialogFooter>
              </DialogContent>
            </Dialog>
          </CardTitle>
        </CardHeader>
        <CardContent>
          {isLoading ? <div className="flex justify-center p-8"><Loader2 className="animate-spin" /></div> :
            <Table>
              <TableHeader><TableRow><TableHead>Username</TableHead><TableHead>Email</TableHead><TableHead>Role</TableHead><TableHead>Status</TableHead><TableHead className="text-right">Actions</TableHead></TableRow></TableHeader>
              <TableBody>
                {users?.length > 0 ? users.map((user) => (
                  <TableRow key={user.id}>
                    <TableCell>{user.username}</TableCell>
                    <TableCell>{user.email}</TableCell>
                    <TableCell>{user.role}</TableCell>
                    <TableCell><Badge variant={user.status === 'active' ? 'default' : 'secondary'}>{user.status}</Badge></TableCell>
                    <TableCell className="text-right space-x-2">
                      <Button size="sm" variant="outline" onClick={() => handleToggleStatus(user.id, user.status)}>
                        {user.status === 'active' ? 'Deactivate' : 'Activate'}
                      </Button>
                      <Button size="sm" variant="destructive" onClick={() => handleDeleteUser(user.id, user.username)}>
                        Delete
                      </Button>
                    </TableCell>
                  </TableRow>
                )) : (
                  <TableRow><TableCell colSpan={5} className="text-center">No users found.</TableCell></TableRow>
                )}
              </TableBody>
            </Table>
          }
        </CardContent>
      </Card>
    </div>
  );
};
export default UserManagement;