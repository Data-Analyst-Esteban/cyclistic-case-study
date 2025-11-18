# Fuentes de Datos y Evaluación de la Calidad

## Fuente Principal

**Divvy Trip Data** - Sistema de bicicletas compartidas de Chicago  
**URL Oficial:** <https://divvybikes.com/system-data>  
**Descarga Directa:** <https://divvy-tripdata.s3.amazonaws.com/index.html>  
**Licencia:** Public data made available by Motivate International Inc.

### Dataset

**Dataset Seleccionado:** 12 meses recientes (Nov 2024 - Oct 2025)  
**Última actualización:** Noviembre 2025  
**Formato:** ZIP

**Archivos Disponibles (Nov 2024 - Oct 2025):**

- 202411-divvy-tripdata.zip (13.83 MB)
- 202412-divvy-tripdata.zip (6.95 MB)
- 202501-divvy-tripdata.zip (5.77 MB)
- 202502-divvy-tripdata.zip (5.89 MB)
- 202503-divvy-tripdata.zip (11.04 MB)
- 202504-divvy-tripdata.zip (15.07 MB)
- 202505-divvy-tripdata.zip (20.19 MB)
- 202506-divvy-tripdata.zip (26.78 MB)
- 202507-divvy-tripdata.zip (30.09 MB)
- 202508-divvy-tripdata.zip (28.84 MB)
- 202509-divvy-tripdata.zip (26.18 MB)
- 202510-divvy-tripdata.zip (24.61 MB)

**Total estimado:** ~215 MB de datos originales

### Estructura de los Datos

Column Name           | Type        | Description
---------------------|-------------|------------------------------------------
TRIP_ID              | TEXT        | ID único del viaje
START_TIME           | TIMESTAMP   | Fecha/hora inicio del viaje
STOP_TIME            | TIMESTAMP   | Fecha/hora fin del viaje  
BIKE_ID              | TEXT        | ID único de la bicicleta
TRIP_DURATION        | NUMBER      | Duración del viaje en segundos
FROM_STATION_ID      | TEXT        | ID estación de origen
FROM_STATION_NAME    | TEXT        | Nombre estación de origen
TO_STATION_ID        | TEXT        | ID estación destino
TO_STATION_NAME      | TEXT        | Nombre estación destino
USER_TYPE            | TEXT        | Tipo de usuario (Member/Single Ride/Day Pass)
GENDER               | TEXT        | Género (solo para miembros)
BIRTH_YEAR           | NUMBER      | Año de nacimiento (solo para miembros)
FROM_LATITUDE        | NUMBER      | Latitud origen
FROM_LONGITUDE       | NUMBER      | Longitud origen  
FROM_LOCATION        | POINT       | Coordenadas origen (formato POINT)
TO_LATITUDE          | NUMBER      | Latitud destino (inferida)
TO_LONGITUDE         | NUMBER      | Longitud destino (inferida)
TO_LOCATION          | POINT       | Coordenadas destino (inferida)

**Fuentes Potenciales de Sesgo:**

1. **Temporal:** Datos pueden excluir días de mantenimiento/inactividad
2. **Demográfico:** Usuarios pueden no representar toda la población de Chicago
3. **Sazonal:** Datos de un año específico pueden no ser representativos
4. **Tecnológico:** Cambios en app/UX pueden afectar patrones

## Herramientas de Evaluación

### Excel/Google Sheets

**Uso:** Exploración inicial, validación básica
**Limitaciones:** <1M rows, limitadas funciones estadísticas

### SQL

**Uso:** Consultas complejas, agregaciones grandes volúmenes
**Herramientas:** BigQuery, PostgreSQL, SQLite
**Ventajas:** Rendimiento optimizado, consultas complejas

### Python

**Uso:** Análisis estadístico avanzado, validación automática
**Librerías:** Pandas (limpieza), NumPy (métricas), SciPy (tests estadísticos)

### R

**Uso:** Análisis estadístico especializado
**Librerías:** dplyr (manipulación), ggplot2 (visualización), statsmodels

## Proceso

- Descarga de todos los archivos de datos
- Verificación de integridad de archivos (size, format)
- Exploración inicial de estructura y rangos
- Identificación de valores nulos y outliers
- Validación de consistencia entre archivos
- Creación de master station list
- Backup de datos originales
