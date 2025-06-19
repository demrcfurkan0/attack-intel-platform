// in: attack-intel-platform/src/services/chatbotService.ts

import apiClient from '../lib/apiClient';
import { PredictionLog } from '../types/apiTypes';

// Backend'e göndereceğimiz verinin tipi
interface ChatQueryPayload {
  prompt: string;
  incident_details: PredictionLog; // O an incelenen olayın tüm detayları
}

// Backend'den beklediğimiz cevabın tipi
interface ChatQueryResponse {
  response: string;
}

/**
 * Kullanıcının sorusunu ve olay detaylarını backend'deki chatbot endpoint'ine gönderir.
 * @param payload - Prompt ve olay detaylarını içeren nesne.
 * @returns Yapay zeka asistanından gelen cevabı içeren bir Promise.
 */
export const postChatQuery = (payload: ChatQueryPayload) => {
  return apiClient.post<ChatQueryResponse>('/api/chatbot/query', payload);
};