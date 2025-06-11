import { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';
import { Shield } from 'lucide-react';
import { getDetectionMetrics } from '@/services/statisticsService';

export const DetectionRateCard = () => {
  const [rate, setRate] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getDetectionMetrics();
        const { detected_attacks, benign_traffic } = response.data;
        const total = detected_attacks + benign_traffic;
        const calculatedRate = total > 0 ? (detected_attacks / total) * 100 : 0;
        setRate(calculatedRate);
      } catch (error) {
        console.error("Failed to fetch detection rate:", error);
      }
    };
    fetchData();
    const interval = setInterval(fetchData, 30000);
    return () => clearInterval(interval);
  }, []);

  return (
    <Card className="glass-morphism">
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">Detection Rate</CardTitle>
        <Shield className="h-4 w-4 text-cyber-primary" />
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold text-cyber-primary">{rate.toFixed(1)}%</div>
        <p className="text-xs text-gray-400">Of all AI predictions</p>
        <Progress value={rate} className="mt-2 h-2" />
      </CardContent>
    </Card>
  );
};