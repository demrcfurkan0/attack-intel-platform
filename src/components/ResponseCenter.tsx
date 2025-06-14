// Yeni UI bileşeni: ResponseCenter.tsx
import React, { useEffect, useState } from 'react';
import { Badge } from '@/components/ui/badge';
import {
  Card, CardContent, CardDescription, CardHeader, CardTitle
} from '@/components/ui/card';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { ShieldCheck, Loader2 } from 'lucide-react';
import { getResponseHistory } from '@/services/responseService';
import { ResponseHistory } from '@/types/apiTypes';
import { Button } from '@/components/ui/button';
import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { useToast } from '@/hooks/use-toast';

const RESPONSE_OPTIONS = {
  ddos: [
    { label: 'Rate Limiting', severity: 'high' },
    { label: 'Geo Blocking', severity: 'medium' },
    { label: 'Notify ISP', severity: 'low' },
  ],
  brute_force: [
    { label: 'Lock Account', severity: 'high' },
    { label: 'CAPTCHA Verification', severity: 'medium' },
    { label: 'Alert Admin', severity: 'low' },
  ],
  sql_injection: [
    { label: 'Sanitize Inputs', severity: 'high' },
    { label: 'Block IP', severity: 'medium' },
    { label: 'Notify DevOps', severity: 'low' },
  ],
};

const inferAttackType = (response: ResponseHistory): keyof typeof RESPONSE_OPTIONS => {
  return (response.attack_type || 'ddos') as keyof typeof RESPONSE_OPTIONS;
};

const ResponseCenter = () => {
  const [responses, setResponses] = useState<ResponseHistory[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [selected, setSelected] = useState<any>(null);
  const { toast } = useToast();

  useEffect(() => {
    const fetchResponses = async () => {
      setIsLoading(true);
      try {
        const response = await getResponseHistory();
        setResponses(response.data);
      } catch {
        toast({ title: 'Failed to load response history', variant: 'destructive' });
      } finally {
        setIsLoading(false);
      }
    };
    fetchResponses();
  }, []);

  const openDialog = (res: ResponseHistory) => setSelected(res);
  const closeDialog = () => setSelected(null);

  return (
    <Card className="glass-morphism border-cyber-light/30">
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <ShieldCheck className="w-5 h-5 text-cyber-primary" />
          <span>Incident Response Log</span>
        </CardTitle>
        <CardDescription>Take action based on prediction logs</CardDescription>
      </CardHeader>
      <CardContent className="space-y-4">
        {isLoading ? <Loader2 className="animate-spin" /> : (
          responses.map((res) => (
            <Alert key={res.id} className="bg-cyber-darker/50">
              <div>
                <h4 className="font-medium text-white">{res.action_title}</h4>
                <AlertDescription className="text-gray-300">{res.result_message}</AlertDescription>
                <p className="text-sm text-gray-400">
                  Target: {res.target}<br />By: {res.executed_by} | {new Date(res.timestamp).toLocaleString()}
                </p>
                <div className="mt-2">
                  <Button variant="destructive" onClick={() => openDialog(res)}>Choose Action</Button>
                </div>
              </div>
            </Alert>
          ))
        )}
      </CardContent>

      <Dialog open={!!selected} onOpenChange={closeDialog}>
        <DialogContent>
  <DialogHeader>
    <DialogTitle>Recommended Actions</DialogTitle>
  </DialogHeader>
  {selected && (
    <div className="space-y-2">
      {(RESPONSE_OPTIONS[inferAttackType(selected)] || [])
        .sort((a, b) => a.severity === 'high' ? -1 : 1)
        .map((opt, idx) => (
          <div key={idx} className="flex justify-between">
            <span className="text-white">{opt.label}</span>
            <Badge variant={opt.severity === 'high' ? 'destructive' : 'default'}>
              {opt.severity.toUpperCase()}
            </Badge>
          </div>
        ))}
    </div>
  )}
</DialogContent>
      </Dialog>
    </Card>
  );
};

export default ResponseCenter;