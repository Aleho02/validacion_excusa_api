import React from 'react';
import { useFormik } from 'formik';
import * as yup from 'yup';
import { Box, Button, TextField, Typography, Container, Paper, MenuItem } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { authService } from '../services/authService';
import { RegisterData } from '../interfaces/types';

const validationSchema = yup.object({
  username: yup.string()
    .required('El usuario es requerido')
    .min(3, 'El usuario debe tener al menos 3 caracteres'),
  email: yup.string()
    .required('El correo electrónico es requerido')
    .email('Ingrese un correo electrónico válido')
    .matches(
      /@ucundinamarca\.edu\.co$/,
      'Solo se permiten correos institucionales (@ucundinamarca.edu.co)'
    ),
  password: yup.string()
    .required('La contraseña es requerida')
    .min(8, 'La contraseña debe tener al menos 8 caracteres'),
  confirmPassword: yup.string()
    .required('Confirme su contraseña')
    .oneOf([yup.ref('password')], 'Las contraseñas deben coincidir'),
  role: yup.string()
    .required('El rol es requerido')
    .oneOf(['estudiante', 'funcionario'] as const, 'Rol no válido')
});

type FormValues = {
  username: string;
  email: string;
  password: string;
  confirmPassword: string;
  role: 'estudiante' | 'funcionario';
};

export const RegisterForm: React.FC = () => {
  const navigate = useNavigate();

  const formik = useFormik<FormValues>({
    initialValues: {
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
      role: 'estudiante'
    },
    validationSchema: validationSchema,
    onSubmit: async (values) => {
      try {
        const registerData: RegisterData = {
          username: values.username,
          email: values.email,
          password: values.password,
          role: values.role
        };
        await authService.register(registerData);
        navigate('/login');
      } catch (error) {
        console.error('Error en el registro:', error);
        // Manejar errores específicos aquí
      }
    },
  });

  return (
    <Container component="main" maxWidth="xs">
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Paper elevation={3} sx={{ p: 4, width: '100%' }}>
          <Typography component="h1" variant="h5" align="center" gutterBottom>
            Registro de Usuario
          </Typography>
          <form onSubmit={formik.handleSubmit}>
            <TextField
              fullWidth
              id="username"
              name="username"
              label="Usuario"
              value={formik.values.username}
              onChange={formik.handleChange}
              error={formik.touched.username && Boolean(formik.errors.username)}
              helperText={formik.touched.username && formik.errors.username}
              margin="normal"
            />
            <TextField
              fullWidth
              id="email"
              name="email"
              label="Correo Electrónico"
              value={formik.values.email}
              onChange={formik.handleChange}
              error={formik.touched.email && Boolean(formik.errors.email)}
              helperText={formik.touched.email && formik.errors.email}
              margin="normal"
            />
            <TextField
              fullWidth
              id="password"
              name="password"
              label="Contraseña"
              type="password"
              value={formik.values.password}
              onChange={formik.handleChange}
              error={formik.touched.password && Boolean(formik.errors.password)}
              helperText={formik.touched.password && formik.errors.password}
              margin="normal"
            />
            <TextField
              fullWidth
              id="confirmPassword"
              name="confirmPassword"
              label="Confirmar Contraseña"
              type="password"
              value={formik.values.confirmPassword}
              onChange={formik.handleChange}
              error={formik.touched.confirmPassword && Boolean(formik.errors.confirmPassword)}
              helperText={formik.touched.confirmPassword && formik.errors.confirmPassword}
              margin="normal"
            />
            <TextField
              fullWidth
              id="role"
              name="role"
              select
              label="Rol"
              value={formik.values.role}
              onChange={formik.handleChange}
              error={formik.touched.role && Boolean(formik.errors.role)}
              helperText={formik.touched.role && formik.errors.role}
              margin="normal"
            >
              <MenuItem value="estudiante">Estudiante</MenuItem>
              <MenuItem value="funcionario">Funcionario</MenuItem>
            </TextField>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Registrarse
            </Button>
            <Button
              fullWidth
              variant="text"
              onClick={() => navigate('/login')}
            >
              ¿Ya tienes una cuenta? Inicia sesión
            </Button>
          </form>
        </Paper>
      </Box>
    </Container>
  );
}; 