import apiClient from '../lib/apiClient';
import {
  DDoSParams,
  BruteForceParams,
  SQLInjectionParams,
  SimulationStartResponse
} from '../types/apiTypes';

export const startDdosSimulation = (params: DDoSParams) => {
  return apiClient.post<SimulationStartResponse>('/api/simulate/ddos', params);
};

export const startBruteForceSimulation = (params: BruteForceParams) => {
  return apiClient.post<SimulationStartResponse>('/api/simulate/bruteforce', params);
};

export const startSqliSimulation = (params: SQLInjectionParams) => {
  return apiClient.post<SimulationStartResponse>('/api/simulate/sqlinjection', params);
};