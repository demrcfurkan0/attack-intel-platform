import { useQuery } from '@tanstack/react-query';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from 'recharts';
import { Shield, Loader2 } from 'lucide-react';
import { getDetectionMetrics } from '@/services/statisticsService';

const DetectionMetricsChart = () => {
  const { data, isLoading, isError } = useQuery({
    queryKey: ['detectionMetrics'],
    queryFn: getDetectionMetrics,
    refetchInterval: 30000,
    staleTime: 15000,
  });

  const pieData = [
    { name: 'Detected Attacks', value: data?.data.detected_attacks || 0, color: '#ff4444' },
    { name: 'Analyzed Benign', value: data?.data.benign_traffic || 0, color: '#00ff88' },
  ];

  return (
    <Card className="glass-morphism border-cyber-light/30 chart-container">
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <Shield className="w-5 h-5 text-cyber-primary" />
          <span>Detection Performance Metrics</span>
        </CardTitle>
        <CardDescription>Breakdown of AI model's predictions</CardDescription>
      </CardHeader>
      <CardContent>
        {isLoading ? (
          <div className="h-[250px] flex justify-center items-center">
            <Loader2 className="w-8 h-8 animate-spin text-cyber-primary" />
          </div>
        ) : isError ? (
          <div className="h-[250px] flex justify-center items-center text-red-500">
            Failed to load metrics.
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
            <ResponsiveContainer width="100%" height={250}>
              <PieChart>
                <Pie
                  data={pieData}
                  cx="50%"
                  cy="50%"
                  innerRadius={60}
                  outerRadius={80}
                  paddingAngle={5}
                  dataKey="value"
                  labelLine={false}
                >
                  {pieData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip
                  contentStyle={{
                    backgroundColor: 'rgba(10, 15, 28, 0.9)',
                    border: '1px solid rgba(0, 255, 136, 0.3)',
                  }}
                />
              </PieChart>
            </ResponsiveContainer>
            <div className="space-y-2">
              <h5 className="text-xs font-medium text-gray-400 uppercase tracking-wide">Prediction Totals</h5>
              {pieData.map((item) => (
                <div key={item.name} className="flex items-center justify-between text-sm">
                  <div className="flex items-center space-x-2">
                    <div className="w-3 h-3 rounded-full" style={{ backgroundColor: item.color }}></div>
                    <span className="text-gray-300">{item.name}</span>
                  </div>
                  <span className="font-mono text-gray-400">{item.value.toLocaleString()}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </CardContent>
    </Card>
  );
};

export default DetectionMetricsChart;