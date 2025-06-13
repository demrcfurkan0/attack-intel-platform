import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { AlertTriangle, Bell, Loader2 } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';
import { getPredictionLogs } from '@/services/reportService';
import { PredictionLog } from '@/types/apiTypes';

const AlertNotificationCenter = () => {
  const [alerts, setAlerts] = useState<PredictionLog[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const { toast } = useToast();
  const [lastShownAlertId, setLastShownAlertId] = useState<string | null>(null);

  const severityMap: { [key: string]: { label: string; color: string } } = {
    'DoS/DDoS': { label: 'Critical', color: 'bg-cyber-accent' },
    'BruteForce': { label: 'High', color: 'bg-cyber-warning' },
    'SQL_Injection': { label: 'Critical', color: 'bg-cyber-accent' },
    default: { label: 'Medium', color: 'bg-cyber-secondary' },
  };

  const getSeverity = (predictionLabel: string) => {
    return severityMap[predictionLabel] || severityMap.default;
  };

  useEffect(() => {
    const fetchAlerts = async () => {
      if (alerts.length === 0) setIsLoading(true);
      setError(null);

      try {
        const response = await getPredictionLogs({ limit: 10 });
        const newAlerts = response.data.data;

        setAlerts(newAlerts);

        if (newAlerts.length > 0) {
          const latestAlert = newAlerts[0];
          if (latestAlert._id !== lastShownAlertId) {
            toast({
              title: `🚨 ATTACK DETECTED: ${latestAlert.prediction_result.prediction_label}`,
              description: `Source: ${latestAlert.source_of_data}`,
              variant: 'destructive',
            });
            setLastShownAlertId(latestAlert._id);
          }
        }
      } catch (err) {
        setError('Could not load alerts.');
        console.error(err);
      } finally {
        setIsLoading(false);
      }
    };

    fetchAlerts();
    const intervalId = setInterval(fetchAlerts, 5000);
    return () => clearInterval(intervalId);
  }, [lastShownAlertId, toast]);

  if (isLoading) {
    return (
      <div className="flex justify-center items-center h-40">
        <Loader2 className="w-8 h-8 animate-spin text-cyber-primary" />
      </div>
    );
  }

  if (error) {
    return <Alert variant="destructive">{error}</Alert>;
  }

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
        {alerts.length === 0 ? (
          <p className="text-gray-400">No attacks detected yet. Run a simulation to see results.</p>
        ) : (
          alerts.map((alert) => {
            const severity = getSeverity(alert.prediction_result.prediction_label);
            return (
              <Alert key={alert._id} className="border-cyber-light/30 bg-cyber-darker/50">
                <AlertTriangle className="h-4 w-4 text-cyber-accent" />
                <div className="flex items-start justify-between w-full">
                  <div className="space-y-1">
                    <div className="flex items-center space-x-3">
                      <h4 className="font-medium text-gray-200">{alert.prediction_result.prediction_label}</h4>
                      <Badge className={`${severity.color} text-white`}>{severity.label}</Badge>
                    </div>
                    <AlertDescription className="text-gray-300">
                      Source: {alert.source_of_data}
                    </AlertDescription>
                    <div className="text-sm text-gray-400">
                      Detected at: {new Date(alert.created_at).toLocaleString()}
                    </div>
                  </div>
                </div>
              </Alert>
            );
          })
        )}
      </CardContent>
    </Card>
  );
};

export default AlertNotificationCenter;