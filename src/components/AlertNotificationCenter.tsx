
import React, { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Input } from '@/components/ui/input';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { AlertTriangle, Bell, Filter, Search, X, CheckCircle, Clock } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';

const AlertNotificationCenter = () => {
  const [alerts, setAlerts] = useState([
    {
      id: 1,
      type: 'SQL Injection',
      severity: 'Critical',
      target: '192.168.1.100',
      description: 'Malicious SQL injection attempt detected on login form',
      timestamp: '2024-05-22 14:30:15',
      status: 'active',
      source: 'WAF',
      recommendation: 'Block source IP and review application security'
    },
    {
      id: 2,
      type: 'DDoS Attack',
      severity: 'High',
      target: 'Web Server Pool',
      description: 'Distributed denial of service attack targeting web infrastructure',
      timestamp: '2024-05-22 14:25:32',
      status: 'investigating',
      source: 'Network Monitor',
      recommendation: 'Enable DDoS protection and rate limiting'
    },
    {
      id: 3,
      type: 'Brute Force',
      severity: 'Medium',
      target: 'SSH Service',
      description: 'Multiple failed login attempts from suspicious IP addresses',
      timestamp: '2024-05-22 14:18:45',
      status: 'resolved',
      source: 'IDS',
      recommendation: 'Implement account lockout policies'
    },
    {
      id: 4,
      type: 'Malware Detection',
      severity: 'High',
      target: 'Workstation 42',
      description: 'Suspicious executable detected and quarantined',
      timestamp: '2024-05-22 14:15:20',
      status: 'active',
      source: 'Endpoint Protection',
      recommendation: 'Run full system scan and isolate machine'
    },
    {
      id: 5,
      type: 'Data Exfiltration',
      severity: 'Critical',
      target: 'Database Server',
      description: 'Unusual data access patterns detected',
      timestamp: '2024-05-22 14:10:05',
      status: 'investigating',
      source: 'DLP',
      recommendation: 'Review access logs and monitor data flows'
    }
  ]);

  const [filterSeverity, setFilterSeverity] = useState('all');
  const [filterStatus, setFilterStatus] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');
  const { toast } = useToast();

  const getSeverityColor = (severity: string) => {
    switch (severity) {
      case 'Critical': return 'bg-cyber-accent';
      case 'High': return 'bg-cyber-warning';
      case 'Medium': return 'bg-cyber-secondary';
      case 'Low': return 'bg-cyber-primary';
      default: return 'bg-gray-500';
    }
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'active': return <AlertTriangle className="w-4 h-4 text-cyber-accent" />;
      case 'investigating': return <Clock className="w-4 h-4 text-cyber-warning" />;
      case 'resolved': return <CheckCircle className="w-4 h-4 text-cyber-primary" />;
      default: return <Bell className="w-4 h-4" />;
    }
  };

  const filteredAlerts = alerts.filter(alert => {
    const matchesSeverity = filterSeverity === 'all' || alert.severity === filterSeverity;
    const matchesStatus = filterStatus === 'all' || alert.status === filterStatus;
    const matchesSearch = searchTerm === '' || 
      alert.type.toLowerCase().includes(searchTerm.toLowerCase()) ||
      alert.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
      alert.target.toLowerCase().includes(searchTerm.toLowerCase());
    
    return matchesSeverity && matchesStatus && matchesSearch;
  });

  const handleAlertAction = (alertId: number, action: string) => {
    setAlerts(alerts.map(alert => 
      alert.id === alertId 
        ? { ...alert, status: action === 'resolve' ? 'resolved' : 'investigating' }
        : alert
    ));
    
    toast({
      title: "Alert Updated",
      description: `Alert has been marked as ${action === 'resolve' ? 'resolved' : 'under investigation'}.`,
    });
  };

  const dismissAlert = (alertId: number) => {
    setAlerts(alerts.filter(alert => alert.id !== alertId));
    toast({
      title: "Alert Dismissed",
      description: "Alert has been removed from the active list.",
    });
  };

  return (
    <div className="space-y-6">
      {/* Alert Summary */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card className="glass-morphism border-cyber-accent/30">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400">Critical Alerts</p>
                <p className="text-2xl font-bold text-cyber-accent">
                  {alerts.filter(a => a.severity === 'Critical' && a.status === 'active').length}
                </p>
              </div>
              <AlertTriangle className="w-8 h-8 text-cyber-accent" />
            </div>
          </CardContent>
        </Card>

        <Card className="glass-morphism border-cyber-warning/30">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400">High Priority</p>
                <p className="text-2xl font-bold text-cyber-warning">
                  {alerts.filter(a => a.severity === 'High' && a.status === 'active').length}
                </p>
              </div>
              <Bell className="w-8 h-8 text-cyber-warning" />
            </div>
          </CardContent>
        </Card>

        <Card className="glass-morphism border-cyber-secondary/30">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400">Under Investigation</p>
                <p className="text-2xl font-bold text-cyber-secondary">
                  {alerts.filter(a => a.status === 'investigating').length}
                </p>
              </div>
              <Clock className="w-8 h-8 text-cyber-secondary" />
            </div>
          </CardContent>
        </Card>

        <Card className="glass-morphism border-cyber-primary/30">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400">Resolved Today</p>
                <p className="text-2xl font-bold text-cyber-primary">
                  {alerts.filter(a => a.status === 'resolved').length}
                </p>
              </div>
              <CheckCircle className="w-8 h-8 text-cyber-primary" />
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Filters and Search */}
      <Card className="glass-morphism border-cyber-light/30">
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <Filter className="w-5 h-5 text-cyber-primary" />
            <span>Alert Filters</span>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex flex-wrap gap-4">
            <div className="flex items-center space-x-2">
              <Search className="w-4 h-4 text-gray-400" />
              <Input
                placeholder="Search alerts..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-64 bg-cyber-darker border-cyber-light/30"
              />
            </div>
            
            <Select value={filterSeverity} onValueChange={setFilterSeverity}>
              <SelectTrigger className="w-40 bg-cyber-darker border-cyber-light/30">
                <SelectValue placeholder="Severity" />
              </SelectTrigger>
              <SelectContent className="bg-cyber-darker border-cyber-light/30">
                <SelectItem value="all">All Severities</SelectItem>
                <SelectItem value="Critical">Critical</SelectItem>
                <SelectItem value="High">High</SelectItem>
                <SelectItem value="Medium">Medium</SelectItem>
                <SelectItem value="Low">Low</SelectItem>
              </SelectContent>
            </Select>

            <Select value={filterStatus} onValueChange={setFilterStatus}>
              <SelectTrigger className="w-40 bg-cyber-darker border-cyber-light/30">
                <SelectValue placeholder="Status" />
              </SelectTrigger>
              <SelectContent className="bg-cyber-darker border-cyber-light/30">
                <SelectItem value="all">All Statuses</SelectItem>
                <SelectItem value="active">Active</SelectItem>
                <SelectItem value="investigating">Investigating</SelectItem>
                <SelectItem value="resolved">Resolved</SelectItem>
              </SelectContent>
            </Select>

            <Button 
              variant="outline" 
              className="border-cyber-light/30"
              onClick={() => {
                setFilterSeverity('all');
                setFilterStatus('all');
                setSearchTerm('');
              }}
            >
              Clear Filters
            </Button>
          </div>
        </CardContent>
      </Card>

      {/* Alert List */}
      <Card className="glass-morphism border-cyber-light/30">
        <CardHeader>
          <CardTitle className="flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <Bell className="w-5 h-5 text-cyber-primary" />
              <span>Security Alerts</span>
            </div>
            <Badge variant="outline" className="border-cyber-light/30">
              {filteredAlerts.length} alerts
            </Badge>
          </CardTitle>
          <CardDescription>Real-time security threats and incidents</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          {filteredAlerts.map((alert) => (
            <Alert key={alert.id} className="border-cyber-light/30 bg-cyber-darker/50 hover:bg-cyber-darker/70 transition-colors">
              <div className="flex items-start justify-between w-full">
                <div className="flex items-start space-x-4">
                  {getStatusIcon(alert.status)}
                  <div className="space-y-2 flex-1">
                    <div className="flex items-center space-x-3">
                      <h4 className="font-medium text-gray-200">{alert.type}</h4>
                      <Badge className={`${getSeverityColor(alert.severity)} text-white`}>
                        {alert.severity}
                      </Badge>
                      <Badge variant="outline" className="border-cyber-light/30 text-xs">
                        {alert.source}
                      </Badge>
                    </div>
                    <AlertDescription className="text-gray-300">
                      {alert.description}
                    </AlertDescription>
                    <div className="flex items-center space-x-4 text-sm text-gray-400">
                      <span>Target: {alert.target}</span>
                      <span>•</span>
                      <span>{alert.timestamp}</span>
                    </div>
                    <div className="text-sm text-cyber-primary">
                      <strong>Recommendation:</strong> {alert.recommendation}
                    </div>
                  </div>
                </div>
                
                <div className="flex items-center space-x-2 ml-4">
                  {alert.status === 'active' && (
                    <>
                      <Button
                        size="sm"
                        variant="outline"
                        className="border-cyber-warning text-cyber-warning hover:bg-cyber-warning hover:text-cyber-dark"
                        onClick={() => handleAlertAction(alert.id, 'investigate')}
                      >
                        Investigate
                      </Button>
                      <Button
                        size="sm"
                        className="bg-cyber-primary hover:bg-cyber-primary/80 text-cyber-dark"
                        onClick={() => handleAlertAction(alert.id, 'resolve')}
                      >
                        Resolve
                      </Button>
                    </>
                  )}
                  <Button
                    size="sm"
                    variant="ghost"
                    className="text-gray-400 hover:text-white"
                    onClick={() => dismissAlert(alert.id)}
                  >
                    <X className="w-4 h-4" />
                  </Button>
                </div>
              </div>
            </Alert>
          ))}
        </CardContent>
      </Card>
    </div>
  );
};

export default AlertNotificationCenter;
