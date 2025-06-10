import axios, { AxiosError } from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

apiClient.interceptors.response.use(
  (response) => response,
  (error: AxiosError) => {
    if (error.response && error.response.data) {
      const errorData = error.response.data as any; //
      if (errorData.detail) {
        if (Array.isArray(errorData.detail) && errorData.detail.length > 0 && errorData.detail[0].msg) {
          const validationError = errorData.detail[0];
          const field = validationError.loc ? validationError.loc.join(' -> ') : 'N/A';
          console.error(`API Validation Error on field ${field}: ${validationError.msg}`);
          // error.message = `Validation Error on ${field}: ${validationError.msg}`;
        } else if (typeof errorData.detail === 'string') {
          console.error('API Error Detail:', errorData.detail);
          // error.message = errorData.detail;
        }
      }
    } else {
      console.error('API Network Error or other:', error.message);
    }
    return Promise.reject(error);
  }
);

export default apiClient;