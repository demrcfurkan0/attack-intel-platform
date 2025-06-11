import apiClient from '../lib/apiClient';
import { AttackTrendsResponse, DetectionMetricsResponse } from '../types/apiTypes';

export const getAttackTrends = () => {
  return apiClient.get<AttackTrendsResponse>('/api/stats/attack_trends');
};

export const getDetectionMetrics = () => {
  return apiClient.get<DetectionMetricsResponse>('/api/stats/detection_metrics');
};