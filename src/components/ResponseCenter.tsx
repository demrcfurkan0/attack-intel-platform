
import React, { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Progress } from '@/components/ui/progress';
import { Shield, PlayCircle, StopCircle, Clock, CheckCircle, AlertTriangle, Bot } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';

const ResponseCenter = () => {
  const [selectedResponse, setSelectedResponse] = useState('');
  const [customAction, setCustomAction] = useState('');
  const [executionProgress, setExecutionProgress] = useState(0);
  const [isExecuting, setIsExecuting] = useState(false);
  const { toast } = useToast();

  // Mock recommended responses
  const recommendedResponses = [
    {
      id: 'block_ip',
      title: 'Block Malicious IP',
      description: 'Immediately block the attacking IP address across all network devices',
      severity: 'High',
      estimatedTime: '30 seconds',
      automated: true,
      commands: ['iptables -A INPUT -s 192.168.1.50 -j DROP', 'firewall block 192.168.1.50'],
      risk: 'Low'
    },
    {
      id: 'isolate_host',
      title: 'Isolate Infected Host',
      description: 'Quarantine the compromised workstation to prevent lateral movement',
      severity: 'Critical',
      estimatedTime: '2 minutes',
      automated: true,
      commands: ['network isolate 192.168.1.75', 'disable_network_access 192.168.1.75'],
      risk: 'Medium'
    },
    {
      id: 'enable_ddos_protection',
      title: 'Enable DDoS Protection',
      description: 'Activate advanced DDoS mitigation and rate limiting',
      severity: 'High',
      estimatedTime: '1 minute',
      automated: true,
      commands: ['cloudflare enable_ddos_protection', 'nginx rate_limit 100req/min'],
      risk: 'Low'
    },
    {
      id: 'update_signatures',
      title: 'Update Detection Signatures',
      description: 'Deploy new threat signatures to improve detection accuracy',
      severity: 'Medium',
      estimatedTime: '5 minutes',
      automated: false,
      commands: ['update_ips_signatures', 'restart_detection_engine'],
      risk: 'Low'
    },
    {
      id: 'backup_critical_data',
      title: 'Emergency Data Backup',
      description: 'Create immediate backup of critical systems before further damage',
      severity: 'Critical',
      estimatedTime: '10 minutes',
      automated: false,
      commands: ['backup --critical --destination=secure_vault', 'verify_backup_integrity'],
      risk: 'Low'
    }
  ];

  // Mock response history
  const responseHistory = [
    {
      id: 1,
      action: 'Block Malicious IP',
      target: '203.0.113.0',
      timestamp: '2024-05-22 14:25:00',
      status: 'completed',
      executedBy: 'auto',
      result: 'Successfully blocked IP address and mitigated DDoS attack'
    },
    {
      id: 2,
      action: 'Isolate Infected Host',
      target: 'Workstation 42',
      timestamp: '2024-05-22 14:15:00',
      status: 'completed',
      executedBy: 'admin',
      result: 'Host isolated, malware contained'
    },
    {
      id: 3,
      action: 'Update Detection Signatures',
      target: 'IDS System',
      timestamp: '2024-05-22 13:45:00',
      status: 'in_progress',
      executedBy: 'auto',
      result: 'Signature update 75% complete'
    },
    {
      id: 4,
      action: 'Emergency Data Backup',
      target: 'Database Server',
      timestamp: '2024-05-22 13:30:00',
      status: 'failed',
      executedBy: 'admin',
      result: 'Backup failed due to insufficient storage space'
    }
  ];

  const getSeverityColor = (severity: string) => {
    switch (severity) {
      case 'Critical': return 'bg-cyber-accent';
      case 'High': return 'bg-cyber-warning';
      case 'Medium': return 'bg-cyber-secondary';
      case 'Low': return 'bg-cyber-primary';
      default: return 'bg-gray-500';
    }
  };

  const getRiskColor = (risk: string) => {
    switch (risk) {
      case 'High': return 'text-cyber-accent';
      case 'Medium': return 'text-cyber-warning';
      case 'Low': return 'text-cyber-primary';
      default: return 'text-gray-400';
    }
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'completed': return <CheckCircle className="w-4 h-4 text-cyber-primary" />;
      case 'in_progress': return <Clock className="w-4 h-4 text-cyber-warning" />;
      case 'failed': return <AlertTriangle className="w-4 h-4 text-cyber-accent" />;
      default: return <Clock className="w-4 h-4 text-gray-400" />;
    }
  };

  const executeResponse = (responseId: string) => {
    const response = recommendedResponses.find(r => r.id === responseId);
    if (!response) return;

    setIsExecuting(true);
    setExecutionProgress(0);

    const interval = setInterval(() => {
      setExecutionProgress(prev => {
        if (prev >= 100) {
          clearInterval(interval);
          setIsExecuting(false);
          toast({
            title: "Response Executed",
            description: `${response.title} has been executed successfully.`,
          });
          return 100;
        }
        return prev + 10;
      });
    }, 200);
  };

  const executeCustomAction = () => {
    if (!customAction.trim()) {
      toast({
        title: "Action Required",
        description: "Please enter a custom action before executing.",
        variant: "destructive",
      });
      return;
    }

    setIsExecuting(true);
    setExecutionProgress(0);

    const interval = setInterval(() => {
      setExecutionProgress(prev => {
        if (prev >= 100) {
          clearInterval(interval);
          setIsExecuting(false);
          toast({
            title: "Custom Action Executed",
            description: "Your custom response action has been executed.",
          });
          return 100;
        }
        return prev + 15;
      });
    }, 150);
  };

  return (
    <div className="space-y-6">
      {/* Response Summary */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card className="glass-morphism border-cyber-primary/30">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400">Active Responses</p>
                <p className="text-2xl font-bold text-cyber-primary">3</p>
              </div>
              <PlayCircle className="w-8 h-8 text-cyber-primary" />
            </div>
          </CardContent>
        </Card>

        <Card className="glass-morphism border-cyber-warning/30">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400">Queued Actions</p>
                <p className="text-2xl font-bold text-cyber-warning">2</p>
              </div>
              <Clock className="w-8 h-8 text-cyber-warning" />
            </div>
          </CardContent>
        </Card>

        <Card className="glass-morphism border-cyber-primary/30">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400">Completed Today</p>
                <p className="text-2xl font-bold text-cyber-primary">18</p>
              </div>
              <CheckCircle className="w-8 h-8 text-cyber-primary" />
            </div>
          </CardContent>
        </Card>

        <Card className="glass-morphism border-cyber-accent/30">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-400">Failed Actions</p>
                <p className="text-2xl font-bold text-cyber-accent">1</p>
              </div>
              <StopCircle className="w-8 h-8 text-cyber-accent" />
            </div>
          </CardContent>
        </Card>
      </div>

      {/* AI Recommended Responses */}
      <Card className="glass-morphism border-cyber-light/30">
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <Bot className="w-5 h-5 text-cyber-primary" />
            <span>AI-Recommended Response Actions</span>
          </CardTitle>
          <CardDescription>Intelligent response suggestions based on current threat analysis</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          {recommendedResponses.map((response) => (
            <Alert key={response.id} className="border-cyber-light/30 bg-cyber-darker/50 hover:bg-cyber-darker/70 transition-colors">
              <div className="flex items-start justify-between w-full">
                <div className="flex items-start space-x-4">
                  <Shield className="w-5 h-5 text-cyber-primary mt-1" />
                  <div className="space-y-2 flex-1">
                    <div className="flex items-center space-x-3">
                      <h4 className="font-medium text-gray-200">{response.title}</h4>
                      <Badge className={`${getSeverityColor(response.severity)} text-white`}>
                        {response.severity}
                      </Badge>
                      {response.automated && (
                        <Badge variant="outline" className="border-cyber-primary text-cyber-primary">
                          <Bot className="w-3 h-3 mr-1" />
                          Auto
                        </Badge>
                      )}
                    </div>
                    <AlertDescription className="text-gray-300">
                      {response.description}
                    </AlertDescription>
                    <div className="flex items-center space-x-4 text-sm text-gray-400">
                      <span>ETA: {response.estimatedTime}</span>
                      <span>•</span>
                      <span className={getRiskColor(response.risk)}>Risk: {response.risk}</span>
                    </div>
                    <div className="text-xs text-gray-500 font-mono">
                      Commands: {response.commands.join(' && ')}
                    </div>
                  </div>
                </div>
                
                <div className="flex items-center space-x-2 ml-4">
                  <Button
                    size="sm"
                    className="bg-cyber-primary hover:bg-cyber-primary/80 text-cyber-dark"
                    onClick={() => executeResponse(response.id)}
                    disabled={isExecuting}
                  >
                    <PlayCircle className="w-4 h-4 mr-1" />
                    Execute
                  </Button>
                </div>
              </div>
            </Alert>
          ))}
        </CardContent>
      </Card>

      {/* Custom Response Action */}
      <Card className="glass-morphism border-cyber-light/30">
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <Shield className="w-5 h-5 text-cyber-primary" />
            <span>Custom Response Action</span>
          </CardTitle>
          <CardDescription>Execute manual security response commands</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
            <div className="space-y-4">
              <div>
                <label className="text-sm text-gray-300 mb-2 block">Response Type</label>
                <Select value={selectedResponse} onValueChange={setSelectedResponse}>
                  <SelectTrigger className="bg-cyber-darker border-cyber-light/30">
                    <SelectValue placeholder="Select response type" />
                  </SelectTrigger>
                  <SelectContent className="bg-cyber-darker border-cyber-light/30">
                    <SelectItem value="network">Network Security</SelectItem>
                    <SelectItem value="endpoint">Endpoint Protection</SelectItem>
                    <SelectItem value="data">Data Protection</SelectItem>
                    <SelectItem value="incident">Incident Response</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              
              <div>
                <label className="text-sm text-gray-300 mb-2 block">Custom Action</label>
                <Textarea
                  value={customAction}
                  onChange={(e) => setCustomAction(e.target.value)}
                  placeholder="Enter custom response commands or actions..."
                  className="bg-cyber-darker border-cyber-light/30 text-white h-24"
                />
              </div>
            </div>

            <div className="space-y-4">
              <Alert className="border-cyber-warning/30 bg-cyber-warning/10">
                <AlertTriangle className="h-4 w-4 text-cyber-warning" />
                <AlertDescription className="text-cyber-warning">
                  Custom actions will be executed with elevated privileges. Ensure commands are safe and tested.
                </AlertDescription>
              </Alert>

              <Button
                onClick={executeCustomAction}
                disabled={isExecuting}
                className="w-full bg-cyber-secondary hover:bg-cyber-secondary/80 text-white"
              >
                <PlayCircle className="w-4 h-4 mr-2" />
                Execute Custom Action
              </Button>
            </div>
          </div>

          {/* Execution Progress */}
          {isExecuting && (
            <div className="space-y-2 mt-4">
              <div className="flex justify-between text-sm">
                <span className="text-gray-300">Execution Progress</span>
                <span className="text-cyber-primary">{executionProgress}%</span>
              </div>
              <Progress value={executionProgress} className="h-2" />
              <div className="flex items-center space-x-2 text-sm text-gray-400">
                <div className="status-indicator status-normal animate-pulse"></div>
                <span>Executing response action...</span>
              </div>
            </div>
          )}
        </CardContent>
      </Card>

      {/* Response History */}
      <Card className="glass-morphism border-cyber-light/30">
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <Clock className="w-5 h-5 text-cyber-primary" />
            <span>Response History</span>
          </CardTitle>
          <CardDescription>Recent security response actions and their outcomes</CardDescription>
        </CardHeader>
        <CardContent className="space-y-3">
          {responseHistory.map((entry) => (
            <div key={entry.id} className="flex items-center justify-between p-4 bg-cyber-darker/50 rounded-lg border border-cyber-light/20">
              <div className="flex items-center space-x-4">
                {getStatusIcon(entry.status)}
                <div>
                  <div className="font-medium text-gray-300">{entry.action}</div>
                  <div className="text-sm text-gray-400">Target: {entry.target}</div>
                  <div className="text-xs text-gray-500">{entry.result}</div>
                </div>
              </div>
              <div className="text-right">
                <div className="text-sm text-gray-400">{entry.timestamp}</div>
                <div className="text-xs text-gray-500">by {entry.executedBy}</div>
                <Badge 
                  variant={entry.status === 'completed' ? "default" : entry.status === 'in_progress' ? "secondary" : "destructive"}
                  className={`mt-1 ${entry.status === 'completed' ? 'bg-cyber-primary text-cyber-dark' : 
                    entry.status === 'in_progress' ? 'bg-cyber-warning text-cyber-dark' : 'bg-cyber-accent'}`}
                >
                  {entry.status.replace('_', ' ')}
                </Badge>
              </div>
            </div>
          ))}
        </CardContent>
      </Card>
    </div>
  );
};

export default ResponseCenter;
