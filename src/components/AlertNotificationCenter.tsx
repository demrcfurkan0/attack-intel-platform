import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';
import { AlertTriangle, Bell, Loader2, Ban } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';
import { useQuery, useMutation } from '@tanstack/react-query';
import { getPredictionLogs } from '@/services/reportService';
import { blockIpAddress } from '@/services/responseService';
import { Button } from '@/components/ui/button';
import { AxiosResponse } from 'axios';
import { PaginatedPredictionsResponse } from '@/types/apiTypes';

const AlertNotificationCenter = () => {
  const { toast } = useToast();

  const { data: alertsResponse, isLoading, isError } = useQuery({
    queryKey: ['predictionLogs'],
    queryFn: () => getPredictionLogs({ limit: 10 }),
    refetchInterval: 5000
  });

  const alerts = alertsResponse?.data.data || [];

  // IP engelleme işlemi için useMutation hook'u
  const blockIpMutation = useMutation({
    mutationFn: blockIpAddress,
    onSuccess: (data: any) => {
        toast({
            title: "Action Successful",
            description: data.data.message,
        });
    },
    onError: (error: any) => {
        toast({
            variant: "destructive",
            title: "Action Failed",
            description: error.response?.data?.detail || "Could not block IP address.",
        });
    },
  });

  // Bu yardımcı fonksiyon, kaynak bilgisinden IP adresini ayıklamaya çalışır.
  // Gerçek uygulamada bu format daha standart olmalıdır.
  const extractIpFromSource = (sourceInfo: string): string | null => {
    // Basit bir regex ile IP adresi arayalım.
    const ipRegex = /(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/;
    const match = sourceInfo.match(ipRegex);
    return match ? match[0] : '127.0.0.1'; // Bulamazsa varsayılan döndür
  };

  const severityMap: { [key: string]: { label: string; color: string } } = {
    'DoS/DDoS': { label: 'Critical', color: 'bg-cyber-accent' },
    'SYN_FLOOD': { label: 'Critical', color: 'bg-cyber-accent' },
    'BruteForce': { label: 'High', color: 'bg-cyber-warning' },
    'SQL_Injection': { label: 'Critical', color: 'bg-cyber-accent' },
    default: { label: 'Medium', color: 'bg-cyber-secondary' },
  };

  const getSeverity = (predictionLabel: string) => {
    return severityMap[predictionLabel] || severityMap.default;
  };

  const renderContent = () => {
    if (isLoading) {
      return (
        <div className="flex justify-center items-center h-40">
          <Loader2 className="w-8 h-8 animate-spin text-cyber-primary" />
        </div>
      );
    }

    if (isError) {
      return <Alert variant="destructive">Could not load alerts.</Alert>;
    }

    if (alerts.length === 0) {
      return <p className="text-gray-400">No attacks detected yet. Run a simulation to see results.</p>;
    }

    return alerts.map((alert) => {
      const severity = getSeverity(alert.prediction_result.prediction_label);
      const sourceIp = extractIpFromSource(alert.source_of_data);

      return (
        <Alert key={alert._id} className="border-cyber-light/30 bg-cyber-darker/50 flex flex-col space-y-2">
          <div className="flex items-center space-x-3">
            <AlertTriangle className="h-4 w-4 text-cyber-accent" />
            <AlertTitle className="flex-grow font-medium text-gray-200">
              {alert.prediction_result.prediction_label}
            </AlertTitle>
            <Badge className={`${severity.color} text-white`}>{severity.label}</Badge>
          </div>
          <AlertDescription className="text-gray-300 pl-7">
            Source: {alert.source_of_data}
          </AlertDescription>
          <div className="text-sm text-gray-400 pl-7">
            Detected at: {new Date(alert.created_at).toLocaleString()}
          </div>
          {sourceIp && (
            <div className="pl-7 pt-2">
              <Button
                  variant="destructive"
                  size="sm"
                  onClick={() => blockIpMutation.mutate(sourceIp)}
                  disabled={blockIpMutation.isPending}
              >
                  {blockIpMutation.isPending ? <Loader2 className="w-4 h-4 animate-spin" /> : <Ban className="w-4 h-4 mr-2" />}
                  Block IP: {sourceIp}
              </Button>
            </div>
          )}
        </Alert>
      );
    });
  };

  return (
    <Card className="glass-morphism border-cyber-light/30">
      <CardHeader>
        <CardTitle className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <Bell className="w-5 h-5 text-cyber-primary" />
            <span>AI-Powered Security Alerts</span>
          </div>
          <Badge variant="outline" className="border-cyber-light/30">
            {alerts.length} recent detections
          </Badge>
        </CardTitle>
        <CardDescription>Real-time threat detections from the AI model</CardDescription>
      </CardHeader>
      <CardContent className="space-y-4">
        {renderContent()}
      </CardContent>
    </Card>
  );
};

export default AlertNotificationCenter;