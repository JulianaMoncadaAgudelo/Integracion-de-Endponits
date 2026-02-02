# Configuración de Ollama

Esta guía te ayudará a configurar Ollama para usar los endpoints de IA del proyecto.

## 1. Instalación de Ollama

### Windows
1. Descarga el instalador desde [ollama.ai](https://ollama.ai/download)
2. Ejecuta el instalador y sigue las instrucciones
3. Ollama se iniciará automáticamente como servicio

### Linux/Mac
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

## 2. Verificar Instalación

Abre una terminal y ejecuta:
```bash
ollama --version
```

Si Ollama está instalado correctamente, verás la versión.

## 3. Descargar un Modelo

Ollama necesita un modelo de lenguaje para funcionar. Recomendamos usar uno de estos:

### Modelos Recomendados (de menor a mayor tamaño):

**Para desarrollo rápido (modelos pequeños):**
```bash
ollama pull llama3.2:1b
ollama pull llama3.2:3b
```

**Para mejor calidad (modelos medianos):**
```bash
ollama pull llama3.2
ollama pull mistral
```

**Para máxima calidad (modelos grandes - requieren más RAM):**
```bash
ollama pull llama3.1:70b
ollama pull mistral-nemo
```

### Verificar Modelos Descargados
```bash
ollama list
```

## 4. Probar Ollama

Prueba que Ollama funciona correctamente:
```bash
ollama run llama3.2
```

Deberías ver un prompt interactivo. Escribe algo y presiona Enter. Para salir, escribe `/bye`.

## 5. Verificar que la API está Funcionando

La API de Ollama debe estar disponible en `http://localhost:11434`.

Puedes probarla con:
```bash
curl http://localhost:11434/api/tags
```

O desde Python:
```python
import requests
response = requests.get('http://localhost:11434/api/tags')
print(response.json())
```

## 6. Configurar el Modelo en la Aplicación

Por defecto, la aplicación usa el modelo `llama3.2`. Si quieres usar otro modelo, edita `app.py`:

```python
# Busca esta línea:
ai_service = AIService()

# Cámbiala por:
ai_service = AIService(model="tu-modelo-aqui")
```

Por ejemplo:
```python
ai_service = AIService(model="mistral")
```

## 7. Solución de Problemas

### Ollama no inicia
- **Windows**: Verifica que el servicio de Ollama esté corriendo en el Administrador de Tareas
- **Linux/Mac**: Ejecuta `ollama serve` manualmente

### Error "Connection refused"
- Verifica que Ollama esté corriendo: `ollama list`
- Verifica que el puerto 11434 no esté bloqueado por un firewall
- Intenta reiniciar Ollama

### Modelo no encontrado
- Verifica que el modelo esté descargado: `ollama list`
- Si no está, descárgalo: `ollama pull nombre-del-modelo`
- Verifica que el nombre del modelo en `app.py` coincida exactamente

### Respuestas muy lentas
- Los modelos más grandes requieren más RAM y tiempo
- Considera usar un modelo más pequeño para desarrollo
- Cierra otras aplicaciones que usen mucha memoria

### Error de memoria
- Los modelos grandes requieren mucha RAM
- Usa un modelo más pequeño o aumenta la RAM disponible
- En Windows, verifica la memoria disponible en el Administrador de Tareas

## 8. Recursos Adicionales

- [Documentación oficial de Ollama](https://github.com/ollama/ollama)
- [Lista de modelos disponibles](https://ollama.ai/library)
- [API Reference](https://github.com/ollama/ollama/blob/main/docs/api.md)

## 9. Notas Importantes

- Ollama debe estar corriendo antes de usar los endpoints de IA
- El primer uso de un modelo puede ser más lento (carga en memoria)
- Los modelos se descargan en `~/.ollama/models` (pueden ocupar varios GB)
- Para producción, considera usar Ollama Cloud o un servidor dedicado

