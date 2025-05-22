
import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, BarChart, Bar, XAxis, YAxis, CartesianGrid } from 'recharts';
import { Shield } from 'lucide-react';

const detectionData = [
  { name: 'True Positives', value: 847, color: '#00ff88' },
  { name: 'False Positives', value: 53, color: '#ffaa00' },
  { name: 'False Negatives', value: 12, color: '#ff4444' },
  { name: 'True Negatives', value: 2034, color: '#0088ff' },
];

const accuracyData = [
  { period: 'Last Hour', accuracy: 94.7, precision: 94.1, recall: 98.6 },
  { period: '6 Hours', accuracy: 93.2, precision: 92.8, recall: 97.3 },
  { period: '24 Hours', accuracy: 92.8, precision: 91.5, recall: 96.8 },
  { period: '7 Days', accuracy: 91.3, precision: 90.2, recall: 95.4 },
];

const DetectionMetricsChart = () => {
  return (
    <Card className="glass-morphism border-cyber-light/30 chart-container">
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <Shield className="w-5 h-5 text-cyber-primary" />
          <span>Detection Performance Metrics</span>
        </CardTitle>
        <CardDescription>Model accuracy, precision, and recall statistics</CardDescription>
      </CardHeader>
      <CardContent className="space-y-6">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Detection Results Pie Chart */}
          <div>
            <h4 className="text-sm font-medium text-gray-300 mb-4">Detection Results Distribution</h4>
            <ResponsiveContainer width="100%" height={200}>
              <PieChart>
                <Pie
                  data={detectionData}
                  cx="50%"
                  cy="50%"
                  innerRadius={40}
                  outerRadius={80}
                  paddingAngle={2}
                  dataKey="value"
                >
                  {detectionData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip 
                  contentStyle={{
                    backgroundColor: 'rgba(10, 15, 28, 0.9)',
                    border: '1px solid rgba(0, 255, 136, 0.3)',
                    borderRadius: '8px',
                    color: '#00ff88'
                  }}
                />
              </PieChart>
            </ResponsiveContainer>
          </div>

          {/* Accuracy Metrics */}
          <div>
            <h4 className="text-sm font-medium text-gray-300 mb-4">Accuracy Trends</h4>
            <ResponsiveContainer width="100%" height={200}>
              <BarChart data={accuracyData}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(0, 255, 136, 0.1)" />
                <XAxis 
                  dataKey="period" 
                  stroke="#00ff88" 
                  fontSize={10}
                  tickLine={false}
                  axisLine={false}
                />
                <YAxis 
                  domain={[85, 100]}
                  stroke="#00ff88" 
                  fontSize={10}
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
                <Bar dataKey="accuracy" fill="#00ff88" radius={[2, 2, 0, 0]} />
                <Bar dataKey="precision" fill="#0088ff" radius={[2, 2, 0, 0]} />
                <Bar dataKey="recall" fill="#ffaa00" radius={[2, 2, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Legend */}
        <div className="grid grid-cols-2 gap-4">
          <div className="space-y-2">
            <h5 className="text-xs font-medium text-gray-400 uppercase tracking-wide">Detection Results</h5>
            <div className="space-y-1">
              {detectionData.map((item, index) => (
                <div key={index} className="flex items-center justify-between text-sm">
                  <div className="flex items-center space-x-2">
                    <div 
                      className="w-3 h-3 rounded-full" 
                      style={{ backgroundColor: item.color }}
                    ></div>
                    <span className="text-gray-300">{item.name}</span>
                  </div>
                  <span className="font-mono text-gray-400">{item.value}</span>
                </div>
              ))}
            </div>
          </div>
          <div className="space-y-2">
            <h5 className="text-xs font-medium text-gray-400 uppercase tracking-wide">Metrics Legend</h5>
            <div className="space-y-1">
              <div className="flex items-center space-x-2 text-sm">
                <div className="w-3 h-3 bg-cyber-primary rounded-full"></div>
                <span className="text-gray-300">Accuracy</span>
              </div>
              <div className="flex items-center space-x-2 text-sm">
                <div className="w-3 h-3 bg-cyber-secondary rounded-full"></div>
                <span className="text-gray-300">Precision</span>
              </div>
              <div className="flex items-center space-x-2 text-sm">
                <div className="w-3 h-3 bg-cyber-warning rounded-full"></div>
                <span className="text-gray-300">Recall</span>
              </div>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default DetectionMetricsChart;
