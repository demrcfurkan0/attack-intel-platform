import { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';
import { AlertTriangle } from 'lucide-react';
import { getDetectionMetrics } from '@/services/statisticsService';

export const ActiveThreatsCard = () => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getDetectionMetrics();
        setCount(response.data.detected_attacks || 0);
      } catch (error) {
        console.error("Failed to fetch active threats:", error);
      }
    };
    fetchData();
    const interval = setInterval(fetchData, 30000);
    return () => clearInterval(interval);
  }, []);

  return (
    <Card className="glass-morphism">
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">Detected Attacks</CardTitle>
        <AlertTriangle className="h-4 w-4 text-cyber-accent" />
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold text-cyber-accent">{count.toLocaleString()}</div>
        <p className="text-xs text-gray-400">Total predictions marked as attack</p>
        <Progress value={count % 100} className="mt-2 h-2" />
      </CardContent>
    </Card>
  );
};