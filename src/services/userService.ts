import apiClient from '../lib/apiClient';
import { User, UserCreatePayload, UserUpdatePayload } from '../types/apiTypes';

export const getUsers = () => apiClient.get<User[]>('/api/users');
export const createUser = (payload: UserCreatePayload) => apiClient.post<User>('/api/users', payload);
export const deleteUser = (userId: string) => apiClient.delete(`/api/users/${userId}`);
export const updateUser = (userId: string, payload: UserUpdatePayload) => apiClient.patch<User>(`/api/users/${userId}`, payload);