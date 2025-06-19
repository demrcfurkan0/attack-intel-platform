// in: attack-intel-platform/src/components/ResponseCenter.tsx

import React from 'react';
import { useParams } from 'react-router-dom';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Loader2, AlertCircle, ShieldCheck, History, CornerUpRight, CheckCircle, Clock } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';

// Servisler ve Tipler
import { getPredictionLogById, updatePredictionStatus } from '@/services/reportService';
import { blockIpAddress, getIncidentHistory, executeAction } from '@/services/responseService';
import { PredictionLog, ResponseHistory } from '@/types/apiTypes';

// Aksiyon butonu tipi
type ActionItem = {
    label: string;
    action: () => void;
    loading?: boolean;
    variant?: "default" | "destructive" | "outline" | "secondary" | "ghost" | "link";
    icon: React.ElementType;
};

// Yardımcı fonksiyon: Kaynak bilgisinden IP'yi ayıklar
const extractIpFromSource = (sourceInfo: string): string | null => {
    const ipRegex = /(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/;
    const match = sourceInfo.match(ipRegex);
    return match ? match[0] : null;
};


const ResponseCenter = () => {
    const { predictionId } = useParams<{ predictionId: string }>();
    const queryClient = useQueryClient();
    const { toast } = useToast();

    // Hata ayıklama için konsol logu
    console.log("Current Prediction ID from URL:", predictionId);

    // 1. Belirli bir uyarıyı çekmek için useQuery
    const { data: alert, isLoading: isLoadingAlert, isError: isErrorAlert } = useQuery({
        queryKey: ['predictionLog', predictionId],
        queryFn: async () => {
            console.log(`Fetching prediction log for ID: ${predictionId}`);
            const response = await getPredictionLogById(predictionId!);
            console.log("Fetched alert data:", response.data);
            return response.data;
        },
        enabled: !!predictionId, // Sadece predictionId varsa bu query'i çalıştır
    });

    // 2. Bu olaya özel aksiyon geçmişini çekmek için useQuery
    const { data: incidentHistory, isLoading: isLoadingHistory } = useQuery({
        queryKey: ['incidentHistory', predictionId],
        queryFn: async () => {
            console.log(`Fetching history for ID: ${predictionId}`);
            const response = await getIncidentHistory(predictionId!);
            console.log("Fetched history data:", response.data);
            return response.data;
        },
        enabled: !!predictionId,
    });
    
    // --- MUTASYONLAR ---

    const logActionMutation = useMutation({
        mutationFn: (actionTitle: string) => executeAction({ action_title: actionTitle, target_prediction_id: predictionId! }),
        onSuccess: () => {
            toast({ title: "Action Logged", description: "The action has been recorded in the incident history." });
            queryClient.invalidateQueries({ queryKey: ['incidentHistory', predictionId] });
        },
        onError: (error: any) => {
            toast({ variant: "destructive", title: "Logging Failed", description: error.response?.data?.detail || "Could not log the action." });
        }
    });

    const blockIpMutation = useMutation({
        mutationFn: (ip: string) => Promise.all([
            blockIpAddress(ip),
            logActionMutation.mutateAsync(`Blocked IP: ${ip}`)
        ]),
        onSuccess: ([blockData]) => {
            toast({ title: "Action Successful", description: (blockData as any).data.message });
            // Bu zaten logActionMutation'ın onSuccess'i tarafından tetiklenir, tekrar gerek yok.
        },
        onError: (error: any) => {
            toast({ variant: "destructive", title: "Action Failed", description: error.response?.data?.detail || "Could not block IP." });
        }
    });

    const updateStatusMutation = useMutation({
        mutationFn: (status: string) => Promise.all([
            updatePredictionStatus(predictionId!, status),
            logActionMutation.mutateAsync(`Status changed to: ${status}`)
        ]),
        onSuccess: ([statusUpdateData]) => {
            toast({ title: "Status Updated", description: (statusUpdateData as any).data.message });
            queryClient.invalidateQueries({ queryKey: ['predictionLog', predictionId] });
        },
        onError: (error: any) => {
            toast({ variant: "destructive", title: "Status Update Failed", description: error.response?.data?.detail });
        }
    });


    // --- AKSİYON HANDLER'LARI ---
    
    const handleBlockIp = () => {
        if (alert) {
            const ip = extractIpFromSource(alert.source_of_data);
            if (ip) {
                blockIpMutation.mutate(ip);
            } else {
                toast({ variant: "destructive", title: "Cannot Block", description: "No valid IP address found in source." });
            }
        }
    };

    // --- RENDER MANTIĞI ---

    if (!predictionId) {
        return (
            <Card className="glass-morphism h-96 flex flex-col items-center justify-center">
                <CardHeader><CardTitle>Incident Response Center</CardTitle></CardHeader>
                <CardContent className="text-center">
                    <ShieldCheck className="w-16 h-16 mx-auto text-cyber-primary mb-4" />
                    <p className="text-gray-400">Select an alert from the "Alerts" tab to begin analysis and response.</p>
                </CardContent>
            </Card>
        );
    }
    
    if (isLoadingAlert) return <div className="flex justify-center items-center h-96"><Loader2 className="w-12 h-12 animate-spin text-cyber-primary" /></div>;
    
    if (isErrorAlert || !alert) {
        return <div className="text-cyber-accent text-center p-10"><AlertCircle className="w-12 h-12 mx-auto mb-4" />Failed to load incident details for ID: {predictionId}. Please check if the backend is running and the ID is correct.</div>;
    }

    const getRecommendedActions = (alert: PredictionLog): ActionItem[] => {
        const actions: ActionItem[] = [];
        const alertStatus = alert.status || 'new';

        if (alertStatus !== 'triaged' && alertStatus !== 'resolved') {
            actions.push({ label: `Acknowledge & Triage`, icon: CornerUpRight, action: () => updateStatusMutation.mutate('triaged'), loading: updateStatusMutation.isPending });
        }

        if (alertStatus !== 'resolved') {
            const attackType = alert.prediction_result.prediction_label;
            if ((attackType === 'DoS/DDoS' || attackType === 'BruteForce') && extractIpFromSource(alert.source_of_data)) {
                actions.push({ label: `Block Source IP`, icon: ShieldCheck, variant: "destructive", action: handleBlockIp, loading: blockIpMutation.isPending });
            }
            if (attackType === 'SQL_Injection') {
                actions.push({ label: `Isolate Web Application (Simulated)`, icon: ShieldCheck, variant: "destructive", action: () => logActionMutation.mutate('Simulated web application isolation'), loading: logActionMutation.isPending });
            }
            actions.push({ label: `Mark as Resolved`, icon: CheckCircle, action: () => updateStatusMutation.mutate('resolved'), loading: updateStatusMutation.isPending });
        }
        
        return actions;
    };
    
    const recommendedActions = getRecommendedActions(alert);
    const alertStatus = alert.status || 'new';

    return (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {/* SOL SÜTUN: OLAY DETAYLARI */}
            <div className="lg:col-span-2 space-y-6">
                <Card className="glass-morphism">
                    <CardHeader>
                        <div className="flex justify-between items-start">
                            <div>
                                <CardTitle>Incident Details: {alert.prediction_result.prediction_label}</CardTitle>
                                <CardDescription>ID: {alert._id}</CardDescription>
                            </div>
                            <Badge variant={alertStatus === 'resolved' ? 'default' : alertStatus === 'triaged' ? 'secondary' : 'destructive'} className="capitalize">
                                {alertStatus}
                            </Badge>
                        </div>
                    </CardHeader>
                    <CardContent className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                        <div><strong>Source:</strong> <span className="font-mono text-cyber-warning break-all">{alert.source_of_data}</span></div>
                        <div><strong>Detected At:</strong> <span className="font-mono">{new Date(alert.created_at).toLocaleString()}</span></div>
                        <div><strong>Model Confidence:</strong> <span className="font-mono text-cyber-primary">{alert.prediction_result.probabilities ? `${(Math.max(...alert.prediction_result.probabilities) * 100).toFixed(2)}%` : 'N/A'}</span></div>
                        <div><strong>Simulation ID:</strong> <span className="font-mono">{alert.simulation_id || 'N/A'}</span></div>
                    </CardContent>
                </Card>

                {/* Aksiyon Geçmişi Kartı */}
                <Card className="glass-morphism">
                    <CardHeader><CardTitle className="flex items-center"><History className="w-5 h-5 mr-2" />Action History for this Incident</CardTitle></CardHeader>
                    <CardContent>
                        {isLoadingHistory ? <Loader2 className="animate-spin" /> :
                         !incidentHistory || incidentHistory.length === 0 ? <p className="text-gray-400">No actions taken for this incident yet.</p> :
                         <div className="space-y-3">
                             {incidentHistory.map((h: ResponseHistory) => (
                                 <div key={h.id} className="flex items-start space-x-3 text-sm">
                                     <Clock className="w-4 h-4 mt-0.5 text-gray-500"/>
                                     <div>
                                         <p className="text-gray-200">{h.action_title}</p>
                                         <p className="text-xs text-gray-400">by {h.executed_by} at {new Date(h.timestamp).toLocaleString()}</p>
                                     </div>
                                 </div>
                             ))}
                         </div>
                        }
                    </CardContent>
                </Card>
            </div>

            {/* SAĞ SÜTUN: ÖNERİLEN AKSİYONLAR */}
            <Card className="glass-morphism">
                <CardHeader>
                    <CardTitle>Recommended Actions</CardTitle>
                </CardHeader>
                <CardContent className="space-y-3">
                    {recommendedActions.map((item, index) => (
                        <Button key={index} className="w-full justify-start" variant={item.variant || "outline"} onClick={item.action} disabled={item.loading}>
                            {item.loading ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : <item.icon className="w-4 h-4 mr-2" />}
                            {item.label}
                        </Button>
                    ))}
                    {recommendedActions.length === 0 && (
                        <p className="text-sm text-gray-400">No further actions recommended. This incident is resolved.</p>
                    )}
                </CardContent>
            </Card>
        </div>
    );
};

export default ResponseCenter;