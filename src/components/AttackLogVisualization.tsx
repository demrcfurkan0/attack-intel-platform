import React, { useState, useEffect, useMemo } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip } from 'recharts';
import { Activity, Loader2, ChevronLeft, ChevronRight } from 'lucide-react';

import { getSimulationLogs } from '../services/reportService';
import { SimulationLog } from '../types/apiTypes';

const LOGS_PER_PAGE = 10;

const AttackLogVisualization = () => {
  const [logs, setLogs] = useState<SimulationLog[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalLogs, setTotalLogs] = useState(0);
  
  const totalPages = Math.ceil(totalLogs / LOGS_PER_PAGE);

  const fetchLogs = async (page: number) => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await getSimulationLogs({
        limit: LOGS_PER_PAGE,
        skip: (page - 1) * LOGS_PER_PAGE,
      });
      setLogs(response.data.data);
      setTotalLogs(response.data.total_count);
    } catch (err) {
      setError("Failed to load attack logs.");
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchLogs(currentPage);
  }, [currentPage]);

  // Grafik verisini, gelen loglardan hesapla
  const attackTimelineData = useMemo(() => {
    if (!logs.length) return [];
    const timeline = logs
      .slice() // Orijinal diziyi değiştirmemek için kopyala
      .sort((a, b) => new Date(a.start_time).getTime() - new Date(b.start_time).getTime())
      .map(log => ({
        time: new Date(log.start_time).toLocaleTimeString(),
        // Örnek bir metrik, örn. DDoS ise request sayısı, değilse 1
        attacks: log.summary?.total_requests_attempted || 1,
        type: log.simulation_type
      }));
    return timeline;
  }, [logs]);

  return (
    <div className="space-y-6">
      <Card className="glass-morphism border-cyber-light/30">
          <CardHeader>
            <CardTitle>Attack Timeline</CardTitle>
          </CardHeader>
          <CardContent>
            {isLoading ? <Loader2 className="animate-spin" /> : 
            <ResponsiveContainer width="100%" height={250}>
              <LineChart data={attackTimelineData}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(0, 255, 136, 0.1)" />
                <XAxis dataKey="time" stroke="#00ff88" fontSize={12} />
                <YAxis stroke="#00ff88" fontSize={12} />
                <Tooltip />
                <Line type="monotone" dataKey="attacks" stroke="#ff4444" strokeWidth={2} />
              </LineChart>
            </ResponsiveContainer>
            }
          </CardContent>
      </Card>

      <Card className="glass-morphism border-cyber-light/30">
        <CardHeader>
          <CardTitle>Attack Log Details</CardTitle>
          <CardDescription>Detailed security event logs from simulations</CardDescription>
        </CardHeader>
        <CardContent>
          {isLoading ? (
            <div className="flex justify-center items-center h-40">
              <Loader2 className="w-8 h-8 animate-spin text-cyber-primary" />
            </div>
          ) : error ? (
            <p className="text-cyber-accent">{error}</p>
          ) : (
            <>
              <div className="overflow-x-auto">
                <Table>
                  <TableHeader>
                    <TableRow>
                      <TableHead>Type</TableHead>
                      <TableHead>Target</TableHead>
                      <TableHead>Status</TableHead>
                      <TableHead>Start Time</TableHead>
                      <TableHead>Duration (s)</TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {logs.map((log) => (
                      <TableRow key={log.simulation_id}>
                        <TableCell>{log.simulation_type.toUpperCase()}</TableCell>
                        <TableCell className="max-w-xs truncate">{log.target_details.url}</TableCell>
                        <TableCell><Badge variant={log.status === 'completed' ? 'default' : 'destructive'}>{log.status}</Badge></TableCell>
                        <TableCell>{new Date(log.start_time).toLocaleString()}</TableCell>
                        <TableCell>{log.duration_seconds}</TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </div>
              {/* Pagination */}
              <div className="flex items-center justify-end space-x-2 py-4">
                <Button variant="outline" size="sm" onClick={() => setCurrentPage(p => Math.max(1, p - 1))} disabled={currentPage === 1}>
                  <ChevronLeft className="h-4 w-4" /> Previous
                </Button>
                <span className="text-sm">Page {currentPage} of {totalPages}</span>
                <Button variant="outline" size="sm" onClick={() => setCurrentPage(p => Math.min(totalPages, p + 1))} disabled={currentPage === totalPages}>
                  Next <ChevronRight className="h-4 w-4" />
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