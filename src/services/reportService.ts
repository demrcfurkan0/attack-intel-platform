// src/services/reportService.ts

import apiClient from '../lib/apiClient';
import { PaginatedSimulationsResponse, PaginatedPredictionsResponse } from '../types/apiTypes';

interface GetSimulationLogsParams {
  limit?: number;
  skip?: number;
  sim_type?: 'ddos' | 'brute_force' | 'sql_injection';
}

export const getSimulationLogs = (params: GetSimulationLogsParams = {}) => {
  return apiClient.get<PaginatedSimulationsResponse>('/api/reports/simulations', { params });
};


interface GetPredictionLogsParams {
  limit?: number;
  skip?: number;
}

// --- YENİ FONKSİYON ---
export const getPredictionLogs = (params: GetPredictionLogsParams = {}) => {
  return apiClient.get<PaginatedPredictionsResponse>('/api/reports/predictions', { params });
};