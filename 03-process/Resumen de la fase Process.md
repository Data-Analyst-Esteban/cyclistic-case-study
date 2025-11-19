# Fase PROCESS

## Objetivo

Limpiar, validar y preparar datos de Divvy para análisis, siguiendo metodología del caso de estudio Cyclistic.

## Resultados

- **Registros procesados:** 5,563,698 registros válidos
- **Tasa de retención:** 99.9% (solo 5,581 registros filtrados, 0.1%)
- **Duración promedio:** 14.5 minutos por viaje
- **Período cubierto:** Nov 2024 - Oct 2025 (12 meses)
- **Archivos procesados:** 12 archivos ZIP mensuales

**Archivo de salida:** `cyclistic_clean_data.csv` ubicado en `data/processed/`

## Datos de Entrada

**Fuente:** 12 archivos ZIP descargados en fase PREPARE  
**Ubicación:** `cyclistic-case-study/data/raw/`  
**Período:** Nov 2024 - Oct 2025

## Herramientas Utilizadas

- **excel y power query:** manipulacion y screaning superficial de los datos
- **Python + Pandas:** Limpieza automática y validación
- **Script personalizado:** `clean_cyclistic_data.py`

## Proceso de Limpieza

### Paso 1: Verificación de Integridad

- Verificados archivos descargados (12/12 disponibles)
- Validada estructura CSV
- Identificados errores y datos corruptos

### Paso 2: Organización de Archivos

03-process/
├── data/
│   ├── raw/          # ZIPs originales
│   ├── extracted/    # CSV extraídos
│   └── processed/    # Datos procesados
└── scripts/          # Scripts de limpieza

### Paso 3: Columnas Calculadas Creadas

- **ride_length:** duración del viaje (ended_at - started_at)
- **day_of_week:** día de la semana del viaje (1=Domingo, 7=Sábado)
- **day_name:** nombre del día de la semana

### Paso 4: Limpieza de Datos

- Removidos registros inválidos (timestamps nulos, duraciones negativas)
- Validadas fechas y horas
- Verificadas coordenadas geográficas
- Consolidados tipos de usuario

### Paso 5: Documentación Completa

- Creado reporte de estadísticas formales (`Reporte de estadísticas.md`)
- Documentada metodología completa (`Metodologia de limpieza.md`)
- Script de limpieza versionado (`clean_cyclistic_data.py`)

## Métricas

| Métrica | Valor |
|---------|-------|
| **Total de registros** | 5,563,698 |
| **Registros válidos** | 5,563,698 (99.9%) |
| **Registros filtrados** | 5,581 (0.1%) |
| **Duración promedio** | 14.5 minutos |
| **Tiempo de procesamiento** | 14.5 minutos |
