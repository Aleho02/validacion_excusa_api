import axios from 'axios';
import { AuthResponse, LoginCredentials, RegisterData } from '../interfaces/types';

const API_URL = 'http://localhost:8000/api';

export const authService = {
  async register(data: RegisterData): Promise<void> {
    try {
      await axios.post(`${API_URL}/usuarios/register/`, data);
    } catch (error) {
      console.error('Error en el registro:', error);
      throw error;
    }
  },

  async login(credentials: LoginCredentials): Promise<AuthResponse> {
    const response = await axios.post(`${API_URL}/token/`, credentials);
    if (response.data.access) {
      localStorage.setItem('token', response.data.access);
      localStorage.setItem('refresh', response.data.refresh);
    }
    return response.data;
  },

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('refresh');
  },

  async refreshToken(): Promise<string> {
    const refresh = localStorage.getItem('refresh');
    if (!refresh) throw new Error('No refresh token available');
    
    const response = await axios.post(`${API_URL}/token/refresh/`, {
      refresh,
    });
    
    if (response.data.access) {
      localStorage.setItem('token', response.data.access);
      return response.data.access;
    }
    throw new Error('Failed to refresh token');
  },

  getToken(): string | null {
    return localStorage.getItem('token');
  },

  isAuthenticated(): boolean {
    return !!this.getToken();
  },
}; 