# API de Validación de Excusas Médicas

Esta API REST fue desarrollada para gestionar el proceso de validación de excusas médicas en una universidad. Permite a los estudiantes subir sus excusas médicas, a los funcionarios validarlas y mantener un registro de los cursos afectados.

## Características

- Autenticación JWT
- Gestión de estudiantes y funcionarios
- Carga y validación de excusas médicas
- Registro de cursos afectados por las excusas
- Validación de excusas por funcionarios autorizados

## Tecnologías Utilizadas

- Django 4.2
- Django REST Framework
- PostgreSQL
- JWT Authentication

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/Aleho02/validacion_excusa_api.git
cd validacion_excusa_api
```

2. Crear y activar el entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar la base de datos en settings.py:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'validacion_excusa_db',
        'USER': 'postgres',
        'PASSWORD': '123456789',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. Realizar las migraciones:
```bash
python manage.py migrate
```

6. Crear un superusuario:
```bash
python manage.py createsuperuser
```

7. Ejecutar el servidor:
```bash
python manage.py runserver
```

## Estructura del Proyecto

El proyecto está organizado en las siguientes aplicaciones:

- `usuarios`: Gestión de estudiantes y funcionarios
- `excusas`: Gestión de excusas médicas y cursos afectados
- `validaciones`: Gestión de validaciones de excusas
- `facultades`: Gestión de facultades y programas académicos

## Endpoints de la API

### Autenticación
- POST /api/token/: Obtener token JWT
- POST /api/token/refresh/: Refrescar token JWT

### Usuarios
- GET/POST /api/estudiantes/: Listar y crear estudiantes
- GET/PUT/DELETE /api/estudiantes/{id}/: Gestionar estudiante específico
- GET/POST /api/funcionarios/: Listar y crear funcionarios
- GET/PUT/DELETE /api/funcionarios/{id}/: Gestionar funcionario específico

### Excusas
- GET/POST /api/excusas/: Listar y crear excusas médicas
- GET/PUT/DELETE /api/excusas/{id}/: Gestionar excusa específica
- GET/POST /api/cursos-afectados/: Listar y crear cursos afectados
- GET/PUT/DELETE /api/cursos-afectados/{id}/: Gestionar curso afectado específico

### Validaciones
- GET/POST /api/validaciones/: Listar y crear validaciones
- GET/PUT/DELETE /api/validaciones/{id}/: Gestionar validación específica

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
python manage.py test
```

## Contribuir

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. 