// src/pages/Index.tsx

import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Progress } from '@/components/ui/progress';
import AttackTrendsChart from '@/components/AttackTrendsChart';
import DetectionMetricsChart from '@/components/DetectionMetricsChart';
import AttackSimulationPanel from '@/components/AttackSimulationPanel';
import AlertNotificationCenter from '@/components/AlertNotificationCenter';
import AttackLogVisualization from '@/components/AttackLogVisualization';
import ResponseCenter from '@/components/ResponseCenter';
import UserManagement from '@/components/UserManagement';
import { Shield, AlertTriangle, Activity, Target, Users, Loader2 } from 'lucide-react';
import { getAttackTrends, getDetectionMetrics } from '@/services/statisticsService';
import { DetectionMetricsResponse } from '@/types/apiTypes';

interface DashboardData {
  detected_attacks: number;
  benign_traffic: number;
  total_simulations: number;
}
interface IndexPageProps {
  data: DashboardData;
  isLoading: boolean;
}

const Index: React.FC<IndexPageProps> = ({ data, isLoading }) => {
  const [currentTime, setCurrentTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => setCurrentTime(new Date()), 1000);
    return () => clearInterval(timer);
  }, []);

  const totalPredictions = data.detected_attacks + data.benign_traffic;
  const detectionRate = totalPredictions > 0 ? (data.detected_attacks / totalPredictions) * 100 : 0;

  return (
    <div className="min-h-screen bg-cyber-dark text-white cyber-grid">
      <header className="sticky top-0 z-50 w-full border-b border-cyber-light/30 bg-cyber-darker/80 backdrop-blur-sm">
        <div className="container mx-auto px-6 py-4">
            <div className="flex items-center justify-between">
                <div className="flex items-center space-x-4">
                    <Shield className="w-8 h-8 text-cyber-primary" />
                    <h1 className="text-2xl font-bold terminal-text">CyberShield SOC</h1>
                    <Badge variant="outline" className="border-cyber-primary text-cyber-primary">v2.1.0</Badge>
                </div>
                <div className="flex items-center space-x-6">
                    <div className="text-sm text-gray-400">{currentTime.toLocaleTimeString()}</div>
                    <div className="flex items-center space-x-2"><div className="status-indicator status-normal" /><span>System operational</span></div>
                    {/* Active Alerts sayısını canlı veriyle güncelleyelim */}
                    <Badge variant="destructive" className="bg-cyber-accent">{isLoading ? '...' : data.detected_attacks} Active Alerts</Badge>
                </div>
            </div>
        </div>
      </header>

      <main className="container mx-auto px-6 py-8">
        <Tabs defaultValue="dashboard" className="w-full">
          
          {/* --- STİL DÜZELTMESİ BURADA --- */}
          <TabsList className="grid w-full grid-cols-6 bg-cyber-darker border border-cyber-light/30">
            <TabsTrigger value="dashboard" className="data-[state=active]:bg-cyber-primary data-[state=active]:text-cyber-dark"><Activity className="w-4 h-4 mr-2" />Dashboard</TabsTrigger>
            <TabsTrigger value="simulation" className="data-[state=active]:bg-cyber-primary data-[state=active]:text-cyber-dark"><Target className="w-4 h-4 mr-2" />Simulation</TabsTrigger>
            <TabsTrigger value="alerts" className="data-[state=active]:bg-cyber-primary data-[state=active]:text-cyber-dark"><AlertTriangle className="w-4 h-4 mr-2" />Alerts</TabsTrigger>
            <TabsTrigger value="logs" className="data-[state=active]:bg-cyber-primary data-[state=active]:text-cyber-dark"><Activity className="w-4 h-4 mr-2" />Logs</TabsTrigger>
            <TabsTrigger value="response" className="data-[state=active]:bg-cyber-primary data-[state=active]:text-cyber-dark"><Shield className="w-4 h-4 mr-2" />Response</TabsTrigger>
            <TabsTrigger value="users" className="data-[state=active]:bg-cyber-primary data-[state=active]:text-cyber-dark"><Users className="w-4 h-4 mr-2" />Users</TabsTrigger>
          </TabsList>
          {/* --- STİL DÜZELTMESİ SONU --- */}
          
          <TabsContent value="dashboard" className="mt-6 space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              <Card className="glass-morphism"><CardHeader><CardTitle className="text-sm font-medium">Detected Attacks</CardTitle></CardHeader><CardContent><div className="text-2xl font-bold text-cyber-accent">{isLoading ? <Loader2 className="h-6 w-6 animate-spin" /> : data.detected_attacks.toLocaleString()}</div></CardContent></Card>
              <Card className="glass-morphism border-cyber-secondary/30"><CardHeader><CardTitle className="text-sm font-medium">Detection Rate</CardTitle></CardHeader><CardContent><div className="text-2xl font-bold text-cyber-primary">{isLoading ? <Loader2 className="h-6 w-6 animate-spin" /> : `${detectionRate.toFixed(1)}%`}</div></CardContent></Card>
              <Card className="glass-morphism"><CardHeader><CardTitle className="text-sm font-medium">Total Simulations</CardTitle></CardHeader><CardContent><div className="text-2xl font-bold text-cyber-warning">{isLoading ? <Loader2 className="h-6 w-6 animate-spin" /> : data.total_simulations.toLocaleString()}</div></CardContent></Card>
              <Card className="glass-morphism"><CardHeader><CardTitle className="text-sm font-medium">Analyzed Benign</CardTitle></CardHeader><CardContent><div className="text-2xl font-bold text-cyber-secondary">{isLoading ? <Loader2 className="h-6 w-6 animate-spin" /> : data.benign_traffic.toLocaleString()}</div></CardContent></Card>
            </div>
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <AttackTrendsChart />
              <DetectionMetricsChart />
            </div>
            <Card className="glass-morphism border-cyber-light/30">
              <CardHeader><CardTitle>Recent Security Alerts</CardTitle><CardDescription>Latest threat detections from AI model</CardDescription></CardHeader>
              <CardContent><AlertNotificationCenter /></CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="simulation"><AttackSimulationPanel /></TabsContent>
          <TabsContent value="alerts"><AlertNotificationCenter /></TabsContent>
          <TabsContent value="logs"><AttackLogVisualization /></TabsContent>
          <TabsContent value="response"><ResponseCenter /></TabsContent>
          <TabsContent value="users"><UserManagement /></TabsContent>
        </Tabs>
      </main>
    </div>
  );
};
export default Index;