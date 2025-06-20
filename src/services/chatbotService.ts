import apiClient from '../lib/apiClient';
import { PredictionLog } from '../types/apiTypes';

interface ChatQueryPayload {
  prompt: string;
  incident_details: PredictionLog; 
}

interface ChatQueryResponse {
  response: string;
}


export const postChatQuery = (payload: ChatQueryPayload) => {
  return apiClient.post<ChatQueryResponse>('/api/chatbot/query', payload);
};