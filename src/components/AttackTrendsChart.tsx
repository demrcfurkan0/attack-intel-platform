import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { TrendingUp, Loader2 } from 'lucide-react';
import { getAttackTrends } from '@/services/statisticsService';

const AttackTrendsChart = () => {
  const [data, setData] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getAttackTrends();
        const formattedData = Object.entries(response.data).map(([time, values]) => ({
          time,
          ddos: values.ddos || 0,
          bruteforce: values.brute_force || 0,
          sqlinjection: values.sql_injection || 0,
        }));
        setData(formattedData);
      } catch (error) {
        console.error("Failed to fetch attack trends:", error);
      } finally {
        setIsLoading(false);
      }
    };
    fetchData();
  }, []);

  return (
    <Card className="glass-morphism border-cyber-light/30 chart-container">
      <CardHeader>
        <CardTitle>Attack Trends - Last 24 Hours</CardTitle>
        <CardDescription>Hourly frequency of simulated attacks</CardDescription>
      </CardHeader>
      <CardContent>
        {isLoading ? <Loader2 className="animate-spin" /> :
        <ResponsiveContainer width="100%" height={300}>
          <AreaChart data={data}>
            {/* ... <defs> ve gradientler aynı kalabilir ... */}
            <CartesianGrid strokeDasharray="3 3" stroke="rgba(0, 255, 136, 0.1)" />
            <XAxis dataKey="time" stroke="#00ff88" fontSize={12} />
            <YAxis stroke="#00ff88" fontSize={12} />
            <Tooltip contentStyle={{ backgroundColor: 'rgba(10, 15, 28, 0.9)', border: '1px solid rgba(0, 255, 136, 0.3)' }}/>
            <Area type="monotone" dataKey="ddos" stackId="1" stroke="#ff4444" fill="url(#ddosGradient)" />
            <Area type="monotone" dataKey="bruteforce" stackId="1" stroke="#0088ff" fill="url(#bruteGradient)" />
            <Area type="monotone" dataKey="sqlinjection" stackId="1" stroke="#ffaa00" fill="url(#sqlGradient)" />
          </AreaChart>
        </ResponsiveContainer>
        }
      </CardContent>
    </Card>
  );
};
export default AttackTrendsChart;