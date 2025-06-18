import apiClient from '../lib/apiClient';
import { AttackTrendsResponse, DetectionMetricsResponse, ModelPerformanceResponse } from '../types/apiTypes';

export const getAttackTrends = () => {
  return apiClient.get<AttackTrendsResponse>('/api/stats/attack_trends');
};

export const getDetectionMetrics = () => {
  return apiClient.get<DetectionMetricsResponse>('/api/stats/detection_metrics');
};

export const getModelPerformance = () => {
  return apiClient.get<ModelPerformanceResponse>('/api/stats/model-performance');
};