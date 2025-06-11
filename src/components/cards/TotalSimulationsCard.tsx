import { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';
import { Activity } from 'lucide-react';
import { getAttackTrends } from '@/services/statisticsService';

export const TotalSimulationsCard = () => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getAttackTrends();
        const totalSims = Object.values(response.data).reduce((acc, hour) => {
          return acc + (hour.ddos || 0) + (hour.brute_force || 0) + (hour.sql_injection || 0);
        }, 0);
        setCount(totalSims);
      } catch (error) {
        console.error("Failed to fetch total simulations:", error);
      }
    };
    fetchData();
    const interval = setInterval(fetchData, 30000);
    return () => clearInterval(interval);
  }, []);

  return (
    <Card className="glass-morphism">
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">Total Simulations</CardTitle>
        <Activity className="h-4 w-4 text-cyber-warning" />
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold text-cyber-warning">{count.toLocaleString()}</div>
        <p className="text-xs text-gray-400">In the last 24 hours</p>
        <Progress value={count % 100} className="mt-2 h-2" />
      </CardContent>
    </Card>
  );
};