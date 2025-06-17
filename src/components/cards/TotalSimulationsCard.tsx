import { useQuery } from '@tanstack/react-query';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';
import { Activity, Loader2 } from 'lucide-react';
import { getAttackTrends } from '@/services/statisticsService';

export const TotalSimulationsCard = () => {
  const { data, isLoading, isError } = useQuery({
    queryKey: ['attackTrends'],
    queryFn: getAttackTrends,
    refetchInterval: 30000,
  });

  const count = data?.data
    ? Object.values(data.data).reduce((acc, hour) => {
        const hourlyTotal = (hour.ddos || 0) + (hour.brute_force || 0) + (hour.sql_injection || 0);
        return acc + hourlyTotal;
      }, 0)
    : 0;
    
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
        <CardTitle className="text-sm font-medium">Total Simulations</CardTitle>
        <Activity className="h-4 w-4 text-cyber-warning" />
      </CardHeader>
      <CardContent>
        {isLoading ? (
          <Loader2 className="h-6 w-6 animate-spin text-cyber-warning" />
        ) : (
          <>
            <div className="text-2xl font-bold text-cyber-warning">{count.toLocaleString()}</div>
            <p className="text-xs text-gray-400">In the last 24 hours</p>
          </>
        )}
        <Progress value={count % 100} className="mt-2 h-2" />
      </CardContent>
    </Card>
  );
};