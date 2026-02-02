"""
Servicio de IA para interactuar con Ollama y generar contenido para tareas.
"""

import requests
from typing import Optional
import re


class AIService:
    """Servicio para interactuar con modelos LLM a través de Ollama"""
    
    def __init__(self, model: str = "llama3.2", base_url: str = "http://localhost:11434"):
        """
        Inicializa el servicio de IA
        
        Args:
            model: Nombre del modelo de Ollama a usar (por defecto: llama3.2)
            base_url: URL base de la API de Ollama (por defecto: http://localhost:11434)
        """
        self.model = model
        self.base_url = base_url
        self.api_url = f"{base_url}/api/generate"
    
    def _generate(self, prompt: str) -> str:
        """
        Método interno para generar texto usando Ollama
        
        Args:
            prompt: El prompt a enviar al modelo
            
        Returns:
            str: Respuesta del modelo
        """
        try:
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
            
            response = requests.post(self.api_url, json=payload, timeout=120)
            response.raise_for_status()
            
            result = response.json()
            return result.get('response', '').strip()
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error al conectar con Ollama: {str(e)}")
        except Exception as e:
            raise Exception(f"Error al generar respuesta: {str(e)}")
    
    def generate_description(self, title: str, priority: Optional[str] = None, 
                            assigned_to: Optional[str] = None) -> str:
        """
        Genera una descripción detallada para una tarea basándose en su título y otros campos.
        
        Args:
            title: Título de la tarea
            priority: Prioridad de la tarea (opcional)
            assigned_to: Persona asignada (opcional)
            
        Returns:
            str: Descripción generada
        """
        prompt = f"""Genera una descripción detallada y profesional para la siguiente tarea de desarrollo de software.

Título: {title}
{f'Prioridad: {priority}' if priority else ''}
{f'Asignada a: {assigned_to}' if assigned_to else ''}

La descripción debe ser clara, específica y útil para entender qué se necesita hacer. 
Incluye detalles técnicos relevantes si es apropiado. Responde SOLO con la descripción, sin texto adicional."""

        try:
            return self._generate(prompt)
        except Exception as e:
            raise Exception(f"Error al generar descripción: {str(e)}")
    
    def categorize_task(self, title: str, description: Optional[str] = None) -> str:
        """
        Clasifica una tarea en una categoría: Frontend, Backend, Testing, Infra, etc.
        
        Args:
            title: Título de la tarea
            description: Descripción de la tarea (opcional)
            
        Returns:
            str: Categoría de la tarea
        """
        prompt = f"""Clasifica la siguiente tarea de desarrollo de software en una de estas categorías:
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

Título: {title}
{f'Descripción: {description}' if description else ''}

Responde SOLO con el nombre de la categoría, sin texto adicional ni explicaciones."""

        try:
            response_text = self._generate(prompt)
            # Limpiar la respuesta para obtener solo la categoría
            category = re.sub(r'[^a-zA-Z/]', '', response_text)
            # Si contiene múltiples palabras, tomar la primera
            if '/' in category:
                category = category.split('/')[0]
            # Si la respuesta está vacía, devolver "Other"
            if not category:
                category = "Other"
            return category
        except Exception as e:
            raise Exception(f"Error al categorizar tarea: {str(e)}")
    
    def estimate_effort(self, title: str, description: Optional[str] = None, 
                       category: Optional[str] = None) -> float:
        """
        Estima el esfuerzo en horas para completar una tarea.
        
        Args:
            title: Título de la tarea
            description: Descripción de la tarea (opcional)
            category: Categoría de la tarea (opcional)
            
        Returns:
            float: Horas estimadas
        """
        prompt = f"""Estima el esfuerzo en horas necesario para completar la siguiente tarea de desarrollo de software.

Título: {title}
{f'Descripción: {description}' if description else ''}
{f'Categoría: {category}' if category else ''}

Considera la complejidad, el alcance y el tipo de trabajo. 
Responde SOLO con un número decimal (ejemplo: 8.5, 12.0, 3.5), sin texto adicional."""

        try:
            response_text = self._generate(prompt)
            # Extraer número de la respuesta
            # Buscar números decimales en la respuesta
            numbers = re.findall(r'\d+\.?\d*', response_text)
            if numbers:
                return float(numbers[0])
            else:
                # Si no encuentra número, intentar parsear directamente
                try:
                    return float(response_text)
                except:
                    raise Exception("No se pudo extraer un número válido de la respuesta")
        except Exception as e:
            raise Exception(f"Error al estimar esfuerzo: {str(e)}")
    
    def analyze_risks(self, title: str, description: Optional[str] = None, 
                     category: Optional[str] = None, priority: Optional[str] = None,
                     effort_hours: Optional[float] = None) -> str:
        """
        Analiza los riesgos potenciales de una tarea.
        
        Args:
            title: Título de la tarea
            description: Descripción de la tarea (opcional)
            category: Categoría de la tarea (opcional)
            priority: Prioridad de la tarea (opcional)
            effort_hours: Horas estimadas (opcional)
            
        Returns:
            str: Análisis de riesgos
        """
        prompt = f"""Realiza un análisis de riesgos para la siguiente tarea de desarrollo de software.

Título: {title}
{f'Descripción: {description}' if description else ''}
{f'Categoría: {category}' if category else ''}
{f'Prioridad: {priority}' if priority else ''}
{f'Horas estimadas: {effort_hours}' if effort_hours else ''}

Identifica los riesgos potenciales que podrían surgir durante la ejecución de esta tarea.
Considera riesgos técnicos, de tiempo, de recursos, de dependencias, etc.
Proporciona un análisis claro y estructurado. Responde SOLO con el análisis, sin texto adicional."""

        try:
            return self._generate(prompt)
        except Exception as e:
            raise Exception(f"Error al analizar riesgos: {str(e)}")
    
    def generate_mitigation_plan(self, title: str, description: Optional[str] = None,
                                 category: Optional[str] = None, priority: Optional[str] = None,
                                 effort_hours: Optional[float] = None, 
                                 risk_analysis: Optional[str] = None) -> str:
        """
        Genera un plan de mitigación de riesgos para una tarea.
        
        Args:
            title: Título de la tarea
            description: Descripción de la tarea (opcional)
            category: Categoría de la tarea (opcional)
            priority: Prioridad de la tarea (opcional)
            effort_hours: Horas estimadas (opcional)
            risk_analysis: Análisis de riesgos previo (opcional)
            
        Returns:
            str: Plan de mitigación de riesgos
        """
        prompt = f"""Genera un plan de mitigación de riesgos para la siguiente tarea de desarrollo de software.

Título: {title}
{f'Descripción: {description}' if description else ''}
{f'Categoría: {category}' if category else ''}
{f'Prioridad: {priority}' if priority else ''}
{f'Horas estimadas: {effort_hours}' if effort_hours else ''}
{f'Análisis de riesgos: {risk_analysis}' if risk_analysis else ''}

Basándote en la información de la tarea y el análisis de riesgos, proporciona un plan detallado 
para mitigar o prevenir los riesgos identificados. Incluye acciones concretas y estrategias.
Responde SOLO con el plan de mitigación, sin texto adicional."""

        try:
            return self._generate(prompt)
        except Exception as e:
            raise Exception(f"Error al generar plan de mitigación: {str(e)}")

