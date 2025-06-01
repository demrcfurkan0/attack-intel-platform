
import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Area, AreaChart } from 'recharts';
import { TrendingUp } from 'lucide-react';

const data = [
  { time: '00:00', ddos: 4, sqlinjection: 2, bruteforce: 1, malware: 0 },
  { time: '04:00', ddos: 3, sqlinjection: 1, bruteforce: 2, malware: 1 },
  { time: '08:00', ddos: 7, sqlinjection: 4, bruteforce: 3, malware: 2 },
  { time: '12:00', ddos: 12, sqlinjection: 8, bruteforce: 5, malware: 3 },
  { time: '16:00', ddos: 9, sqlinjection: 6, bruteforce: 4, malware: 2 },
  { time: '20:00', ddos: 15, sqlinjection: 12, bruteforce: 8, malware: 5 },
  { time: '24:00', ddos: 6, sqlinjection: 3, bruteforce: 2, malware: 1 },
];

const AttackTrendsChart = () => {
  return (
    <Card className="glass-morphism border-cyber-light/30 chart-container">
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <TrendingUp className="w-5 h-5 text-cyber-primary" />
          <span>Attack Trends - Last 24 Hours</span>
        </CardTitle>
        <CardDescription>Real-time monitoring of attack patterns and frequencies</CardDescription>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <AreaChart data={data}>
            <defs>
              <linearGradient id="ddosGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#ff4444" stopOpacity={0.8}/>
                <stop offset="95%" stopColor="#ff4444" stopOpacity={0}/>
              </linearGradient>
              <linearGradient id="sqlGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#ffaa00" stopOpacity={0.8}/>
                <stop offset="95%" stopColor="#ffaa00" stopOpacity={0}/>
              </linearGradient>
              <linearGradient id="bruteGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#0088ff" stopOpacity={0.8}/>
                <stop offset="95%" stopColor="#0088ff" stopOpacity={0}/>
              </linearGradient>
              <linearGradient id="malwareGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#00ff88" stopOpacity={0.8}/>
                <stop offset="95%" stopColor="#00ff88" stopOpacity={0}/>
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" stroke="rgba(0, 255, 136, 0.1)" />
            <XAxis 
              dataKey="time" 
              stroke="#00ff88" 
              fontSize={12}
              tickLine={false}
              axisLine={false}
            />
            <YAxis 
              stroke="#00ff88" 
              fontSize={12}
              tickLine={false}
              axisLine={false}
            />
            <Tooltip 
              contentStyle={{
                backgroundColor: 'rgba(10, 15, 28, 0.9)',
                border: '1px solid rgba(0, 255, 136, 0.3)',
                borderRadius: '8px',
                color: '#00ff88'
              }}
            />
            <Area
              type="monotone"
              dataKey="ddos"
              stackId="1"
              stroke="#ff4444"
              fill="url(#ddosGradient)"
              strokeWidth={2}
            />
            <Area
              type="monotone"
              dataKey="sqlinjection"
              stackId="1"
              stroke="#ffaa00"
              fill="url(#sqlGradient)"
              strokeWidth={2}
            />
            <Area
              type="monotone"
              dataKey="bruteforce"
              stackId="1"
              stroke="#0088ff"
              fill="url(#bruteGradient)"
              strokeWidth={2}
            />
            <Area
              type="monotone"
              dataKey="malware"
              stackId="1"
              stroke="#00ff88"
              fill="url(#malwareGradient)"
              strokeWidth={2}
            />
          </AreaChart>
        </ResponsiveContainer>
        <div className="flex justify-center space-x-6 mt-4">
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 bg-cyber-accent rounded-full"></div>
            <span className="text-sm text-gray-400">DDoS</span>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 bg-cyber-warning rounded-full"></div>
            <span className="text-sm text-gray-400">SQL Injection</span>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 bg-cyber-secondary rounded-full"></div>
            <span className="text-sm text-gray-400">Brute Force</span>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 bg-cyber-primary rounded-full"></div>
            <span className="text-sm text-gray-400">Malware</span>
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default AttackTrendsChart;
