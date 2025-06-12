import apiClient from '../lib/apiClient';
import { ResponseAction, ResponseHistory } from '../types/apiTypes';

export const getRecommendedActions = () => {
  return apiClient.get<ResponseAction[]>('/api/responses/actions');
};

export const getResponseHistory = () => {
  return apiClient.get<ResponseHistory[]>('/api/responses/history');
};

interface ExecuteActionPayload {
  action_title: string;
  target_prediction_id?: string;
  executed_by?: string;
}

export const executeAction = (payload: ExecuteActionPayload) => {
  return apiClient.post<ResponseHistory>('/api/responses/execute', payload);
};