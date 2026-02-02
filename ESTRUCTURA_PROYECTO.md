# Estructura del Proyecto

## Archivos Esenciales

### Aplicación Principal
- `app.py` - Aplicación Flask principal con todos los endpoints (CRUD + IA)
- `requirements.txt` - Dependencias del proyecto
- `migrate_db.py` - Script para migrar bases de datos existentes

### Servicios
- `services/` - Directorio de servicios
  - `__init__.py` - Inicialización del módulo
  - `ai_service.py` - Servicio de IA para interactuar con Ollama

### Interfaz Web
- `templates/` - Plantillas HTML
  - `base.html` - Plantilla base
  - `login.html` - Página de inicio de sesión
  - `register.html` - Página de registro
  - `dashboard.html` - Panel principal
  - `nueva_tarea.html` - Formulario para crear tarea
  - `editar_tarea.html` - Formulario para editar tarea
  - `usuarios.html` - Gestión de usuarios (admin)
  - `nuevo_usuario.html` - Formulario para crear usuario

- `static/` - Archivos estáticos
  - `css/style.css` - Estilos CSS
  - `js/main.js` - JavaScript del frontend

### Documentación
- `README.md` - Documentación principal del proyecto
- `ENDPOINTS_IA.md` - Documentación completa de los endpoints de IA
- `SETUP_OLLAMA.md` - Guía de instalación y configuración de Ollama

## Archivos Generados (no incluidos en repositorio)

- `instance/tareas.db` - Base de datos SQLite (se crea automáticamente)
- `__pycache__/` - Archivos compilados de Python (se generan automáticamente)
- `venv/` - Entorno virtual (no debe incluirse en el repositorio)

## Instalación y Ejecución

1. Instalar dependencias: `pip install -r requirements.txt`
2. Configurar Ollama: Ver `SETUP_OLLAMA.md`
3. Ejecutar migración (si aplica): `python migrate_db.py`
4. Ejecutar aplicación: `python app.py`
5. Acceder a: `http://localhost:5000`

## Notas

- La base de datos se crea automáticamente al ejecutar `app.py` por primera vez
- Los archivos `.db`, `__pycache__` y `venv/` no deben incluirse en la entrega
- Todos los endpoints de IA requieren que Ollama esté corriendo

