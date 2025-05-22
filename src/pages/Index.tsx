
import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Progress } from '@/components/ui/progress';
import AttackTrendsChart from '@/components/AttackTrendsChart';
import DetectionMetricsChart from '@/components/DetectionMetricsChart';
import AttackSimulationPanel from '@/components/AttackSimulationPanel';
import AlertNotificationCenter from '@/components/AlertNotificationCenter';
import AttackLogVisualization from '@/components/AttackLogVisualization';
import ResponseCenter from '@/components/ResponseCenter';
import UserManagement from '@/components/UserManagement';
import { Shield, AlertTriangle, Activity, Target, Users, Settings } from 'lucide-react';

const Index = () => {
  const [currentTime, setCurrentTime] = useState(new Date());
  const [systemStatus, setSystemStatus] = useState('operational');
  const [activeAlerts, setActiveAlerts] = useState(3);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="min-h-screen bg-cyber-dark text-white cyber-grid">
      {/* Header */}
      <header className="border-b border-cyber-light/30 bg-cyber-darker/80 backdrop-blur-sm">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-2">
                <Shield className="w-8 h-8 text-cyber-primary" />
                <h1 className="text-2xl font-bold terminal-text">CyberShield SOC</h1>
              </div>
              <Badge variant="outline" className="border-cyber-primary text-cyber-primary">
                v2.1.0
              </Badge>
            </div>
            
            <div className="flex items-center space-x-6">
              <div className="text-sm text-gray-400">
                {currentTime.toLocaleTimeString()}
              </div>
              <div className="flex items-center space-x-2">
                <div className={`status-indicator ${systemStatus === 'operational' ? 'status-normal' : 'status-warning'}`} />
                <span className="text-sm">System {systemStatus}</span>
              </div>
              <Badge variant="destructive" className="bg-cyber-accent">
                {activeAlerts} Active Alerts
              </Badge>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-6 py-8">
        <Tabs defaultValue="dashboard" className="space-y-6">
          <TabsList className="grid w-full grid-cols-6 bg-cyber-darker border border-cyber-light/30">
            <TabsTrigger value="dashboard" className="data-[state=active]:bg-cyber-primary data-[state=active]:text-cyber-dark">
              <Activity className="w-4 h-4 mr-2" />
              Dashboard
            </TabsTrigger>
            <TabsTrigger value="simulation" className="data-[state=active]:bg-cyber-primary data-[state=active]:text-cyber-dark">
              <Target className="w-4 h-4 mr-2" />
              Simulation
            </TabsTrigger>
            <TabsTrigger value="alerts" className="data-[state=active]:bg-cyber-primary data-[state=active]:text-cyber-dark">
              <AlertTriangle className="w-4 h-4 mr-2" />
              Alerts
            </TabsTrigger>
            <TabsTrigger value="logs" className="data-[state=active]:bg-cyber-primary data-[state=active]:text-cyber-dark">
              <Activity className="w-4 h-4 mr-2" />
              Logs
            </TabsTrigger>
            <TabsTrigger value="response" className="data-[state=active]:bg-cyber-primary data-[state=active]:text-cyber-dark">
              <Shield className="w-4 h-4 mr-2" />
              Response
            </TabsTrigger>
            <TabsTrigger value="users" className="data-[state=active]:bg-cyber-primary data-[state=active]:text-cyber-dark">
              <Users className="w-4 h-4 mr-2" />
              Users
            </TabsTrigger>
          </TabsList>

          <TabsContent value="dashboard" className="space-y-6">
            {/* System Overview Cards */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              <Card className="glass-morphism border-cyber-primary/30 hover:shadow-cyber-glow transition-all duration-300">
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                  <CardTitle className="text-sm font-medium text-gray-300">Active Threats</CardTitle>
                  <AlertTriangle className="h-4 w-4 text-cyber-accent" />
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold text-cyber-accent">12</div>
                  <p className="text-xs text-gray-400">+2 from last hour</p>
                  <Progress value={75} className="mt-2 h-2" />
                </CardContent>
              </Card>

              <Card className="glass-morphism border-cyber-secondary/30 hover:shadow-cyber-glow transition-all duration-300">
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                  <CardTitle className="text-sm font-medium text-gray-300">Detection Rate</CardTitle>
                  <Shield className="h-4 w-4 text-cyber-primary" />
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold text-cyber-primary">94.7%</div>
                  <p className="text-xs text-gray-400">+1.2% from yesterday</p>
                  <Progress value={95} className="mt-2 h-2" />
                </CardContent>
              </Card>

              <Card className="glass-morphism border-cyber-warning/30 hover:shadow-warning-glow transition-all duration-300">
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                  <CardTitle className="text-sm font-medium text-gray-300">Network Load</CardTitle>
                  <Activity className="h-4 w-4 text-cyber-warning" />
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold text-cyber-warning">67%</div>
                  <p className="text-xs text-gray-400">Normal range</p>
                  <Progress value={67} className="mt-2 h-2" />
                </CardContent>
              </Card>

              <Card className="glass-morphism border-cyber-primary/30 hover:shadow-cyber-glow transition-all duration-300">
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                  <CardTitle className="text-sm font-medium text-gray-300">False Positives</CardTitle>
                  <Target className="h-4 w-4 text-cyber-secondary" />
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold text-cyber-secondary">5.3%</div>
                  <p className="text-xs text-gray-400">-0.8% from yesterday</p>
                  <Progress value={5} className="mt-2 h-2" />
                </CardContent>
              </Card>
            </div>

            {/* Charts Section */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <AttackTrendsChart />
              <DetectionMetricsChart />
            </div>

            {/* Recent Alerts */}
            <Card className="glass-morphism border-cyber-light/30">
              <CardHeader>
                <CardTitle className="flex items-center space-x-2">
                  <AlertTriangle className="w-5 h-5 text-cyber-accent" />
                  <span>Recent Security Alerts</span>
                </CardTitle>
                <CardDescription>Latest threat detections and security events</CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                {[
                  { type: 'SQL Injection', severity: 'Critical', target: '192.168.1.100', time: '2 minutes ago' },
                  { type: 'DDoS Attack', severity: 'High', target: 'Web Server', time: '5 minutes ago' },
                  { type: 'Brute Force', severity: 'Medium', target: 'SSH Service', time: '8 minutes ago' },
                ].map((alert, index) => (
                  <Alert key={index} className="border-cyber-light/30 bg-cyber-darker/50">
                    <AlertTriangle className="h-4 w-4" />
                    <AlertDescription className="flex justify-between items-center">
                      <div className="flex items-center space-x-4">
                        <span className="font-medium">{alert.type}</span>
                        <Badge 
                          variant={alert.severity === 'Critical' ? 'destructive' : alert.severity === 'High' ? 'default' : 'secondary'}
                          className={alert.severity === 'Critical' ? 'bg-cyber-accent' : alert.severity === 'High' ? 'bg-cyber-warning' : 'bg-cyber-secondary'}
                        >
                          {alert.severity}
                        </Badge>
                        <span className="text-sm text-gray-400">Target: {alert.target}</span>
                      </div>
                      <span className="text-xs text-gray-500">{alert.time}</span>
                    </AlertDescription>
                  </Alert>
                ))}
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="simulation">
            <AttackSimulationPanel />
          </TabsContent>

          <TabsContent value="alerts">
            <AlertNotificationCenter />
          </TabsContent>

          <TabsContent value="logs">
            <AttackLogVisualization />
          </TabsContent>

          <TabsContent value="response">
            <ResponseCenter />
          </TabsContent>

          <TabsContent value="users">
            <UserManagement />
          </TabsContent>
        </Tabs>
      </main>
    </div>
  );
};

export default Index;
