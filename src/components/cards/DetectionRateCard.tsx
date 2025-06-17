import { useQuery } from '@tanstack/react-query';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';
import { Shield, Loader2 } from 'lucide-react';
import { getDetectionMetrics } from '@/services/statisticsService';

export const DetectionRateCard = () => {
  const { data, isLoading, isError } = useQuery({
    queryKey: ['detectionMetrics'],
    queryFn: getDetectionMetrics,
    refetchInterval: 30000,
  });

  const metrics = data?.data;
  const total = metrics ? metrics.detected_attacks + metrics.benign_traffic : 0;
  const rate = total > 0 && metrics ? (metrics.detected_attacks / total) * 100 : 0;

  if (isError) {
    return (
      <Card className="glass-morphism">
        <CardHeader><CardTitle className="text-sm font-medium text-red-500">Error</CardTitle></CardHeader>
        <CardContent><p className="text-xs text-gray-400">Could not load data.</p></CardContent>
      </Card>
    );
  }

  return (
    <Card className="glass-morphism">
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">Detection Rate</CardTitle>
        <Shield className="h-4 w-4 text-cyber-primary" />
      </CardHeader>
      <CardContent>
        {isLoading ? (
          <Loader2 className="h-6 w-6 animate-spin text-cyber-primary" />
        ) : (
          <>
            <div className="text-2xl font-bold text-cyber-primary">{rate.toFixed(1)}%</div>
            <p className="text-xs text-gray-400">Of all AI predictions</p>
          </>
        )}
        <Progress value={rate} className="mt-2 h-2" />
      </CardContent>
    </Card>
  );
};