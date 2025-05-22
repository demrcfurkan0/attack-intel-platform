
import React, { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from '@/components/ui/dialog';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Users, UserPlus, Settings, Shield, AlertTriangle, Search } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';

const UserManagement = () => {
  const [users, setUsers] = useState([
    {
      id: 1,
      username: 'admin',
      email: 'admin@cybershield.com',
      role: 'Administrator',
      status: 'active',
      lastLogin: '2024-05-22 14:30:00',
      permissions: ['full_access', 'user_management', 'system_config']
    },
    {
      id: 2,
      username: 'analyst1',
      email: 'analyst1@cybershield.com',
      role: 'Security Analyst',
      status: 'active',
      lastLogin: '2024-05-22 14:15:00',
      permissions: ['view_alerts', 'manage_responses', 'export_data']
    },
    {
      id: 3,
      username: 'operator1',
      email: 'operator1@cybershield.com',
      role: 'SOC Operator',
      status: 'active',
      lastLogin: '2024-05-22 13:45:00',
      permissions: ['view_alerts', 'acknowledge_alerts']
    },
    {
      id: 4,
      username: 'auditor1',
      email: 'auditor1@cybershield.com',
      role: 'Auditor',
      status: 'inactive',
      lastLogin: '2024-05-21 16:30:00',
      permissions: ['view_logs', 'export_reports']
    },
    {
      id: 5,
      username: 'guest',
      email: 'guest@cybershield.com',
      role: 'Guest',
      status: 'active',
      lastLogin: '2024-05-22 12:00:00',
      permissions: ['view_dashboard']
    }
  ]);

  const [searchTerm, setSearchTerm] = useState('');
  const [roleFilter, setRoleFilter] = useState('all');
  const [statusFilter, setStatusFilter] = useState('all');
  const [newUser, setNewUser] = useState({
    username: '',
    email: '',
    role: '',
    password: ''
  });
  const [isAddingUser, setIsAddingUser] = useState(false);
  const { toast } = useToast();

  const roles = [
    { value: 'Administrator', label: 'Administrator', color: 'bg-cyber-accent' },
    { value: 'Security Analyst', label: 'Security Analyst', color: 'bg-cyber-warning' },
    { value: 'SOC Operator', label: 'SOC Operator', color: 'bg-cyber-secondary' },
    { value: 'Auditor', label: 'Auditor', color: 'bg-cyber-primary' },
    { value: 'Guest', label: 'Guest', color: 'bg-gray-500' }
  ];

  const permissions = [
    'full_access',
    'user_management',
    'system_config',
    'view_alerts',
    'manage_responses',
    'export_data',
    'acknowledge_alerts',
    'view_logs',
    'export_reports',
    'view_dashboard'
  ];

  const filteredUsers = users.filter(user => {
    const matchesSearch = searchTerm === '' || 
      user.username.toLowerCase().includes(searchTerm.toLowerCase()) ||
      user.email.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesRole = roleFilter === 'all' || user.role === roleFilter;
    const matchesStatus = statusFilter === 'all' || user.status === statusFilter;
    
    return matchesSearch && matchesRole && matchesStatus;
  });

  const getRoleColor = (role: string) => {
    const roleObj = roles.find(r => r.value === role);
    return roleObj ? roleObj.color : 'bg-gray-500';
  };

  const handleAddUser = () => {
    if (!newUser.username || !newUser.email || !newUser.role || !newUser.password) {
      toast({
        title: "Validation Error",
        description: "Please fill in all required fields.",
        variant: "destructive",
      });
      return;
    }

    const user = {
      id: users.length + 1,
      username: newUser.username,
      email: newUser.email,
      role: newUser.role,
      status: 'active',
      lastLogin: 'Never',
      permissions: getDefaultPermissions(newUser.role)
    };

    setUsers([...users, user]);
    setNewUser({ username: '', email: '', role: '', password: '' });
    setIsAddingUser(false);
    
    toast({
      title: "User Created",
      description: `User ${newUser.username} has been created successfully.`,
    });
  };

  const getDefaultPermissions = (role: string) => {
    switch (role) {
      case 'Administrator':
        return ['full_access', 'user_management', 'system_config'];
      case 'Security Analyst':
        return ['view_alerts', 'manage_responses', 'export_data'];
      case 'SOC Operator':
        return ['view_alerts', 'acknowledge_alerts'];
      case 'Auditor':
        return ['view_logs', 'export_reports'];
      case 'Guest':
        return ['view_dashboard'];
      default:
        return [];
    }
  };

  const toggleUserStatus = (userId: number) => {
    setUsers(users.map(user => 
      user.id === userId 
        ? { ...user, status: user.status === 'active' ? 'inactive' : 'active' }
        : user
    ));
    
    const user = users.find(u => u.id === userId);
    toast({
      title: "User Status Updated",
      description: `${user?.username} has been ${user?.status === 'active' ? 'deactivated' : 'activated'}.`,
    });
  };

  const deleteUser = (userId: number) => {
    const user = users.find(u => u.id === userId);
    setUsers(users.filter(u => u.id !== userId));
    
    toast({
      title: "User Deleted",
      description: `User ${user?.username} has been deleted.`,
      variant: "destructive",
    });
  };

  return (
    <div className="space-y-6">
      {/* User Statistics */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card className="glass-morphism border-cyber-primary/30">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400">Total Users</p>
                <p className="text-2xl font-bold text-cyber-primary">{users.length}</p>
              </div>
              <Users className="w-8 h-8 text-cyber-primary" />
            </div>
          </CardContent>
        </Card>

        <Card className="glass-morphism border-cyber-primary/30">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400">Active Users</p>
                <p className="text-2xl font-bold text-cyber-primary">
                  {users.filter(u => u.status === 'active').length}
                </p>
              </div>
              <Users className="w-8 h-8 text-cyber-primary" />
            </div>
          </CardContent>
        </Card>

        <Card className="glass-morphism border-cyber-warning/30">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400">Administrators</p>
                <p className="text-2xl font-bold text-cyber-warning">
                  {users.filter(u => u.role === 'Administrator').length}
                </p>
              </div>
              <Shield className="w-8 h-8 text-cyber-warning" />
            </div>
          </CardContent>
        </Card>

        <Card className="glass-morphism border-cyber-secondary/30">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400">Inactive Users</p>
                <p className="text-2xl font-bold text-cyber-secondary">
                  {users.filter(u => u.status === 'inactive').length}
                </p>
              </div>
              <AlertTriangle className="w-8 h-8 text-cyber-secondary" />
            </div>
          </CardContent>
        </Card>
      </div>

      {/* User Management Controls */}
      <Card className="glass-morphism border-cyber-light/30">
        <CardHeader>
          <CardTitle className="flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <Users className="w-5 h-5 text-cyber-primary" />
              <span>User Management</span>
            </div>
            <Dialog open={isAddingUser} onOpenChange={setIsAddingUser}>
              <DialogTrigger asChild>
                <Button className="bg-cyber-primary hover:bg-cyber-primary/80 text-cyber-dark">
                  <UserPlus className="w-4 h-4 mr-2" />
                  Add User
                </Button>
              </DialogTrigger>
              <DialogContent className="bg-cyber-darker border-cyber-light/30">
                <DialogHeader>
                  <DialogTitle className="text-gray-200">Create New User</DialogTitle>
                  <DialogDescription className="text-gray-400">
                    Add a new user to the CyberShield SOC platform
                  </DialogDescription>
                </DialogHeader>
                <div className="space-y-4">
                  <div>
                    <Label htmlFor="username" className="text-gray-300">Username</Label>
                    <Input
                      id="username"
                      value={newUser.username}
                      onChange={(e) => setNewUser({...newUser, username: e.target.value})}
                      className="bg-cyber-dark border-cyber-light/30 text-white"
                      placeholder="Enter username"
                    />
                  </div>
                  <div>
                    <Label htmlFor="email" className="text-gray-300">Email</Label>
                    <Input
                      id="email"
                      type="email"
                      value={newUser.email}
                      onChange={(e) => setNewUser({...newUser, email: e.target.value})}
                      className="bg-cyber-dark border-cyber-light/30 text-white"
                      placeholder="Enter email address"
                    />
                  </div>
                  <div>
                    <Label htmlFor="role" className="text-gray-300">Role</Label>
                    <Select value={newUser.role} onValueChange={(value) => setNewUser({...newUser, role: value})}>
                      <SelectTrigger className="bg-cyber-dark border-cyber-light/30">
                        <SelectValue placeholder="Select role" />
                      </SelectTrigger>
                      <SelectContent className="bg-cyber-darker border-cyber-light/30">
                        {roles.map((role) => (
                          <SelectItem key={role.value} value={role.value}>
                            {role.label}
                          </SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                  </div>
                  <div>
                    <Label htmlFor="password" className="text-gray-300">Password</Label>
                    <Input
                      id="password"
                      type="password"
                      value={newUser.password}
                      onChange={(e) => setNewUser({...newUser, password: e.target.value})}
                      className="bg-cyber-dark border-cyber-light/30 text-white"
                      placeholder="Enter password"
                    />
                  </div>
                </div>
                <DialogFooter>
                  <Button
                    variant="outline"
                    onClick={() => setIsAddingUser(false)}
                    className="border-cyber-light/30"
                  >
                    Cancel
                  </Button>
                  <Button
                    onClick={handleAddUser}
                    className="bg-cyber-primary hover:bg-cyber-primary/80 text-cyber-dark"
                  >
                    Create User
                  </Button>
                </DialogFooter>
              </DialogContent>
            </Dialog>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex flex-wrap gap-4 mb-6">
            <div className="flex items-center space-x-2">
              <Search className="w-4 h-4 text-gray-400" />
              <Input
                placeholder="Search users..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-64 bg-cyber-darker border-cyber-light/30"
              />
            </div>
            
            <Select value={roleFilter} onValueChange={setRoleFilter}>
              <SelectTrigger className="w-40 bg-cyber-darker border-cyber-light/30">
                <SelectValue placeholder="Role" />
              </SelectTrigger>
              <SelectContent className="bg-cyber-darker border-cyber-light/30">
                <SelectItem value="all">All Roles</SelectItem>
                {roles.map((role) => (
                  <SelectItem key={role.value} value={role.value}>
                    {role.label}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>

            <Select value={statusFilter} onValueChange={setStatusFilter}>
              <SelectTrigger className="w-40 bg-cyber-darker border-cyber-light/30">
                <SelectValue placeholder="Status" />
              </SelectTrigger>
              <SelectContent className="bg-cyber-darker border-cyber-light/30">
                <SelectItem value="all">All Statuses</SelectItem>
                <SelectItem value="active">Active</SelectItem>
                <SelectItem value="inactive">Inactive</SelectItem>
              </SelectContent>
            </Select>
          </div>

          {/* Users Table */}
          <div className="overflow-x-auto">
            <Table>
              <TableHeader>
                <TableRow className="border-cyber-light/30">
                  <TableHead className="text-gray-300">Username</TableHead>
                  <TableHead className="text-gray-300">Email</TableHead>
                  <TableHead className="text-gray-300">Role</TableHead>
                  <TableHead className="text-gray-300">Status</TableHead>
                  <TableHead className="text-gray-300">Last Login</TableHead>
                  <TableHead className="text-gray-300">Permissions</TableHead>
                  <TableHead className="text-gray-300">Actions</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {filteredUsers.map((user) => (
                  <TableRow key={user.id} className="border-cyber-light/20 hover:bg-cyber-darker/50">
                    <TableCell className="font-medium text-gray-300">
                      {user.username}
                    </TableCell>
                    <TableCell className="text-gray-300">
                      {user.email}
                    </TableCell>
                    <TableCell>
                      <Badge className={`${getRoleColor(user.role)} text-white`}>
                        {user.role}
                      </Badge>
                    </TableCell>
                    <TableCell>
                      <Badge 
                        variant={user.status === 'active' ? "default" : "destructive"}
                        className={user.status === 'active' ? "bg-cyber-primary text-cyber-dark" : "bg-cyber-accent"}
                      >
                        {user.status}
                      </Badge>
                    </TableCell>
                    <TableCell className="text-sm text-gray-400 font-mono">
                      {user.lastLogin}
                    </TableCell>
                    <TableCell>
                      <div className="flex flex-wrap gap-1">
                        {user.permissions.slice(0, 2).map((permission, index) => (
                          <Badge key={index} variant="outline" className="text-xs border-cyber-light/30">
                            {permission.replace('_', ' ')}
                          </Badge>
                        ))}
                        {user.permissions.length > 2 && (
                          <Badge variant="outline" className="text-xs border-cyber-light/30">
                            +{user.permissions.length - 2} more
                          </Badge>
                        )}
                      </div>
                    </TableCell>
                    <TableCell>
                      <div className="flex items-center space-x-2">
                        <Button
                          size="sm"
                          variant="outline"
                          className="border-cyber-light/30"
                          onClick={() => toggleUserStatus(user.id)}
                        >
                          {user.status === 'active' ? 'Deactivate' : 'Activate'}
                        </Button>
                        <Button
                          size="sm"
                          variant="outline"
                          className="border-cyber-secondary text-cyber-secondary"
                        >
                          <Settings className="w-3 h-3" />
                        </Button>
                        <Button
                          size="sm"
                          variant="destructive"
                          className="bg-cyber-accent hover:bg-cyber-accent/80"
                          onClick={() => deleteUser(user.id)}
                        >
                          Delete
                        </Button>
                      </div>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        </CardContent>
      </Card>

      {/* Security Notice */}
      <Alert className="border-cyber-warning/30 bg-cyber-warning/10">
        <Shield className="h-4 w-4 text-cyber-warning" />
        <AlertDescription className="text-cyber-warning">
          User management actions are logged and monitored. All changes require appropriate authorization.
        </AlertDescription>
      </Alert>
    </div>
  );
};

export default UserManagement;
