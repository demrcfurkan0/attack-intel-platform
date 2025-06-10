export enum HTTPMethod {
    GET = "GET",
    POST = "POST",
  }
  
  export interface DDoSParams {
    target_url: string;
    num_requests?: number;
    concurrency?: number;
    method?: HTTPMethod;
    payload?: Record<string, any>;
    headers?: Record<string, string>;
    timeout_seconds?: number;
    random_delay_ms_max?: number;
  }
  
  export interface BruteForceParams {
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
  
  export interface SQLInjectionParams {
    target_url: string;
    param_to_inject: string;
    method?: HTTPMethod;
    other_post_data?: Record<string, string>;
    base_value_for_param?: string;
    payload_categories?: string[];
    error_indicator_texts?: string[];
  }
  
  export interface PredictionInput {
    features: Record<string, number>;
    source_info?: string;
  }
  
  export interface PredictionOutput {
    prediction_label: string;
    prediction_id: number;
    probabilities?: number[];
    processed_features_count: number;
  }
  
  export interface SimulationStartResponse {
    status: string;
    simulation_run_id: string;
    params_received: any;
  }
  
  export interface SimulationLogTargetDetails {
    url: string;
    method: string;
  }
  
  export interface SimulationLogSummary {
      total_requests_attempted?: number;
      successful_requests?: number;
      failed_requests?: number;
      requests_per_second?: number;
      average_request_time_ms?: number;
      status_codes_distribution?: Record<string, number>;
      total_attempts_made?: number;
      credentials_found_count?: number;
      simulation_halted_early?: boolean;
      total_payloads_tested?: number;
      potentially_vulnerable_findings_count?: number;
  }
  
  export interface SimulationLog {
    _id: string; // MongoDB ObjectId
    simulation_id: string;
    simulation_type: string;
    target_details: SimulationLogTargetDetails;
    parameters_used: any;
    status: "completed" | "failed" | "running"; 
    start_time: string; 
    end_time?: string;
    duration_seconds?: number;
    summary?: SimulationLogSummary;
    raw_result?: any; 
    error_message?: string;
    error_traceback?: string;
    created_at: string;
  }
  
  export interface PaginatedResponse<T> {
    total_count: number;
    data: T[];
  }