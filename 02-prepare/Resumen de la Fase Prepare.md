# Fase PREPARE

## Objetivo

Descargar y preparar 12 meses de datos de Divvy para analizar diferencias entre usuarios casuales y miembros anuales.

## Datos de Divvy

**Fuente:** Sistema de bicicletas compartidas de Chicago  
**Período:** Nov 2024 - Oct 2025  
**Formato:** ZIP → CSV  
**Total:** ~215 MB de datos

### Archivos a Descargar

| Mes | Archivo | Tamaño |
|-----|---------|--------|
| Nov 2024 | 202411-divvy-tripdata.zip | 13.83 MB |
| Dec 2024 | 202412-divvy-tripdata.zip | 6.95 MB |
| Jan 2025 | 202501-divvy-tripdata.zip | 5.77 MB |
| Feb 2025 | 202502-divvy-tripdata.zip | 5.89 MB |
| Mar 2025 | 202503-divvy-tripdata.zip | 11.04 MB |
| Apr 2025 | 202504-divvy-tripdata.zip | 15.07 MB |
| May 2025 | 202505-divvy-tripdata.zip | 20.19 MB |
| Jun 2025 | 202506-divvy-tripdata.zip | 26.78 MB |
| Jul 2025 | 202507-divvy-tripdata.zip | 30.09 MB |
| Aug 2025 | 202508-divvy-tripdata.zip | 28.84 MB |
| Sep 2025 | 202509-divvy-tripdata.zip | 26.18 MB |
| Oct 2025 | 202510-divvy-tripdata.zip | 24.61 MB |

## Estructura de Datos

| Columna | Tipo | Descripción |
|---------|------|-------------|
| TRIP_ID | TEXT | ID único del viaje |
| START_TIME | TIMESTAMP | Fecha/hora inicio |
| STOP_TIME | TIMESTAMP | Fecha/hora fin |
| BIKE_ID | TEXT | ID de la bicicleta |
| TRIP_DURATION | NUMBER | Duración en segundos |
| FROM_STATION_ID | TEXT | ID estación origen |
| FROM_STATION_NAME | TEXT | Nombre estación origen |
| TO_STATION_ID | TEXT | ID estación destino |
| TO_STATION_NAME | TEXT | Nombre estación destino |
| USER_TYPE | TEXT | Member/Single Ride/Day Pass |
| GENDER | TEXT | Solo para miembros |
| BIRTH_YEAR | NUMBER | Solo para miembros |
| FROM_LATITUDE | NUMBER | Latitud origen |
| FROM_LONGITUDE | NUMBER | Longitud origen |
| TO_LATITUDE | NUMBER | Latitud destino |
| TO_LONGITUDE | NUMBER | Longitud destino |

## Herramientas

- **Python:** Análisis estadístico y validación automática
- **R:** Análisis estadístico especializado
- **SQL:** Consultas complejas y agregaciones
- **Excel:** Exploración inicial

## Proceso de Preparación

1. **Descarga:** Ejecutar script de descarga
2. **Validación:** Verificar integridad de archivos
3. **Exploración:** Análisis exploratorio inicial (EDA)
4. **Identificación:** Documentar anomalías
5. **Preparación:** Listo para limpieza y procesamiento

## Archivos

- `script descarga archivos.py` - Script de descarga
- `Plan de Descarga de Datos.md` - Plan detallado de descarga
- `Fuentes de Datos y Evaluación de la Calidad.md` - Evaluación de calidad
- `Metodología de Análisis.md` - Metodología completa

---

**Nota:** Los datos raw NO se incluyen en GitHub por su tamaño. Solo scripts y datasets procesados.
