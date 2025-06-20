import apiClient from '../lib/apiClient';

interface TokenResponse {
  access_token: string;
  token_type: string;
}

export const login = async (username: string, password: string): Promise<TokenResponse> => {

  const params = new URLSearchParams();
  params.append('username', username);
  params.append('password', password);

  const config = {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  };

  const response = await apiClient.post<TokenResponse>('/api/auth/token', params, config);
  return response.data;
};