import React, { useState, useEffect, useMemo } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Alert } from "@/components/ui/alert";
import { Badge } from "@/components/ui/badge";
// ... diğer tüm UI importların ...
import { getRecommendedActions, getResponseHistory, executeAction } from '@/services/responseService';
import { ResponseAction, ResponseHistory } from '@/types/apiTypes';
import { useToast } from '@/hooks/use-toast';
import { Loader2, PlayCircle, Clock, CheckCircle, StopCircle, Bot, Shield } from 'lucide-react';

const ResponseCenter = () => {
  const [actions, setActions] = useState<ResponseAction[]>([]);
  const [history, setHistory] = useState<ResponseHistory[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [executingId, setExecutingId] = useState<string | null>(null);
  const { toast } = useToast();

  const fetchData = async () => {
    setIsLoading(true);
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
  }, []);

  const handleExecute = async (actionId: string, title: string) => {
    setExecutingId(actionId);
    try {
      await executeAction({
        action_title: title,
        target_prediction_id: actionId,
        executed_by: "furkan"
      });
      toast({ title: "Action Executed", description: `${title} has been logged.` });
      await fetchData(); // Yanıt geçmişini yenile
    } catch (error) {
      toast({ variant: 'destructive', title: 'Execution Failed' });
    } finally {
      setExecutingId(null);
    }
  };

  // Kartlar için verileri hesapla
  const historyStats = useMemo(() => {
    return {
      in_progress: history.filter(h => h.status === 'in_progress').length,
      completed: history.filter(h => h.status === 'completed').length,
      failed: history.filter(h => h.status === 'failed').length,
    }
  }, [history]);

  return (
    <div className="space-y-6">
      {/* 1. Kısım: İstatistik Kartları */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        {/* Bu kartların verilerini 'historyStats'ten alıyoruz */}
        <Card><CardHeader><CardTitle>Active Responses</CardTitle></CardHeader><CardContent>{historyStats.in_progress}</CardContent></Card>
        <Card><CardHeader><CardTitle>Completed Today</CardTitle></CardHeader><CardContent>{historyStats.completed}</CardContent></Card>
        <Card><CardHeader><CardTitle>Failed Actions</CardTitle></CardHeader><CardContent>{historyStats.failed}</CardContent></Card>
      </div>

      {/* 2. Kısım: Önerilen Eylemler */}
      <Card>
        <CardHeader><CardTitle>AI-Recommended Response Actions</CardTitle></CardHeader>
        <CardContent className="space-y-4">
          {isLoading ? <Loader2 className="animate-spin" /> : actions.map(action => (
            <Alert key={action.id}>
              {/* ... Alert içeriği action verisiyle doldurulacak ... */}
              <div className="font-medium">{action.title}</div>
              <Button onClick={() => handleExecute(action.id, action.title)} disabled={!!executingId}>
                {executingId === action.id ? <Loader2 className="animate-spin" /> : <PlayCircle />} Execute
              </Button>
            </Alert>
          ))}
        </CardContent>
      </Card>
      
      {/* 3. Kısım: Custom Action (Aynı kalabilir) */}
      <Card>{/* ... */}</Card>

      {/* 4. Kısım: Yanıt Geçmişi */}
      <Card>
        <CardHeader><CardTitle>Response History</CardTitle></CardHeader>
        <CardContent className="space-y-3">
          {isLoading ? <Loader2 className="animate-spin" /> : history.map(entry => (
            <div key={entry.id}>
              <div>{entry.action_title}</div>
              <div className="text-sm">Target: {entry.target}</div>
              <Badge>{entry.status}</Badge>
            </div>
          ))}
        </CardContent>
      </Card>
    </div>
  );
};

export default ResponseCenter;