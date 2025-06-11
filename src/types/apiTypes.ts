// src/types/apiTypes.ts

export type HTTPMethod = "GET" | "POST";

// Request Payloads
export interface DDoSRequestPayload {
  target_url: string;
  num_requests?: number;
  concurrency?: number;
  method?: HTTPMethod;
  payload?: Record<string, any>;
  headers?: Record<string, string>;
  timeout_seconds?: number;
  random_delay_ms_max?: number;
}

export interface BruteForceRequestPayload {
  target_url: string;
  usernames?: string[];
  passwords?: string[];
  success_text_indicator?: string;
  success_status_code?: number;
  username_field?: string;
  password_field?: string;
  concurrency?: number;
  stop_on_first_success?: boolean;
}

export interface SQLInjectionRequestPayload {
  target_url: string;
  param_to_inject: string;
  method?: HTTPMethod;
  other_post_data?: Record<string, string>;
  base_value_for_param?: string;
  payload_categories?: string[];
  error_indicator_texts?: string[];
}

// API Responses
export interface SimulationStartResponse {
  status: string;
  simulation_run_id: string;
  params_received: any;
}

// --- DÜZELTME: İki ayrı log tipi için de paginated response tipleri ---

// Simulation Log Tipi
export interface SimulationLog {
  _id: string;
  simulation_id: string;
  simulation_type: 'ddos' | 'brute_force' | 'sql_injection';
  target_details: { url: string; method: string; };
  parameters_used: any;
  status: "completed" | "failed" | "running";
  start_time: string;
  end_time?: string;
  duration_seconds?: number;
  summary?: any;
  raw_result?: any;
  error_message?: string;
}

// Simulation Log'ları için Sayfalanmış Yanıt Tipi
export interface PaginatedSimulationsResponse {
  total_count: number;
  data: SimulationLog[];
}

// Prediction Log Tipi
export interface PredictionLog {
  _id: string;
  prediction_run_id: string;
  source_of_data: string;
  input_features_snapshot: Record<string, number>;
  prediction_result: {
    prediction_label: string;
    prediction_id: number;
    probabilities?: number[];
    processed_features_count: number;
  };
  is_attack: boolean;
  created_at: string;
}

// Prediction Log'ları için Sayfalanmış Yanıt Tipi
export interface PaginatedPredictionsResponse {
  total_count: number;
  data: PredictionLog[];
}

// Statistics Endpoint Tipleri
export interface AttackTrendsResponse {
  [hour: string]: {
    ddos?: number;
    brute_force?: number;
    sql_injection?: number;
  };
}

export interface DetectionMetricsResponse {
  detected_attacks: number;
  benign_traffic: number;
}

export interface User {
  id: string; // _id'ye karşılık gelir
  username: string;
  email: string;
  role: string;
  status: 'active' | 'inactive';
  lastLogin?: string; // Bu veri backend'den gelmiyor, şimdilik opsiyonel
}

export interface UserCreatePayload {
  username: string;
  email: string;
  role: string;
  password: string;
}

export interface UserUpdatePayload {
    role?: string;
    status?: 'active' | 'inactive';
}