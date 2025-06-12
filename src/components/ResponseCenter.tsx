import React, { useState, useEffect, useMemo } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Textarea } from '@/components/ui/textarea';
import { Alert } from '@/components/ui/alert';
import { getRecommendedActions, getResponseHistory, executeAction } from '@/services/responseService';
import { ResponseAction, ResponseHistory } from '@/types/apiTypes';
import { useToast } from '@/hooks/use-toast';
import { Loader2, PlayCircle, Clock, CheckCircle, Bot, Shield } from 'lucide-react';

const ResponseCenter = () => {
  const [actions, setActions] = useState<ResponseAction[]>([]);
  const [history, setHistory] = useState<ResponseHistory[]>([]);
  const [customActionText, setCustomActionText] = useState('');
  const [isLoading, setIsLoading] = useState(true);
  const [executingId, setExecutingId] = useState<string | null>(null);
  const { toast } = useToast();

  const fetchData = async () => {
    try {
      const [actionsRes, historyRes] = await Promise.all([
        getRecommendedActions(),
        getResponseHistory()
      ]);
      setActions(actionsRes.data);
      setHistory(historyRes.data);
    } catch (error) {
      toast({ variant: 'destructive', title: 'Failed to load response data.' });
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 15000); // 15 saniyede bir yenile
    return () => clearInterval(interval);
  }, []);

  const handleExecute = async (actionId: string, title: string) => {
    setExecutingId(actionId);
    try {
      await executeAction({ action_title: title, target_prediction_id: actionId });
      toast({ title: "Action Executed", description: `${title} has been logged.` });
      await fetchData();
    } catch (error) {
      toast({ variant: 'destructive', title: 'Execution Failed' });
    } finally {
      setExecutingId(null);
    }
  };

  const stats = useMemo(() => ({
    completed: history.filter(h => h.status === 'completed').length,
    failed: history.filter(h => h.status === 'failed').length,
  }), [history]);

  return (
    <div className="space-y-6">
      {/* İstatistik Kartları */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card className="glass-morphism"><CardHeader><CardTitle>Active Responses</CardTitle></CardHeader><CardContent className="text-2xl font-bold">0</CardContent></Card>
        <Card className="glass-morphism"><CardHeader><CardTitle>Queued Actions</CardTitle></CardHeader><CardContent className="text-2xl font-bold">0</CardContent></Card>
        <Card className="glass-morphism"><CardHeader><CardTitle>Completed Today</CardTitle></CardHeader><CardContent className="text-2xl font-bold text-green-400">{isLoading ? '...' : stats.completed}</CardContent></Card>
        <Card className="glass-morphism"><CardHeader><CardTitle>Failed Actions</CardTitle></CardHeader><CardContent className="text-2xl font-bold text-red-500">{isLoading ? '...' : stats.failed}</CardContent></Card>
      </div>

      {/* Önerilen Eylemler */}
      <Card className="glass-morphism">
        <CardHeader><CardTitle>AI-Recommended Response Actions</CardTitle></CardHeader>
        <CardContent className="space-y-4">
          {isLoading ? <Loader2 className="animate-spin" /> : actions.map(action => (
            <Alert key={action.id}>
              <div className="flex justify-between items-center">
                <div>
                  <p className="font-bold">{action.title} <Badge>{action.severity}</Badge></p>
                  <p className="text-sm text-gray-400">{action.description}</p>
                </div>
                <Button onClick={() => handleExecute(action.id, action.title)} disabled={!!executingId}>
                  {executingId === action.id ? <Loader2 className="animate-spin" /> : <PlayCircle className="mr-2" />} Execute
                </Button>
              </div>
            </Alert>
          ))}
        </CardContent>
      </Card>
      
      {/* Custom Action */}
      <Card className="glass-morphism">
        <CardHeader><CardTitle>Custom Response Action</CardTitle></CardHeader>
        <CardContent className="flex items-end gap-4">
          <Textarea placeholder="Enter custom commands..." value={customActionText} onChange={e => setCustomActionText(e.target.value)} />
          <Button onClick={() => handleExecute('custom', customActionText)} disabled={!customActionText || !!executingId}>
            {executingId === 'custom' ? <Loader2 className="animate-spin" /> : <PlayCircle className="mr-2" />} Execute Custom
          </Button>
        </CardContent>
      </Card>

      {/* Yanıt Geçmişi */}
      <Card className="glass-morphism">
        <CardHeader><CardTitle>Response History</CardTitle></CardHeader>
        <CardContent className="space-y-3">
          {isLoading ? <Loader2 className="animate-spin" /> : history.map(entry => (
            <div key={entry.id} className="flex justify-between p-2 rounded bg-cyber-darker/50">
              <div>
                <p className="font-semibold">{entry.action_title}</p>
                <p className="text-xs text-gray-400">{entry.result_message}</p>
              </div>
              <div className="text-right">
                <p className="text-xs">{new Date(entry.timestamp).toLocaleTimeString()}</p>
                <Badge>{entry.status}</Badge>
              </div>
            </div>
          ))}
        </CardContent>
      </Card>
    </div>
  );
};
export default ResponseCenter;