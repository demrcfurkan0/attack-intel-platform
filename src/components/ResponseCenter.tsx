import React, { useEffect, useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { ShieldCheck, Loader2 } from 'lucide-react';
import { getResponseHistory, executeResponseAction } from '@/services/responseService';
import { ResponseHistory } from '@/types/apiTypes';
import { useToast } from '@/hooks/use-toast';

const ResponseCenter = () => {
  const [responses, setResponses] = useState<ResponseHistory[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const { toast } = useToast();

  useEffect(() => {
    const fetchResponses = async () => {
      setIsLoading(true);
      try {
        const response = await getResponseHistory();
        setResponses(response.data);
      } catch (err) {
        console.error(err);
        setError("Could not load response history.");
      } finally {
        setIsLoading(false);
      }
    };

    fetchResponses();
  }, []);

  const handleExecuteAction = async (action: string, predictionId: string) => {
    try {
      const res = await executeResponseAction(action, predictionId);
      toast({
        title: '✅ Action Executed',
        description: res.data.result_message,
      });
    } catch (err) {
      toast({
        title: '❌ Action Failed',
        description: 'An error occurred while executing the response.',
        variant: 'destructive',
      });
      console.error(err);
    }
  };

  if (isLoading) {
    return <div className="flex justify-center items-center h-40"><Loader2 className="w-8 h-8 animate-spin text-cyber-primary" /></div>;
  }

  if (error) {
    return <Alert variant="destructive">{error}</Alert>;
  }

  return (
    <Card className="glass-morphism border-cyber-light/30">
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <ShieldCheck className="w-5 h-5 text-cyber-primary" />
          <span>Incident Response Log</span>
        </CardTitle>
        <CardDescription>Latest actions taken in response to threats</CardDescription>
      </CardHeader>
      <CardContent className="space-y-4">
        {responses.length === 0 ? (
          <p className="text-gray-400">No response actions have been recorded yet.</p>
        ) : (
          responses.map((res) => (
            <Alert key={res.id} className="border-cyber-light/30 bg-cyber-darker/50">
              <div className="space-y-1">
                <h4 className="font-medium text-gray-200">{res.action_title}</h4>
                <AlertDescription className="text-gray-300">{res.result_message}</AlertDescription>
                <div className="text-sm text-gray-400">
                  Target: {res.target}<br />
                  By: {res.executed_by} | {new Date(res.timestamp).toLocaleString()}
                </div>
                <div className="mt-2 flex space-x-2">
                  <button
                    className="bg-cyber-warning text-black px-3 py-1 rounded text-sm hover:bg-cyber-warning/80 transition"
                    onClick={() => handleExecuteAction("Alert Admin", res.id)}
                  >
                    Alert Admin
                  </button>
                  <button
                    className="bg-cyber-accent text-white px-3 py-1 rounded text-sm hover:bg-cyber-accent/80 transition"
                    onClick={() => handleExecuteAction("Block IP", res.id)}
                  >
                    Block IP
                  </button>
                </div>
              </div>
            </Alert>
          ))
        )}
      </CardContent>
    </Card>
  );
};

export default ResponseCenter;