import pandas as pd
import os

# Simula bucket cloud (carpeta local como S3)
bucket = 'mi-bucket'
os.makedirs(bucket, exist_ok=True)

# Generar y "subir" datos
df = pd.DataFrame({'id': [1,2,3], 'valor': [10,20,30]})
file_path = os.path.join(bucket, 'datos.csv')
df.to_csv(file_path, index=False)

# Integración: Leer de "cloud" y analizar
df_cloud = pd.read_csv(file_path)
print(df_cloud.describe())  # Análisis estadístico

print("Reflexión: Simulé integración cloud, usando storage local como proxy para S3. En producción, usaría boto3; esto muestra escalabilidad para datos distribuidos.")
