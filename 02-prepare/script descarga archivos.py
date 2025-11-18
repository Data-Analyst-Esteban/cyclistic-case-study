"""
Script: Descarga - Datos Divvy
Autor: Esteban Alonso Molina Morales
Descripción: Este script descarga archivos de datos de Divvy desde una URL específica y los guarda en un directorio local. Maneja errores de descarga y proporciona retroalimentación sobre el progreso.
"""

import requests
from pathlib import Path
import time

# Lista de archivos a descargar
files = [
    "202411-divvy-tripdata.zip",
    "202412-divvy-tripdata.zip",
    "202501-divvy-tripdata.zip",
    "202502-divvy-tripdata.zip",
    "202503-divvy-tripdata.zip",
    "202504-divvy-tripdata.zip",
    "202505-divvy-tripdata.zip",
    "202506-divvy-tripdata.zip",
    "202507-divvy-tripdata.zip",
    "202508-divvy-tripdata.zip",
    "202509-divvy-tripdata.zip",
    "202510-divvy-tripdata.zip"
]

base_url = "https://divvy-tripdata.s3.amazonaws.com/"
output_dir = Path("cyclistic-case-study/data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

successful = 0
for filename in files:
    url = base_url + filename
    output_path = output_dir / filename
    
    try:
        print(f"Descargando {filename}...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        size = output_path.stat().st_size / (1024 * 1024)
        print(f"OK: {filename} ({size:.2f} MB)")
        successful += 1
        
    except Exception as e:
        print(f"ERROR: {filename} - {e}")
    
    time.sleep(1)  # Pausa entre descargas

print(f"Descarga completada: {successful}/{len(files)} archivos")