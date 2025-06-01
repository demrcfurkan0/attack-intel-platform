
import React, { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Input } from '@/components/ui/input';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ScatterChart, Scatter } from 'recharts';
import { Activity, Filter, Download, Calendar, Search } from 'lucide-react';

const AttackLogVisualization = () => {
  const [dateRange, setDateRange] = useState('24h');
  const [attackTypeFilter, setAttackTypeFilter] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');

  // Mock attack log data
  const attackLogs = [
    {
      id: 1,
      timestamp: '2024-05-22 14:30:15',
      type: 'SQL Injection',
      sourceIP: '192.168.1.50',
      targetIP: '10.0.0.100',
      severity: 'Critical',
      detected: true,
      blocked: true,
      confidence: 95.7,
      payload: "'; DROP TABLE users; --"
    },
    {
      id: 2,
      timestamp: '2024-05-22 14:25:32',
      type: 'DDoS',
      sourceIP: '203.0.113.0',
      targetIP: '10.0.0.50',
      severity: 'High',
      detected: true,
      blocked: true,
      confidence: 89.3,
      payload: 'TCP SYN Flood'
    },
    {
      id: 3,
      timestamp: '2024-05-22 14:18:45',
      type: 'Brute Force',
      sourceIP: '198.51.100.25',
      targetIP: '10.0.0.22',
      severity: 'Medium',
      detected: true,
      blocked: false,
      confidence: 87.1,
      payload: 'SSH Login Attempts'
    },
    {
      id: 4,
      timestamp: '2024-05-22 14:15:20',
      type: 'Malware',
      sourceIP: '192.168.1.75',
      targetIP: '10.0.0.200',
      severity: 'High',
      detected: true,
      blocked: true,
      confidence: 92.4,
      payload: 'trojan.exe'
    },
    {
      id: 5,
      timestamp: '2024-05-22 14:10:05',
      type: 'Port Scan',
      sourceIP: '172.16.0.10',
      targetIP: '10.0.0.0/24',
      severity: 'Low',
      detected: false,
      blocked: false,
      confidence: 45.2,
      payload: 'TCP Connect Scan'
    }
  ];

  // Mock time series data for attack patterns
  const attackTimelineData = [
    { time: '14:00', attacks: 2, detected: 2, blocked: 1 },
    { time: '14:05', attacks: 1, detected: 1, blocked: 1 },
    { time: '14:10', attacks: 3, detected: 2, blocked: 2 },
    { time: '14:15', attacks: 4, detected: 4, blocked: 3 },
    { time: '14:20', attacks: 2, detected: 2, blocked: 2 },
    { time: '14:25', attacks: 5, detected: 4, blocked: 4 },
    { time: '14:30', attacks: 3, detected: 3, blocked: 3 },
  ];

  // Mock accuracy scatter plot data
  const accuracyData = [
    { confidence: 95.7, accuracy: 98, type: 'SQL Injection' },
    { confidence: 89.3, accuracy: 94, type: 'DDoS' },
    { confidence: 87.1, accuracy: 91, type: 'Brute Force' },
    { confidence: 92.4, accuracy: 96, type: 'Malware' },
    { confidence: 45.2, accuracy: 52, type: 'Port Scan' },
    { confidence: 78.9, accuracy: 85, type: 'XSS' },
    { confidence: 91.2, accuracy: 93, type: 'CSRF' },
  ];

  const filteredLogs = attackLogs.filter(log => {
    const matchesType = attackTypeFilter === 'all' || log.type === attackTypeFilter;
    const matchesSearch = searchTerm === '' || 
      log.type.toLowerCase().includes(searchTerm.toLowerCase()) ||
      log.sourceIP.includes(searchTerm) ||
      log.targetIP.includes(searchTerm);
    return matchesType && matchesSearch;
  });

  const getSeverityColor = (severity: string) => {
    switch (severity) {
      case 'Critical': return 'bg-cyber-accent';
      case 'High': return 'bg-cyber-warning';
      case 'Medium': return 'bg-cyber-secondary';
      case 'Low': return 'bg-cyber-primary';
      default: return 'bg-gray-500';
    }
  };

  return (
    <div className="space-y-6">
      {/* Controls */}
      <Card className="glass-morphism border-cyber-light/30">
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <Filter className="w-5 h-5 text-cyber-primary" />
            <span>Log Analysis Controls</span>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex flex-wrap gap-4">
            <div className="flex items-center space-x-2">
              <Search className="w-4 h-4 text-gray-400" />
              <Input
                placeholder="Search logs..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-64 bg-cyber-darker border-cyber-light/30"
              />
            </div>
            
            <Select value={dateRange} onValueChange={setDateRange}>
              <SelectTrigger className="w-40 bg-cyber-darker border-cyber-light/30">
                <SelectValue />
              </SelectTrigger>
              <SelectContent className="bg-cyber-darker border-cyber-light/30">
                <SelectItem value="1h">Last Hour</SelectItem>
                <SelectItem value="24h">Last 24 Hours</SelectItem>
                <SelectItem value="7d">Last 7 Days</SelectItem>
                <SelectItem value="30d">Last 30 Days</SelectItem>
              </SelectContent>
            </Select>

            <Select value={attackTypeFilter} onValueChange={setAttackTypeFilter}>
              <SelectTrigger className="w-40 bg-cyber-darker border-cyber-light/30">
                <SelectValue />
              </SelectTrigger>
              <SelectContent className="bg-cyber-darker border-cyber-light/30">
                <SelectItem value="all">All Types</SelectItem>
                <SelectItem value="SQL Injection">SQL Injection</SelectItem>
                <SelectItem value="DDoS">DDoS</SelectItem>
                <SelectItem value="Brute Force">Brute Force</SelectItem>
                <SelectItem value="Malware">Malware</SelectItem>
                <SelectItem value="Port Scan">Port Scan</SelectItem>
              </SelectContent>
            </Select>

            <Button variant="outline" className="border-cyber-light/30">
              <Download className="w-4 h-4 mr-2" />
              Export
            </Button>
          </div>
        </CardContent>
      </Card>

      {/* Visualization Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Attack Timeline */}
        <Card className="glass-morphism border-cyber-light/30 chart-container">
          <CardHeader>
            <CardTitle className="flex items-center space-x-2">
              <Activity className="w-5 h-5 text-cyber-primary" />
              <span>Attack Timeline</span>
            </CardTitle>
            <CardDescription>Real-time attack detection and blocking statistics</CardDescription>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={250}>
              <LineChart data={attackTimelineData}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(0, 255, 136, 0.1)" />
                <XAxis 
                  dataKey="time" 
                  stroke="#00ff88" 
                  fontSize={12}
                  tickLine={false}
                  axisLine={false}
                />
                <YAxis 
                  stroke="#00ff88" 
                  fontSize={12}
                  tickLine={false}
                  axisLine={false}
                />
                <Tooltip 
                  contentStyle={{
                    backgroundColor: 'rgba(10, 15, 28, 0.9)',
                    border: '1px solid rgba(0, 255, 136, 0.3)',
                    borderRadius: '8px',
                    color: '#00ff88'
                  }}
                />
                <Line 
                  type="monotone" 
                  dataKey="attacks" 
                  stroke="#ff4444" 
                  strokeWidth={2}
                  dot={{ fill: '#ff4444', strokeWidth: 2, r: 4 }}
                />
                <Line 
                  type="monotone" 
                  dataKey="detected" 
                  stroke="#ffaa00" 
                  strokeWidth={2}
                  dot={{ fill: '#ffaa00', strokeWidth: 2, r: 4 }}
                />
                <Line 
                  type="monotone" 
                  dataKey="blocked" 
                  stroke="#00ff88" 
                  strokeWidth={2}
                  dot={{ fill: '#00ff88', strokeWidth: 2, r: 4 }}
                />
              </LineChart>
            </ResponsiveContainer>
            <div className="flex justify-center space-x-6 mt-4">
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-cyber-accent rounded-full"></div>
                <span className="text-sm text-gray-400">Total Attacks</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-cyber-warning rounded-full"></div>
                <span className="text-sm text-gray-400">Detected</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-cyber-primary rounded-full"></div>
                <span className="text-sm text-gray-400">Blocked</span>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Detection Accuracy Scatter Plot */}
        <Card className="glass-morphism border-cyber-light/30 chart-container">
          <CardHeader>
            <CardTitle className="flex items-center space-x-2">
              <Activity className="w-5 h-5 text-cyber-primary" />
              <span>Detection Accuracy</span>
            </CardTitle>
            <CardDescription>Confidence vs. accuracy correlation analysis</CardDescription>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={250}>
              <ScatterChart data={accuracyData}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(0, 255, 136, 0.1)" />
                <XAxis 
                  type="number"
                  dataKey="confidence"
                  name="Confidence"
                  domain={[0, 100]}
                  stroke="#00ff88" 
                  fontSize={12}
                  tickLine={false}
                  axisLine={false}
                />
                <YAxis 
                  type="number"
                  dataKey="accuracy"
                  name="Accuracy"
                  domain={[0, 100]}
                  stroke="#00ff88" 
                  fontSize={12}
                  tickLine={false}
                  axisLine={false}
                />
                <Tooltip 
                  cursor={{ strokeDasharray: '3 3' }}
                  contentStyle={{
                    backgroundColor: 'rgba(10, 15, 28, 0.9)',
                    border: '1px solid rgba(0, 255, 136, 0.3)',
                    borderRadius: '8px',
                    color: '#00ff88'
                  }}
                />
                <Scatter dataKey="accuracy" fill="#00ff88" />
              </ScatterChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>
      </div>

      {/* Attack Log Table */}
      <Card className="glass-morphism border-cyber-light/30">
        <CardHeader>
          <CardTitle className="flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <Activity className="w-5 h-5 text-cyber-primary" />
              <span>Attack Log Details</span>
            </div>
            <Badge variant="outline" className="border-cyber-light/30">
              {filteredLogs.length} entries
            </Badge>
          </CardTitle>
          <CardDescription>Detailed security event logs and attack signatures</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="overflow-x-auto">
            <Table>
              <TableHeader>
                <TableRow className="border-cyber-light/30">
                  <TableHead className="text-gray-300">Timestamp</TableHead>
                  <TableHead className="text-gray-300">Type</TableHead>
                  <TableHead className="text-gray-300">Source IP</TableHead>
                  <TableHead className="text-gray-300">Target IP</TableHead>
                  <TableHead className="text-gray-300">Severity</TableHead>
                  <TableHead className="text-gray-300">Status</TableHead>
                  <TableHead className="text-gray-300">Confidence</TableHead>
                  <TableHead className="text-gray-300">Payload</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {filteredLogs.map((log) => (
                  <TableRow key={log.id} className="border-cyber-light/20 hover:bg-cyber-darker/50">
                    <TableCell className="font-mono text-sm text-gray-300">
                      {log.timestamp}
                    </TableCell>
                    <TableCell>
                      <Badge variant="outline" className="border-cyber-secondary text-cyber-secondary">
                        {log.type}
                      </Badge>
                    </TableCell>
                    <TableCell className="font-mono text-sm text-gray-300">
                      {log.sourceIP}
                    </TableCell>
                    <TableCell className="font-mono text-sm text-gray-300">
                      {log.targetIP}
                    </TableCell>
                    <TableCell>
                      <Badge className={`${getSeverityColor(log.severity)} text-white`}>
                        {log.severity}
                      </Badge>
                    </TableCell>
                    <TableCell>
                      <div className="flex items-center space-x-2">
                        <Badge 
                          variant={log.detected ? "default" : "destructive"}
                          className={log.detected ? "bg-cyber-primary text-cyber-dark" : "bg-cyber-accent"}
                        >
                          {log.detected ? "Detected" : "Missed"}
                        </Badge>
                        {log.blocked && (
                          <Badge className="bg-cyber-warning text-cyber-dark">
                            Blocked
                          </Badge>
                        )}
                      </div>
                    </TableCell>
                    <TableCell className="text-center">
                      <span className={`font-mono ${log.confidence > 80 ? 'text-cyber-primary' : log.confidence > 60 ? 'text-cyber-warning' : 'text-cyber-accent'}`}>
                        {log.confidence}%
                      </span>
                    </TableCell>
                    <TableCell className="font-mono text-sm text-gray-400 max-w-xs truncate">
                      {log.payload}
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default AttackLogVisualization;
