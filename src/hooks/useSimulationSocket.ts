import { useState, useEffect, useRef } from 'react';
import { useToast } from './use-toast';

export interface SimulationUpdate {
  type: 'progress' | 'completed' | 'error' | 'final_summary';
  message: string;
  completed?: number;
  total?: number;
}

export const useSimulationSocket = (simulationId: string | null) => {
  const [statusMessage, setStatusMessage] = useState('');
  const [progress, setProgress] = useState(0);
  const [isConnected, setIsConnected] = useState(false);
  const [isFinished, setIsFinished] = useState(false);
  const webSocketRef = useRef<WebSocket | null>(null);
  const { toast } = useToast();

  useEffect(() => {
    if (!simulationId) {
      return;
    }

    setIsFinished(false);
    setProgress(0);
    setStatusMessage('Connecting to real-time feed...');
    
    const wsUrl = (import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000')
                    .replace(/^http/, 'ws') + `/ws/simulation/${simulationId}`;
    
    const socket = new WebSocket(wsUrl);
    webSocketRef.current = socket;

    socket.onopen = () => {
      console.log(`WebSocket connected for simulation: ${simulationId}`);
      setIsConnected(true);
      setStatusMessage('Real-time feed connected.');
    };

    socket.onmessage = (event) => {
      try {
        const data: SimulationUpdate = JSON.parse(event.data);
        setStatusMessage(data.message);

        if (data.type === 'progress' && data.total && data.total > 0) {
          setProgress(Math.round((data.completed! / data.total) * 100));
        }

        if (data.type === 'completed' || data.type === 'error' || data.type === 'final_summary') {
          setProgress(100);
          setIsFinished(true); 
          if (data.type === 'error') {
            toast({
              variant: 'destructive',
              title: 'Simulation Error',
              description: data.message,
            });
          }
        }
      } catch (error) {
        console.error('Error parsing WebSocket message:', error);
      }
    };

    socket.onclose = () => {
      console.log(`WebSocket disconnected for simulation: ${simulationId}`);
      setIsConnected(false);
      if(isFinished) {
          toast({
            title: "Simulation Finished",
            description: "Real-time feed disconnected.",
          });
      }
    };

    socket.onerror = (err) => {
      console.error('WebSocket Error:', err);
      toast({
        variant: 'destructive',
        title: 'WebSocket Connection Error',
        description: 'Could not connect to the real-time feed.',
      });
      setIsConnected(false);
    };

    return () => {
      if (socket.readyState === WebSocket.OPEN) {
        socket.close();
      }
      webSocketRef.current = null;
    };
  }, [simulationId, toast, isFinished]); 

  return { statusMessage, progress, isConnected, isFinished };
};