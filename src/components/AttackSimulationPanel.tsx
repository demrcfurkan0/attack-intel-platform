import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Badge } from '@/components/ui/badge';
import { Target, Play, Square, Settings, AlertTriangle, Loader2 } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';

import {
  startDdosSimulation,
  startBruteForceSimulation,
  startSqliSimulation
} from '../services/simulationService';
import { getSimulationLogs } from '../services/reportService';
import {
  DDoSParams,
  BruteForceParams,
  SQLInjectionParams,
  SimulationLog
} from '../types/apiTypes';

const AttackSimulationPanel = () => {
  const [attackType, setAttackType] = useState<'ddos' | 'brute_force' | 'sql_injection' | ''>('');
  const [target, setTarget] = useState('https://httpbin.org/get');
  const [params, setParams] = useState<any>({}); // Saldırı tipine göre değişen parametreler

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [recentSimulations, setRecentSimulations] = useState<SimulationLog[]>([]);
  const [isLoadingLogs, setIsLoadingLogs] = useState(true);
  const { toast } = useToast();

  const attackTypes = [
    { value: 'ddos', label: 'DDoS Attack' },
    { value: 'brute_force', label: 'Brute Force' },
    { value: 'sql_injection', label: 'SQL Injection' },
  ];

  // Son simülasyonları çekmek için fonksiyon
  const fetchRecentSimulations = async () => {
    try {
      const response = await getSimulationLogs({ limit: 5 });
      setRecentSimulations(response.data.data);
    } catch (error) {
      console.error("Failed to fetch recent simulations:", error);
      toast({ variant: "destructive", title: "Could not load recent simulations." });
    } finally {
      setIsLoadingLogs(false);
    }
  };

  // Bileşen yüklendiğinde ve simülasyon bittiğinde logları çek
  useEffect(() => {
    fetchRecentSimulations();
  }, []);

  // Periyodik olarak logları yenile (gerçek zamanlı hissi için)
  useEffect(() => {
    const interval = setInterval(() => {
        fetchRecentSimulations();
    }, 10000); // her 10 saniyede bir
    return () => clearInterval(interval);
  }, []);

  const handleParamChange = (field: string, value: any) => {
    setParams((prev: any) => ({ ...prev, [field]: value }));
  };

  const handleStartSimulation = async () => {
    if (!attackType) {
      toast({ title: "Configuration Required", description: "Please select an attack type.", variant: "destructive" });
      return;
    }
    
    setIsSubmitting(true);
    
    try {
      let response;
      const commonPayload = { target_url: target, ...params };

      switch (attackType) {
        case 'ddos':
          response = await startDdosSimulation(commonPayload as DDoSParams);
          break;
        case 'brute_force':
          response = await startBruteForceSimulation(commonPayload as BruteForceParams);
          break;
        case 'sql_injection':
          response = await startSqliSimulation(commonPayload as SQLInjectionParams);
          break;
        default:
          throw new Error("Invalid attack type");
      }
      
      toast({
        title: "Simulation Started! 🚀",
        description: `${attackTypes.find(a => a.value === attackType)?.label} running in background. ID: ${response.data.simulation_run_id}`,
      });
      // Simülasyon başladıktan kısa bir süre sonra listeyi yenile
      setTimeout(fetchRecentSimulations, 2000);

    } catch (error: any) {
      toast({
        variant: "destructive",
        title: "Simulation Failed to Start",
        description: error.response?.data?.detail || "An unknown error occurred.",
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  // Saldırı tipine göre dinamik form render eden fonksiyon
  const renderAttackParams = () => {
    switch (attackType) {
      case 'ddos':
        return (
          <>
            <div>
              <Label htmlFor="num_requests">Number of Requests</Label>
              <Input id="num_requests" type="number" placeholder="1000" onChange={(e) => handleParamChange('num_requests', parseInt(e.target.value))} />
            </div>
            <div>
              <Label htmlFor="concurrency">Concurrency</Label>
              <Input id="concurrency" type="number" placeholder="50" onChange={(e) => handleParamChange('concurrency', parseInt(e.target.value))} />
            </div>
          </>
        );
      case 'brute_force':
        return (
          <div>
            <Label htmlFor="passwords">Passwords (comma separated)</Label>
            <Input id="passwords" placeholder="password,123456,admin" onChange={(e) => handleParamChange('passwords', e.target.value.split(',').map(p => p.trim()))} />
          </div>
        );
      case 'sql_injection':
        return (
          <div>
            <Label htmlFor="param_to_inject">Parameter to Inject</Label>
            <Input id="param_to_inject" placeholder="id" onChange={(e) => handleParamChange('param_to_inject', e.target.value)} />
          </div>
        );
      default:
        return <p className="text-gray-400 text-sm">Select an attack type to see its parameters.</p>;
    }
  };

  return (
    <div className="space-y-6">
      <Card className="glass-morphism border-cyber-light/30">
        <CardHeader>
          <CardTitle>Attack Simulation Control Panel</CardTitle>
          <CardDescription>Configure and launch cybersecurity attack simulations</CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-4">
              <Label htmlFor="attack-type">Attack Type</Label>
              <Select onValueChange={(value: any) => setAttackType(value)}>
                  <SelectTrigger><SelectValue placeholder="Select attack type" /></SelectTrigger>
                  <SelectContent>
                    {attackTypes.map((attack) => <SelectItem key={attack.value} value={attack.value}>{attack.label}</SelectItem>)}
                  </SelectContent>
              </Select>
            </div>
            <div className="space-y-4">
              <Label htmlFor="target">Target URL</Label>
              <Input id="target" value={target} onChange={(e) => setTarget(e.target.value)} placeholder="http://example.com/login" />
            </div>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {renderAttackParams()}
          </div>
          <Button onClick={handleStartSimulation} disabled={isSubmitting || !attackType}>
            {isSubmitting ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : <Play className="w-4 h-4 mr-2" />}
            Launch Simulation
          </Button>
        </CardContent>
      </Card>
      
      {/* Recent Simulations (Canlı Veri) */}
      <Card className="glass-morphism border-cyber-light/30">
        <CardHeader>
          <CardTitle>Recent Simulations</CardTitle>
          <CardDescription>History of completed attack simulations</CardDescription>
        </CardHeader>
        <CardContent>
          {isLoadingLogs ? <p>Loading logs...</p> : (
            <div className="space-y-3">
              {recentSimulations.map((sim) => (
                <div key={sim.simulation_id} className="flex items-center justify-between p-4 bg-cyber-darker/50 rounded-lg">
                  <div>
                    <div className="font-medium text-gray-300">{sim.simulation_type.toUpperCase()}</div>
                    <div className="text-sm text-gray-400">Target: {sim.target_details.url}</div>
                  </div>
                  <div className="flex items-center space-x-4">
                    <Badge variant={sim.status === 'completed' ? 'default' : sim.status === 'failed' ? 'destructive' : 'secondary'}>
                      {sim.status}
                    </Badge>
                    <span className="text-sm text-gray-400">{new Date(sim.start_time).toLocaleTimeString()}</span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
};

export default AttackSimulationPanel;