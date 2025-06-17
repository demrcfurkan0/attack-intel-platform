import { useQuery } from '@tanstack/react-query';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { Loader2 } from 'lucide-react';
import { getAttackTrends } from '@/services/statisticsService';

const AttackTrendsChart = () => {
  const { data, isLoading, isError } = useQuery({
    queryKey: ['attackTrends'],
    queryFn: getAttackTrends,
    refetchInterval: 30000,
    staleTime: 15000,
  });

  const formattedData = data?.data
    ? Object.entries(data.data).map(([time, values]) => ({
        time,
        ddos: values.ddos || 0,
        bruteforce: values.brute_force || 0,
        sqlinjection: values.sql_injection || 0,
      }))
    : [];

  return (
    <Card className="glass-morphism border-cyber-light/30 chart-container">
      <CardHeader>
        <CardTitle>Attack Trends - Last 24 Hours</CardTitle>
        <CardDescription>Hourly frequency of simulated attacks</CardDescription>
      </CardHeader>
      <CardContent className="h-[300px] flex justify-center items-center">
        {isLoading ? (
          <Loader2 className="w-8 h-8 animate-spin text-cyber-primary" />
        ) : isError ? (
           <p className="text-red-500">Failed to load attack trends.</p>
        ) : (
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={formattedData}>
              <defs>
                  <linearGradient id="ddosGradient" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#ff4444" stopOpacity={0.8}/>
                      <stop offset="95%" stopColor="#ff4444" stopOpacity={0}/>
                  </linearGradient>
                  <linearGradient id="bruteGradient" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#0088ff" stopOpacity={0.8}/>
                      <stop offset="95%" stopColor="#0088ff" stopOpacity={0}/>
                  </linearGradient>
                  <linearGradient id="sqlGradient" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#ffaa00" stopOpacity={0.8}/>
                      <stop offset="95%" stopColor="#ffaa00" stopOpacity={0}/>
                  </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(0, 255, 136, 0.1)" />
              <XAxis dataKey="time" stroke="#00ff88" fontSize={12} />
              <YAxis stroke="#00ff88" fontSize={12} />
              <Tooltip contentStyle={{ backgroundColor: 'rgba(10, 15, 28, 0.9)', border: '1px solid rgba(0, 255, 136, 0.3)' }}/>
              <Area type="monotone" dataKey="ddos" stackId="1" stroke="#ff4444" fill="url(#ddosGradient)" />
              <Area type="monotone" dataKey="bruteforce" stackId="1" stroke="#0088ff" fill="url(#bruteGradient)" />
              <Area type="monotone" dataKey="sqlinjection" stackId="1" stroke="#ffaa00" fill="url(#sqlGradient)" />
            </AreaChart>
          </ResponsiveContainer>
        )}
      </CardContent>
    </Card>
  );
};
export default AttackTrendsChart;