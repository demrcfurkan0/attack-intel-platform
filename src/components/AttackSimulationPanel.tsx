import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Badge } from '@/components/ui/badge';
import { Target as TargetIcon, Play, Loader2 } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';
import { Progress } from '@/components/ui/progress';
import { useQuery, useQueryClient } from '@tanstack/react-query';

import { useSimulationSocket } from '../hooks/useSimulationSocket';
import { startDdosSimulation, startBruteForceSimulation, startSqliSimulation, startSynFloodSimulation } from '../services/simulationService';
import { getSimulationLogs } from '../services/reportService';
import { SimulationLog } from '../types/apiTypes';

const AttackSimulationPanel = () => {
    const [attackType, setAttackType] = useState<'ddos' | 'brute_force' | 'sql_injection' | 'syn_flood' | ''>('');
    const [target, setTarget] = useState('127.0.0.1'); // Default olarak IP adresi ile başlatalım
    const [params, setParams] = useState<any>({});
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [activeSimulationId, setActiveSimulationId] = useState<string | null>(null);
    const { toast } = useToast();
    const queryClient = useQueryClient();

    const attackTypes = [
        { value: 'ddos', label: 'DDoS Attack (HTTP)' },
        { value: 'brute_force', label: 'Brute Force' },
        { value: 'sql_injection', label: 'SQL Injection' },
        { value: 'syn_flood', label: 'SYN Flood (Network)' },
    ];

    const { data: recentSimulations, isLoading: isLoadingLogs } = useQuery({
        queryKey: ['recentSimulations'],
        queryFn: () => getSimulationLogs({ limit: 5 }),
        refetchInterval: 5000,
    });
    
    const { statusMessage, progress, isFinished } = useSimulationSocket(activeSimulationId);

    useEffect(() => {
        if (isFinished) {
            setActiveSimulationId(null);
            queryClient.invalidateQueries({ queryKey: ['recentSimulations'] });
        }
    }, [isFinished, queryClient]);

    const handleParamChange = (field: string, value: any) => setParams((prev) => ({ ...prev, [field]: value }));
    const handleNumericParamChange = (field: string, value: string) => handleParamChange(field, parseInt(value) || undefined);

    const handleStartSimulation = async () => {
        if (!attackType) {
            toast({ title: "Configuration Required", description: "Please select an attack type.", variant: "destructive" });
            return;
        }

        if (attackType === 'sql_injection' && (!params.param_to_inject || params.param_to_inject.trim() === '')) {
            toast({ variant: "destructive", title: "Field Required", description: "Please enter the parameter name for SQL Injection." });
            return;
        }

        setIsSubmitting(true);
        try {
            let response;
            // SYN Flood için payload yapısı farklı, diğerleri için aynı
            const payload = attackType === 'syn_flood' 
                ? { target_ip: target, ...params }
                : { target_url: target, ...params };

            switch (attackType) {
                case 'ddos': response = await startDdosSimulation(payload); break;
                case 'brute_force': response = await startBruteForceSimulation(payload); break;
                case 'sql_injection': response = await startSqliSimulation(payload); break;
                case 'syn_flood': response = await startSynFloodSimulation(payload); break;
                default: throw new Error("Invalid attack type selected");
            }
            setActiveSimulationId(response.data.simulation_run_id);
            toast({ title: "Simulation Initialized! 🚀", description: "Connecting to real-time feed..." });
            
            setTimeout(() => {
                queryClient.invalidateQueries({ queryKey: ['recentSimulations'] });
            }, 1000);

        } catch (error: any) {
            const errorMessage = error.response?.data?.detail?.[0]?.msg || error.response?.data?.detail || "An unknown error occurred.";
            toast({ variant: "destructive", title: "Simulation Failed to Start", description: String(errorMessage) });
        } finally {
            setIsSubmitting(false);
        }
    };
    
    const renderAttackParams = () => {
        switch (attackType) {
            case 'ddos':
                return (
                    <>
                        <div><Label htmlFor="num_requests">Number of Requests</Label><Input id="num_requests" type="number" placeholder="1000" onChange={(e) => handleNumericParamChange('num_requests', e.target.value)} /></div>
                        <div><Label htmlFor="concurrency">Concurrency</Label><Input id="concurrency" type="number" placeholder="50" onChange={(e) => handleNumericParamChange('concurrency', e.target.value)} /></div>
                    </>
                );
            case 'brute_force':
                return (
                    <>
                        <div><Label htmlFor="usernames">Usernames (comma-separated)</Label><Input id="usernames" placeholder="admin,user,root" onChange={(e) => handleParamChange('usernames', e.target.value.split(',').map(p => p.trim()))} /></div>
                        <div><Label htmlFor="passwords">Passwords (comma-separated)</Label><Input id="passwords" placeholder="password,123456" onChange={(e) => handleParamChange('passwords', e.target.value.split(',').map(p => p.trim()))} /></div>
                    </>
                );
            case 'sql_injection':
                return (
                    <>
                        <div><Label htmlFor="param_to_inject">Parameter to Inject</Label><Input id="param_to_inject" placeholder="e.g., id, username" onChange={(e) => handleParamChange('param_to_inject', e.target.value)} /></div>
                    </>
                );
            case 'syn_flood':
                return (
                    <>
                        <div><Label htmlFor="target_port">Target Port</Label><Input id="target_port" type="number" placeholder="80" onChange={(e) => handleNumericParamChange('target_port', e.target.value)} /></div>
                        <div><Label htmlFor="num_packets">Number of Packets</Label><Input id="num_packets" type="number" placeholder="1000" onChange={(e) => handleNumericParamChange('num_packets', e.target.value)} /></div>
                    </>
                );
            default:
                return <p className="text-gray-400 text-sm col-span-2">Select an attack type to see its parameters.</p>;
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
                        <div className="space-y-2">
                            <Label htmlFor="attack-type">Attack Type</Label>
                            <Select onValueChange={(value: any) => { setAttackType(value); setParams({}); }}>
                                <SelectTrigger><SelectValue placeholder="Select attack type" /></SelectTrigger>
                                <SelectContent>
                                    {attackTypes.map((attack) => <SelectItem key={attack.value} value={attack.value}>{attack.label}</SelectItem>)}
                                </SelectContent>
                            </Select>
                        </div>
                        <div className="space-y-2">
                            <Label htmlFor="target">
                                {attackType === 'syn_flood' ? 'Target IP Address' : 'Target URL'}
                            </Label>
                            <Input 
                                id="target" 
                                value={target} 
                                onChange={(e) => setTarget(e.target.value)} 
                                placeholder={attackType === 'syn_flood' ? 'e.g., 192.168.1.100' : 'http://example.com/login'} 
                            />
                        </div>
                    </div>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        {renderAttackParams()}
                    </div>
                    <Button onClick={handleStartSimulation} disabled={isSubmitting || !!activeSimulationId || !attackType}>
                        {activeSimulationId ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : <Play className="w-4 h-4 mr-2" />}
                        {activeSimulationId ? 'Simulation Running...' : 'Launch Simulation'}
                    </Button>
                    {activeSimulationId && (
                        <div className="space-y-2 mt-4">
                            <div className="flex justify-between text-sm">
                                <span className="text-gray-300 font-mono">{statusMessage || "Initializing..."}</span>
                                <span className="text-cyber-primary">{Math.round(progress)}%</span>
                            </div>
                            <Progress value={progress} className="h-2" />
                        </div>
                    )}
                </CardContent>
            </Card>
            <Card className="glass-morphism border-cyber-light/30">
                <CardHeader>
                    <CardTitle>Recent Simulations</CardTitle>
                    <CardDescription>History of completed and running simulations</CardDescription>
                </CardHeader>
                <CardContent>
                    {isLoadingLogs ? (
                        <div className="flex justify-center items-center h-20"><Loader2 className="w-6 h-6 animate-spin"/></div>
                    ) : (
                        <div className="space-y-3">
                            {(recentSimulations?.data.data.length === 0) ? <p className="text-gray-400">No simulations found.</p> : recentSimulations?.data.data.map((sim: SimulationLog) => (
                                <div key={sim.simulation_id} className="flex items-center justify-between p-3 bg-cyber-darker/50 rounded-lg">
                                    <div className="flex items-center space-x-3">
                                        {sim.status === 'running' && <Loader2 className="w-4 h-4 text-cyber-primary animate-spin" />}
                                        {sim.status === 'completed' && <TargetIcon className="w-4 h-4 text-cyber-primary" />}
                                        {sim.status === 'failed' && <TargetIcon className="w-4 h-4 text-cyber-accent" />}
                                        <div>
                                            <div className="font-medium text-gray-300">{sim.simulation_type.toUpperCase().replace('_', ' ')}</div>
                                            <div className="text-sm text-gray-400 max-w-xs truncate" title={sim.target_details?.url || sim.summary?.target_ip || 'N/A'}>
                                                Target: {sim.target_details?.url || sim.summary?.target_ip || 'N/A'}
                                            </div>
                                        </div>
                                    </div>
                                    <div className="flex items-center space-x-4">
                                        <Badge variant={sim.status === 'completed' ? 'default' : sim.status === 'failed' ? 'destructive' : 'secondary'}>
                                            {sim.status}
                                        </Badge>
                                        <span className="text-sm text-gray-400 hidden md:inline">{new Date(sim.start_time).toLocaleTimeString()}</span>
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