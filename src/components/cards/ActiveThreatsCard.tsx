import { useQuery } from '@tanstack/react-query';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';
import { AlertTriangle, Loader2 } from 'lucide-react';
import { getDetectionMetrics } from '@/services/statisticsService';

export const ActiveThreatsCard = () => {
  const { data, isLoading, isError } = useQuery({
    queryKey: ['detectionMetrics'],
    queryFn: getDetectionMetrics,
    refetchInterval: 30000,
  });

  const count = data?.data.detected_attacks || 0;

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
        <CardTitle className="text-sm font-medium">Detected Attacks</CardTitle>
        <AlertTriangle className="h-4 w-4 text-cyber-accent" />
      </CardHeader>
      <CardContent>
        {isLoading ? (
          <Loader2 className="h-6 w-6 animate-spin text-cyber-accent" />
        ) : (
          <>
            <div className="text-2xl font-bold text-cyber-accent">{count.toLocaleString()}</div>
            <p className="text-xs text-gray-400">Total predictions marked as attack</p>
          </>
        )}
        <Progress value={count % 100} className="mt-2 h-2" />
      </CardContent>
    </Card>
  );
};