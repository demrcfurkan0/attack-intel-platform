import axios, { AxiosError, InternalAxiosRequestConfig } from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

const apiClient = axios.create({
  baseURL: API_BASE_URL, 
});

// --- YENİ INTERCEPTOR ---
// Bu fonksiyon, her istek gönderilmeden ÖNCE çalışır.
apiClient.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    // 1. Tarayıcı hafızasından token'ı oku
    const token = localStorage.getItem('authToken');
    
    // 2. Eğer token varsa, isteğin başlığına ekle
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    
    // 3. Değiştirilmiş config ile isteğin devam etmesini sağla
    return config;
  },
  (error) => {
    // İstek hatası durumunda
    return Promise.reject(error);
  }
);
// --- INTERCEPTOR SONU ---


// Yanıt (response) interceptor'ı aynı kalabilir (hata loglama için)
apiClient.interceptors.response.use(
  (response) => response,
  (error: AxiosError) => {
    if (error.response) {
      console.error('API Error Detail:', error.response.data);
    } else if (error.request) {
      console.error('API Network Error or other:', error.message);
    }
    return Promise.reject(error);
  }
);

export default apiClient;