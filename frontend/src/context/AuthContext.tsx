import React, { createContext, useContext, useState, useEffect } from 'react';
import { User } from '../interfaces/types';
import { authService } from '../services/authService';
import { jwtDecode } from 'jwt-decode';

interface AuthContextType {
  user: User | null;
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);

  useEffect(() => {
    const token = authService.getToken();
    if (token) {
      try {
        const decoded: any = jwtDecode(token);
        setUser({
          id: decoded.user_id,
          username: decoded.username,
          email: decoded.email,
          role: decoded.role,
        });
        setIsAuthenticated(true);
      } catch (error) {
        console.error('Error decoding token:', error);
        authService.logout();
        setIsAuthenticated(false);
      }
    }
  }, []);

  const login = async (username: string, password: string) => {
    try {
      const response = await authService.login({ username, password });
      const decoded: any = jwtDecode(response.access);
      setUser({
        id: decoded.user_id,
        username: decoded.username,
        email: decoded.email,
        role: decoded.role,
      });
      setIsAuthenticated(true);
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  };

  const logout = () => {
    authService.logout();
    setUser(null);
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, isAuthenticated }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}; 