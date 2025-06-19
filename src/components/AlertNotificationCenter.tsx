// in: attack-intel-platform/src/components/AlertNotificationCenter.tsx

import React from 'react';
import { Link } from 'react-router-dom'; // --- HATA 1: Bu import eksikti ---
import { useQuery } from '@tanstack/react-query';

// UI Bileşenleri
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';
import { Button } from '@/components/ui/button';
import { AlertTriangle, Bell, Loader2, ChevronsRight } from 'lucide-react'; // --- HATA 2: ChevronsRight eksikti, Ban kaldırıldı ---

// Servisler ve Tipler
import { getPredictionLogs } from '@/services/reportService';
import { PredictionLog } from '@/types/apiTypes'; // Tipin kendisini import etmek daha temiz

const AlertNotificationCenter = () => {
  // queryKey'i bir dizi olarak tanımlamak best practice'dir.
  const { data: alertsResponse, isLoading, isError } = useQuery<{ data: { data: PredictionLog[] } }>({
    queryKey: ['predictionLogs'],
    queryFn: () => getPredictionLogs({ limit: 10 }),
    refetchInterval: 5000
  });

  const alerts = alertsResponse?.data.data || [];

  // --- HATA 3: blockIpMutation ve extractIpFromSource fonksiyonları artık burada gerekli değil ---
  // Bu mantık ResponseCenter.tsx'e taşındığı için buradan kaldırıldı.

  const severityMap: { [key: string]: { label: string; color: string } } = {
    'DoS/DDoS': { label: 'Critical', color: 'bg-cyber-accent' },
    'SYN Flood': { label: 'Critical', color: 'bg-cyber-accent' }, // SYN Flood için eklendi
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

      return (
        <Alert key={alert._id} className="border-cyber-light/30 bg-cyber-darker/50 flex flex-col space-y-2">
          {/* Üst Kısım: Uyarı Başlığı ve Ciddiyet */}
          <div className="flex items-center space-x-3">
            <AlertTriangle className="h-4 w-4 text-cyber-accent" />
            <AlertTitle className="flex-grow font-medium text-gray-200">
              {alert.prediction_result.prediction_label}
            </AlertTitle>
            <Badge className={`${severity.color} text-white`}>{severity.label}</Badge>
          </div>
          
          {/* Orta Kısım: Detaylar */}
          <AlertDescription className="text-gray-300 pl-7">
            Source: {alert.source_of_data}
          </AlertDescription>
          <div className="text-sm text-gray-400 pl-7">
            Detected at: {new Date(alert.created_at).toLocaleString()}
          </div>
          
          {/* --- HATA 4: Bu bölüm tamamen yeniden düzenlendi --- */}
          {/* Alt Kısım: Aksiyon Butonu */}
          <div className="pl-7 pt-2 flex justify-end">
             {/* asChild prop'u Button'un bir Link gibi davranmasını sağlar */}
             <Button asChild variant="secondary" size="sm">
               <Link to={`/response/${alert._id}`}>
                 Triage & Respond
                 <ChevronsRight className="w-4 h-4 ml-2" />
               </Link>
             </Button>
          </div>
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