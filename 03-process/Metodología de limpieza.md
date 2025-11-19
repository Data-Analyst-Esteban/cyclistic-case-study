# Metodología de Limpieza

## Objetivo

Limpiar y preparar datos para análisis, siguiendo recomendaciones del caso de estudio Cyclistic.

## Pasos Ejecutados

### 1. Verificación de Integridad

- Comprobar archivos ZIP descargados (12/12 disponibles)
- Validar estructura CSV de archivos
- Identificar errores y datos corruptos

### 2. Extracción de Datos

- Descomprimir archivos ZIP de datos
- Organizar datos por mes (Nov 2024 - Oct 2025)

### 3. Limpieza Básica

- Remover registros con timestamps nulos
- Filtrar duraciones negativas o inválidas

### 4. Columnas Calculadas (Caso de Estudio)

- **ride_length:** duración del viaje (ended_at - started_at), formato: HH:MM:SS
- **day_of_week:** día de la semana (1=Domingo, 7=Sábado)
- **day_name:** nombre del día

### 5. Consolidación

- Combinar todos los archivos mensuales en dataset único
- Generar estadísticas básicas del dataset limpio

## 🛠️ Herramientas Utilizadas

- **excel**: comprobacion manual de datos y screening superficial
- **Python:** Procesamiento principal
- **Pandas:** Manipulación de datos

## Metodologías Implementadas

### Python Script (Método Principal)

- **Archivo:** `clean_cyclistic_data.py`
- **Resultado:** 5,563,698 registros
- **Tiempo:** 14.5 minutos

### Power Query (Método Alternativo)

- **Proceso:** Excel + Power Query
- **Resultado:** 5,569,279 registros
- **Validación:** Resultados consistentes con Python
- **Aprendizaje:** Competencia en herramientas visuales

## Proceso Paso a Paso

1. **Extraer:** ZIP
2. **Validar:** Datos
3. **Limpiar:** Filtrar registros inválidos
4. **Calcular:** ride_length y day_of_week
5. **Combinar:** Dataset único
6. **Guardar:** cyclistic_clean_data.csv

## Entregables para caso de estudio

- **Dataset limpio:** `data/processed/cyclistic_clean_data.csv`
- **Reporte de estadísticas:** `Reporte de Estadísticas`
- **Script de procesamiento:** `Script de limpieza de datos.py`
- **Proceso documentado:** Este archivo
