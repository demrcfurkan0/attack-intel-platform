import apiClient from '../lib/apiClient';
import { ResponseAction, ResponseHistory } from '../types/apiTypes';

export const getRecommendedActions = () => {
  return apiClient.get<ResponseAction[]>('/api/responses/actions');
};

export const getResponseHistory = (limit = 10) =>
  apiClient.get(`api/responses/history?limit=${limit}`);

interface ExecuteActionPayload {
  action_title: string;
  target_prediction_id?: string;
  executed_by?: string;
}

export const executeAction = (payload: ExecuteActionPayload) => {
  return apiClient.post<ResponseHistory>('/api/responses/execute', payload);
};

export const executeResponseAction = async (
  action_title: string,
  target_prediction_id: string,
  executed_by: string = 'analyst'
) => {
  return await apiClient.post("api/responses/execute", {
    action_title,
    target_prediction_id,
    executed_by,
  });
};

export const blockIpAddress = (ipAddress: string) => {
  return apiClient.post('/api/responses/block-ip', { ip_address: ipAddress });
};

export const getIncidentHistory = (predictionId: string) => {
  return apiClient.get<ResponseHistory[]>(`/api/responses/history/${predictionId}`);
};

