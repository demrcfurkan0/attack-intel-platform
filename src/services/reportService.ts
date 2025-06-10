import apiClient from '../lib/apiClient';
import { PaginatedResponse, SimulationLog } from '../types/apiTypes';

interface GetSimulationLogsParams {
  limit?: number;
  skip?: number;
  sim_type?: 'ddos' | 'brute_force' | 'sql_injection';
}

export const getSimulationLogs = (params: GetSimulationLogsParams = {}) => {
  return apiClient.get<PaginatedResponse<SimulationLog>>('/api/reports/simulations', { params });
};