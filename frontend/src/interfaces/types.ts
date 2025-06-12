export interface User {
  id: number;
  username: string;
  email: string;
  role: 'estudiante' | 'funcionario';
}

export interface Excusa {
  id: number;
  estudiante: number;
  fecha_creacion: string;
  fecha_excusa: string;
  motivo: string;
  documento: string;
  estado: 'pendiente' | 'aprobada' | 'rechazada';
}

export interface CursoAfectado {
  id: number;
  excusa: number;
  nombre_curso: string;
  codigo_curso: string;
  docente: string;
}

export interface Validacion {
  id: number;
  excusa: number;
  funcionario: number;
  fecha_validacion: string;
  estado: 'aprobada' | 'rechazada';
  comentarios: string;
}

export interface AuthResponse {
  access: string;
  refresh: string;
}

export interface LoginCredentials {
  username: string;
  password: string;
}

export interface RegisterData {
  username: string;
  email: string;
  password: string;
  role: 'estudiante' | 'funcionario';
} 