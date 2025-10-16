# ☁️ Proyecto 4: Simulación de Integración en Cloud

## Descripción
Este proyecto simula un flujo típico de **almacenamiento e integración de datos en la nube**. Se utiliza una carpeta local como proxy de un **bucket de AWS S3** para demostrar cómo los datos se almacenan, recuperan y procesan en entornos cloud. Aunque es una simulación, refleja los patrones fundamentales de arquitecturas de datos modernas, donde el almacenamiento distribuido y la integración eficiente son clave para la escalabilidad.

## Objetivos
- Simular un entorno de almacenamiento en la nube (como AWS S3) utilizando recursos locales.
- Integrar datos desde el "cloud" simulado para su posterior análisis.
- Demostrar comprensión de los flujos de datos en arquitecturas cloud, aplicables a pipelines reales de ingeniería de datos.
- Preparar una base conceptual para la transición a servicios cloud reales (como `boto3` con AWS).

## Tecnologías
- **Python**: Lenguaje principal para la simulación del flujo.
- **pandas**: Para la generación, manipulación y análisis estadístico de los datos.
- **os**: Para la creación y gestión de la estructura de carpetas que simula un bucket en la nube.
