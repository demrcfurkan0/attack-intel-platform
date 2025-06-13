import apiClient from '../lib/apiClient';
import {
  DDoSRequestPayload,
  BruteForceRequestPayload,
  SQLInjectionRequestPayload,
  SimulationStartResponse
} from '../types/apiTypes';

export const startDdosSimulation = (params: DDoSRequestPayload) => {
  return apiClient.post<SimulationStartResponse>('/api/simulate/ddos', params);
};

export const startBruteForceSimulation = (params: BruteForceRequestPayload) => {
  return apiClient.post<SimulationStartResponse>('/api/simulate/bruteforce', params);
};

export const startSqliSimulation = (params: SQLInjectionRequestPayload) => {
  return apiClient.post<SimulationStartResponse>('/api/simulate/sqlinjection', params);
};