import React from 'react';
import { useQuery } from '@tanstack/react-query';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { Loader2, AlertCircle, Cpu } from 'lucide-react';
import { getModelPerformance } from '@/services/statisticsService';

const getCellColor = (isDiagonal: boolean, value: number) => {
  if (isDiagonal) {
    return value > 0 ? 'bg-green-500/20 text-green-300' : 'bg-transparent'; 
  }
  return value > 0 ? 'bg-red-500/20 text-red-300' : 'bg-transparent'; 
};

const ModelPerformanceMatrix = () => {
  const { data: response, isLoading, isError } = useQuery({
    queryKey: ['modelPerformance'],
    queryFn: getModelPerformance,
    refetchInterval: 30000, 
  });

  const matrixData = response?.data;
  const labels = matrixData ? Object.keys(matrixData) : [];

  const renderContent = () => {
    if (isLoading) {
      return <div className="flex justify-center items-center h-40"><Loader2 className="w-8 h-8 animate-spin" /></div>;
    }
    if (isError || !matrixData) {
      return <div className="text-cyber-accent flex items-center space-x-2"><AlertCircle className="h-5 w-5" /><span>Failed to load model performance.</span></div>;
    }

    return (
      <div className="overflow-x-auto">
        <Table className="min-w-full">
          <TableHeader>
            <TableRow className="border-cyber-light/20">
              <TableHead className="w-[150px] sticky left-0 bg-cyber-darker z-10">
                <div className='italic text-xs text-gray-400'>Predicted as →</div>
                <div className='font-bold text-sm'>Actual Class ↓</div>
              </TableHead>
              {labels.map(label => <TableHead key={label} className="text-center">{label}</TableHead>)}
            </TableRow>
          </TableHeader>
          <TableBody>
            {labels.map(trueLabel => (
              <TableRow key={trueLabel} className="border-cyber-light/10">
                <TableCell className="font-medium sticky left-0 bg-cyber-darker z-10">{trueLabel}</TableCell>
                {labels.map(predictedLabel => {
                  const value = matrixData[trueLabel]?.[predictedLabel] || 0;
                  const isDiagonal = trueLabel === predictedLabel;
                  return (
                    <TableCell key={predictedLabel} className={`text-center font-mono text-lg ${getCellColor(isDiagonal, value)}`}>
                      {value}
                    </TableCell>
                  );
                })}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    );
  };

  return (
    <Card className="glass-morphism border-cyber-light/30">
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <Cpu className="w-5 h-5 text-cyber-primary" />
          <span>Model Performance (Confusion Matrix)</span>
        </CardTitle>
        <CardDescription>Compares actual simulation types with AI model's predictions.</CardDescription>
      </CardHeader>
      <CardContent>
        {renderContent()}
      </CardContent>
    </Card>
  );
};

export default ModelPerformanceMatrix;