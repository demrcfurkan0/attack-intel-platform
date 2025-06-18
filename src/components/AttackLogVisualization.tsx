import React, { useState, useMemo } from 'react';
import { useQuery } from '@tanstack/react-query';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import { Loader2, ChevronLeft, ChevronRight, AlertCircle } from 'lucide-react';

import { getSimulationLogs } from '../services/reportService';
import { SimulationLog } from '../types/apiTypes';

const LOGS_PER_PAGE = 10;

const AttackLogVisualization = () => {
  const [currentPage, setCurrentPage] = useState(1);

  const { data: response, isLoading, isError, error } = useQuery({
    queryKey: ['simulationLogs', currentPage],
    queryFn: () => getSimulationLogs({
      limit: LOGS_PER_PAGE,
      skip: (currentPage - 1) * LOGS_PER_PAGE,
    }),
    placeholderData: (previousData) => previousData,
  });
  
  const logs = response?.data.data || [];
  const totalLogs = response?.data.total_count || 0;
  const totalPages = Math.ceil(totalLogs / LOGS_PER_PAGE);

  const attackTimelineData = useMemo(() => {
    if (!logs.length) return [];
    return logs
      .slice()
      .sort((a, b) => new Date(a.start_time).getTime() - new Date(b.start_time).getTime())
      .map(log => ({
        time: new Date(log.start_time).toLocaleTimeString(),
        attacks: log.summary?.total_packets_sent || log.summary?.total_requests_attempted || 1,
        type: log.simulation_type.toUpperCase().replace('_', ' ')
      }));
  }, [logs]);

  return (
    <div className="space-y-6">
      <Card className="glass-morphism border-cyber-light/30">
          <CardHeader>
            <CardTitle>Attack Timeline</CardTitle>
            <CardDescription>Visual representation of simulation intensity over time.</CardDescription>
          </CardHeader>
          <CardContent className="h-[250px] flex items-center justify-center">
            {isLoading && logs.length === 0 ? <Loader2 className="w-8 h-8 animate-spin" /> : 
             logs.length === 0 ? <p className="text-gray-400">No data to display.</p> :
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={attackTimelineData}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(0, 255, 136, 0.1)" />
                <XAxis dataKey="time" stroke="#00ff88" fontSize={12} tick={{ fill: '#a0aec0' }} />
                <YAxis stroke="#00ff88" fontSize={12} tick={{ fill: '#a0aec0' }} />
                <Tooltip 
                  contentStyle={{ backgroundColor: 'rgba(10, 15, 28, 0.9)', border: '1px solid rgba(0, 255, 136, 0.3)', color: '#e2e8f0' }}
                  labelStyle={{ color: '#00ff88' }}
                />
                <Legend />
                <Line type="monotone" name="Intensity" dataKey="attacks" stroke="#ff4444" strokeWidth={2} dot={false} activeDot={{ r: 6 }}/>
              </LineChart>
            </ResponsiveContainer>
            }
          </CardContent>
      </Card>

      <Card className="glass-morphism border-cyber-light/30">
        <CardHeader>
          <CardTitle>Attack Log Details</CardTitle>
          <CardDescription>Detailed security event logs from all simulations</CardDescription>
        </CardHeader>
        <CardContent>
          {isLoading ? (
            <div className="flex justify-center items-center h-40">
              <Loader2 className="w-8 h-8 animate-spin text-cyber-primary" />
            </div>
          ) : isError ? (
            <div className="text-cyber-accent flex items-center space-x-2">
              <AlertCircle className="h-5 w-5" />
              <span>{`Failed to load attack logs: ${error instanceof Error ? error.message : 'Unknown error'}`}</span>
            </div>
          ) : (
            <>
              <div className="overflow-x-auto">
                <Table>
                  <TableHeader>
                    <TableRow className="border-cyber-light/20 hover:bg-transparent">
                      <TableHead>Type</TableHead>
                      <TableHead>Target</TableHead>
                      <TableHead>Status</TableHead>
                      <TableHead>Start Time</TableHead>
                      <TableHead>Duration (s)</TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {logs.map((log) => (
                      <TableRow key={log.simulation_id} className="border-cyber-light/10">
                        <TableCell>{log.simulation_type.toUpperCase().replace('_', ' ')}</TableCell>
                        <TableCell className="max-w-xs truncate" title={log.target_details?.ip || log.target_details?.url || 'N/A'}>
                            {log.target_details?.ip && log.target_details.ip !== 'N/A' 
                              ? log.target_details.ip 
                              : log.target_details?.url || 'N/A'}
                        </TableCell>
                        <TableCell><Badge variant={log.status === 'completed' ? 'default' : log.status === 'running' ? 'secondary' : 'destructive'}>{log.status}</Badge></TableCell>
                        <TableCell>{new Date(log.start_time).toLocaleString()}</TableCell>
                        <TableCell>{log.duration_seconds?.toFixed(3) || '-'}</TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </div>
              <div className="flex items-center justify-end space-x-2 py-4">
                <Button variant="outline" size="sm" onClick={() => setCurrentPage(p => Math.max(1, p - 1))} disabled={currentPage === 1}>
                  <ChevronLeft className="h-4 w-4 mr-1" /> Previous
                </Button>
                <span className="text-sm text-gray-400">Page {currentPage} of {totalPages}</span>
                <Button variant="outline" size="sm" onClick={() => setCurrentPage(p => Math.min(totalPages, p + 1))} disabled={currentPage >= totalPages}>
                  Next <ChevronRight className="h-4 w-4 ml-1" />
                </Button>
              </div>
            </>
          )}
        </CardContent>
      </Card>
    </div>
  );
};

export default AttackLogVisualization;