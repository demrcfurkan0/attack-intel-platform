
import React, { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Textarea } from '@/components/ui/textarea';
import { Badge } from '@/components/ui/badge';
import { Progress } from '@/components/ui/progress';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Target, Play, Square, Settings, AlertTriangle } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';

const AttackSimulationPanel = () => {
  const [attackType, setAttackType] = useState('');
  const [targetIP, setTargetIP] = useState('192.168.1.100');
  const [duration, setDuration] = useState('60');
  const [intensity, setIntensity] = useState('medium');
  const [isRunning, setIsRunning] = useState(false);
  const [progress, setProgress] = useState(0);
  const { toast } = useToast();

  const attackTypes = [
    { value: 'ddos', label: 'DDoS Attack', description: 'Distributed Denial of Service simulation' },
    { value: 'sql', label: 'SQL Injection', description: 'Database injection attack patterns' },
    { value: 'brute', label: 'Brute Force', description: 'Password cracking simulation' },
    { value: 'malware', label: 'Malware Delivery', description: 'Malicious payload simulation' },
    { value: 'mitm', label: 'Man-in-the-Middle', description: 'Network interception simulation' },
  ];

  const intensityLevels = [
    { value: 'low', label: 'Low', color: 'bg-cyber-primary' },
    { value: 'medium', label: 'Medium', color: 'bg-cyber-warning' },
    { value: 'high', label: 'High', color: 'bg-cyber-accent' },
  ];

  const handleStartSimulation = () => {
    if (!attackType) {
      toast({
        title: "Configuration Required",
        description: "Please select an attack type before starting simulation.",
        variant: "destructive",
      });
      return;
    }

    setIsRunning(true);
    setProgress(0);

    // Simulate attack progress
    const interval = setInterval(() => {
      setProgress((prev) => {
        if (prev >= 100) {
          clearInterval(interval);
          setIsRunning(false);
          toast({
            title: "Simulation Complete",
            description: `${attackTypes.find(a => a.value === attackType)?.label} simulation completed successfully.`,
          });
          return 100;
        }
        return prev + 2;
      });
    }, 100);
  };

  const handleStopSimulation = () => {
    setIsRunning(false);
    setProgress(0);
    toast({
      title: "Simulation Stopped",
      description: "Attack simulation has been terminated.",
      variant: "destructive",
    });
  };

  return (
    <div className="space-y-6">
      <Card className="glass-morphism border-cyber-light/30">
        <CardHeader>
          <CardTitle className="flex items-center space-x-2">
            <Target className="w-5 h-5 text-cyber-primary" />
            <span>Attack Simulation Control Panel</span>
          </CardTitle>
          <CardDescription>Configure and launch cybersecurity attack simulations for testing</CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          {/* Attack Configuration */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div className="space-y-4">
              <div>
                <Label htmlFor="attack-type" className="text-gray-300">Attack Type</Label>
                <Select value={attackType} onValueChange={setAttackType}>
                  <SelectTrigger className="bg-cyber-darker border-cyber-light/30">
                    <SelectValue placeholder="Select attack type" />
                  </SelectTrigger>
                  <SelectContent className="bg-cyber-darker border-cyber-light/30">
                    {attackTypes.map((attack) => (
                      <SelectItem key={attack.value} value={attack.value}>
                        <div className="flex flex-col">
                          <span>{attack.label}</span>
                          <span className="text-xs text-gray-400">{attack.description}</span>
                        </div>
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>

              <div>
                <Label htmlFor="target-ip" className="text-gray-300">Target IP Address</Label>
                <Input
                  id="target-ip"
                  value={targetIP}
                  onChange={(e) => setTargetIP(e.target.value)}
                  className="bg-cyber-darker border-cyber-light/30 text-white"
                  placeholder="192.168.1.100"
                />
              </div>

              <div>
                <Label htmlFor="duration" className="text-gray-300">Duration (seconds)</Label>
                <Input
                  id="duration"
                  type="number"
                  value={duration}
                  onChange={(e) => setDuration(e.target.value)}
                  className="bg-cyber-darker border-cyber-light/30 text-white"
                  placeholder="60"
                />
              </div>

              <div>
                <Label className="text-gray-300">Attack Intensity</Label>
                <div className="flex space-x-2 mt-2">
                  {intensityLevels.map((level) => (
                    <Button
                      key={level.value}
                      variant={intensity === level.value ? "default" : "outline"}
                      onClick={() => setIntensity(level.value)}
                      className={`${intensity === level.value ? level.color : 'border-cyber-light/30'} text-white`}
                    >
                      {level.label}
                    </Button>
                  ))}
                </div>
              </div>
            </div>

            <div className="space-y-4">
              <div>
                <Label htmlFor="custom-params" className="text-gray-300">Custom Parameters</Label>
                <Textarea
                  id="custom-params"
                  placeholder="Enter custom attack parameters (JSON format)"
                  className="bg-cyber-darker border-cyber-light/30 text-white h-32"
                />
              </div>

              <Alert className="border-cyber-warning/30 bg-cyber-warning/10">
                <AlertTriangle className="h-4 w-4 text-cyber-warning" />
                <AlertDescription className="text-cyber-warning">
                  Simulations are conducted in a controlled environment. No actual harm will be caused to target systems.
                </AlertDescription>
              </Alert>
            </div>
          </div>

          {/* Control Buttons */}
          <div className="flex items-center space-x-4">
            <Button
              onClick={handleStartSimulation}
              disabled={isRunning}
              className="bg-cyber-primary hover:bg-cyber-primary/80 text-cyber-dark"
            >
              <Play className="w-4 h-4 mr-2" />
              Start Simulation
            </Button>
            <Button
              onClick={handleStopSimulation}
              disabled={!isRunning}
              variant="destructive"
              className="bg-cyber-accent hover:bg-cyber-accent/80"
            >
              <Square className="w-4 h-4 mr-2" />
              Stop Simulation
            </Button>
            <Button variant="outline" className="border-cyber-light/30">
              <Settings className="w-4 h-4 mr-2" />
              Advanced Config
            </Button>
          </div>

          {/* Progress Display */}
          {isRunning && (
            <div className="space-y-2">
              <div className="flex justify-between text-sm">
                <span className="text-gray-300">Simulation Progress</span>
                <span className="text-cyber-primary">{progress}%</span>
              </div>
              <Progress value={progress} className="h-2" />
              <div className="flex items-center space-x-2 text-sm text-gray-400">
                <div className="status-indicator status-normal animate-pulse"></div>
                <span>Simulation in progress...</span>
              </div>
            </div>
          )}
        </CardContent>
      </Card>

      {/* Recent Simulations */}
      <Card className="glass-morphism border-cyber-light/30">
        <CardHeader>
          <CardTitle>Recent Simulations</CardTitle>
          <CardDescription>History of completed attack simulations</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            {[
              { type: 'DDoS Attack', target: '192.168.1.100', status: 'Completed', time: '2 hours ago', detected: true },
              { type: 'SQL Injection', target: '192.168.1.105', status: 'Completed', time: '4 hours ago', detected: true },
              { type: 'Brute Force', target: '192.168.1.110', status: 'Failed', time: '6 hours ago', detected: false },
            ].map((sim, index) => (
              <div key={index} className="flex items-center justify-between p-4 bg-cyber-darker/50 rounded-lg border border-cyber-light/20">
                <div className="flex items-center space-x-4">
                  <Target className="w-4 h-4 text-cyber-primary" />
                  <div>
                    <div className="font-medium text-gray-300">{sim.type}</div>
                    <div className="text-sm text-gray-400">Target: {sim.target}</div>
                  </div>
                </div>
                <div className="flex items-center space-x-4">
                  <Badge 
                    variant={sim.detected ? "default" : "destructive"}
                    className={sim.detected ? "bg-cyber-primary text-cyber-dark" : "bg-cyber-accent"}
                  >
                    {sim.detected ? "Detected" : "Undetected"}
                  </Badge>
                  <Badge variant="outline" className="border-cyber-light/30">
                    {sim.status}
                  </Badge>
                  <span className="text-sm text-gray-400">{sim.time}</span>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default AttackSimulationPanel;
