# Endpoints de IA - Documentación

Este documento describe los nuevos endpoints de IA implementados usando Ollama.

## Requisitos Previos

1. **Instalar Ollama**: Descarga e instala Ollama desde [ollama.ai](https://ollama.ai/)
2. **Descargar un modelo**: Ejecuta `ollama pull llama3.2` (o cualquier otro modelo compatible)
3. **Verificar que Ollama esté corriendo**: La API debe estar disponible en `http://localhost:11434`

## Configuración

El servicio de IA está configurado para usar:
- **Modelo por defecto**: `llama3.2`
- **URL base**: `http://localhost:11434`

Para cambiar el modelo, modifica la inicialización en `app.py`:
```python
ai_service = AIService(model="tu-modelo-aqui")
```

## Endpoints Disponibles

Todos los endpoints requieren autenticación (login) y están bajo la ruta `/ai/tasks/`.

### 1. POST /ai/tasks/describe

Genera una descripción detallada para una tarea basándose en su título y otros campos.

**Request Body (JSON):**
```json
{
  "title": "Implementar autenticación JWT",
  "priority": "alta",
  "assigned_to": "Juan Pérez"
}
```

**Respuesta (200):**
```json
{
  "title": "Implementar autenticación JWT",
  "description": "Implementar un sistema de autenticación basado en tokens JWT...",
  "priority": "alta",
  "assigned_to": "Juan Pérez"
}
```

**Ejemplo con cURL:**
```bash
curl -X POST http://localhost:5000/ai/tasks/describe \
  -H "Content-Type: application/json" \
  -H "Cookie: session=<tu-sesion>" \
  -d '{
    "title": "Implementar autenticación JWT",
    "priority": "alta"
  }'
```

### 2. POST /ai/tasks/categorize

Clasifica una tarea en una categoría (Frontend, Backend, Testing, Infra, etc.).

**Request Body (JSON):**
```json
{
  "title": "Crear componente de login",
  "description": "Implementar formulario de login con validación"
}
```

**Respuesta (200):**
```json
{
  "title": "Crear componente de login",
  "description": "Implementar formulario de login con validación",
  "category": "Frontend"
}
```

**Categorías posibles:**
- Frontend
- Backend
- Testing
- Infra
- DevOps
- Database
- API
- UI/UX
- Security
- Documentation
- Other

**Ejemplo con cURL:**
```bash
curl -X POST http://localhost:5000/ai/tasks/categorize \
  -H "Content-Type: application/json" \
  -H "Cookie: session=<tu-sesion>" \
  -d '{
    "title": "Crear componente de login",
    "description": "Implementar formulario de login"
  }'
```

### 3. POST /ai/tasks/estimate

Estima el esfuerzo en horas necesario para completar una tarea.

**Request Body (JSON):**
```json
{
  "title": "Implementar sistema de notificaciones",
  "description": "Crear sistema de notificaciones push para usuarios",
  "category": "Backend"
}
```

**Respuesta (200):**
```json
{
  "title": "Implementar sistema de notificaciones",
  "description": "Crear sistema de notificaciones push para usuarios",
  "category": "Backend",
  "effort_hours": 8.5
}
```

**Ejemplo con cURL:**
```bash
curl -X POST http://localhost:5000/ai/tasks/estimate \
  -H "Content-Type: application/json" \
  -H "Cookie: session=<tu-sesion>" \
  -d '{
    "title": "Implementar sistema de notificaciones",
    "description": "Crear sistema de notificaciones push",
    "category": "Backend"
  }'
```

### 4. POST /ai/tasks/audit

Realiza un análisis de riesgos y genera un plan de mitigación para una tarea.

**Request Body (JSON):**
```json
{
  "title": "Migrar base de datos a PostgreSQL",
  "description": "Migrar datos de SQLite a PostgreSQL",
  "category": "Database",
  "priority": "alta",
  "effort_hours": 16.0
}
```

**Respuesta (200):**
```json
{
  "title": "Migrar base de datos a PostgreSQL",
  "description": "Migrar datos de SQLite a PostgreSQL",
  "category": "Database",
  "priority": "alta",
  "effort_hours": 16.0,
  "risk_analysis": "Análisis detallado de riesgos...",
  "risk_mitigation": "Plan de mitigación detallado..."
}
```

**Nota:** Este endpoint realiza dos llamadas al LLM:
1. Primera llamada: Genera el análisis de riesgos
2. Segunda llamada: Genera el plan de mitigación basado en el análisis

**Ejemplo con cURL:**
```bash
curl -X POST http://localhost:5000/ai/tasks/audit \
  -H "Content-Type: application/json" \
  -H "Cookie: session=<tu-sesion>" \
  -d '{
    "title": "Migrar base de datos a PostgreSQL",
    "description": "Migrar datos de SQLite a PostgreSQL",
    "category": "Database",
    "priority": "alta",
    "effort_hours": 16.0
  }'
```

## Flujo de Trabajo Recomendado

1. **Crear tarea básica**: Usa el endpoint POST `/tasks` con solo el título
2. **Generar descripción**: Usa POST `/ai/tasks/describe` para generar la descripción
3. **Categorizar**: Usa POST `/ai/tasks/categorize` para asignar una categoría
4. **Estimar esfuerzo**: Usa POST `/ai/tasks/estimate` para obtener horas estimadas
5. **Auditar riesgos**: Usa POST `/ai/tasks/audit` para análisis completo de riesgos
6. **Actualizar tarea**: Usa PUT `/tasks/<id>` para guardar todos los campos generados

## Manejo de Errores

Todos los endpoints devuelven errores en el siguiente formato:

```json
{
  "error": "Mensaje de error descriptivo"
}
```

**Códigos de estado HTTP:**
- `200`: Éxito
- `400`: Error en la solicitud (campos requeridos faltantes)
- `403`: Sin permisos
- `500`: Error del servidor (problemas con Ollama, etc.)

## Solución de Problemas

### Error: "Error al conectar con Ollama"
- Verifica que Ollama esté corriendo: `ollama list`
- Verifica que el puerto 11434 esté disponible
- Verifica la URL en la configuración del servicio

### Error: "Model not found"
- Descarga el modelo: `ollama pull llama3.2`
- Verifica que el modelo esté disponible: `ollama list`
- Ajusta el nombre del modelo en la configuración

### Respuestas lentas
- Los modelos más grandes pueden tardar más
- Considera usar modelos más pequeños para desarrollo
- Aumenta el timeout en el servicio si es necesario

## Notas

- Los endpoints de IA no guardan automáticamente en la base de datos
- Debes usar los endpoints CRUD estándar para persistir los datos
- Los prompts están optimizados para español, pero funcionan con inglés también
- El modelo por defecto es `llama3.2`, pero puedes usar cualquier modelo compatible con Ollama

