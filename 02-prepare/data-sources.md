# Data Sources & Quality Assessment

## 📊 Fuentes de Datos Identificadas

### Fuente Principal
**Divvy Trip Data** - Sistema de bicicletas compartidas de Chicago  
**URL:** https://divvy-tripdata.s3.amazonaws.com/index.html  
**Licencia:** Public data made available by Motivate International Inc.

### Cobertura Temporal
**Opción A - Dataset Completo:** 12 meses recientes (2024-2025)  
**Opción B - Dataset Ligero:** Q1 2019 + Q1 2020 (Recomendado para R/Python)

*Nota: El caso sugiere usar los últimos 12 meses para análisis más robusto*

### Estructura de Datos Esperada
```
ride_id                    | STRING  | ID único del viaje
rideable_type             | STRING  | Tipo de bicicleta (classic, docked, electric)
started_at                | DATETIME| Fecha/hora inicio
ended_at                  | DATETIME| Fecha/hora fin
start_station_name        | STRING  | Nombre estación inicio
start_station_id          | STRING  | ID estación inicio
end_station_name          | STRING  | Nombre estación fin
end_station_id            | STRING  | ID estación fin
start_lat                 | FLOAT   | Latitud inicio
start_lng                 | FLOAT   | Longitud inicio
end_lat                   | FLOAT   | Latitud fin
end_lng                   | FLOAT   | Longitud fin
member_casual            | STRING  | Tipo de usuario (member/casual)
```

## 🔍 Evaluación de Calidad de Datos

### Completeness (Completitud)
**Objetivo:** >95% de campos críticos poblados

**Campos Críticos:**
- `started_at`, `ended_at` (100% requerido)
- `member_casual` (100% requerido)
- `start_station_id`, `end_station_id` (>90% esperado)

### Accuracy (Exactitud)
**Validaciones Planeadas:**
- `started_at` < `ended_at` (no viajes hacia atrás)
- Duración de viaje: 1 minuto < tiempo < 24 horas
- Coordenadas válidas: Chicago metro area bounds
- Stations existentes: matching con master station list

### Consistency (Consistencia)
**Consistencia Temporal:**
- Formato datetime estándar (ISO 8601)
- Zona horaria consistente (America/Chicago)
- Fechas dentro del rango esperado

**Consistencia de Categorías:**
- `member_casual`: solo valores "member" o "casual"
- `rideable_type`: valores estándar de Cyclistic
- Station IDs: formato y longitud consistente

### Bias Assessment
**Fuentes Potenciales de Sesgo:**
1. **Temporal:** Datos pueden excluir días de mantenimiento/inactividad
2. **Demográfico:** Usuarios pueden no representar toda la población de Chicago
3. **Sazonal:** Datos de un año específico pueden no ser representativos
4. **Tecnológico:** Cambios en app/UX pueden afectar patrones

**Mitigaciones:**
- Validación con períodos múltiples si es posible
- Comparación con benchmarks de industria
- Documentación de limitaciones

## 📁 Plan de Organización de Datos

### Raw Data Storage
```
/data/raw/
├── divvy_2024_01.csv
├── divvy_2024_02.csv
├── ...
├── divvy_2025_01.csv
└── stations_master.csv
```

### Processed Data Storage
```
/data/processed/
├── monthly_cleaned/
│   ├── clean_2024_01.csv
│   ├── clean_2024_02.csv
│   └── ...
├── combined_full_year.csv
└── derived_variables/
    ├── ride_length.csv
    ├── day_of_week.csv
    └── seasonality_flags.csv
```

### Final Dataset
```
/data/final/
├── analysis_ready.csv
├── segment_analysis.csv
└── validation_sample.csv
```

## 🛠️ Herramientas de Evaluación

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

## 📋 Checklist de Validación

### Pre-Processing Checklist
- [ ] Descarga de todos los archivos de datos
- [ ] Verificación de integridad de archivos (size, format)
- [ ] Exploración inicial de estructura y rangos
- [ ] Identificación de valores nulos y outliers
- [ ] Validación de consistencia entre archivos
- [ ] Creación de master station list
- [ ] Backup de datos originales

### Processing Checklist
- [ ] Aplicación de filtros de calidad
- [ ] Creación de variables derivadas
- [ ] Validación de transformaciones
- [ ] Documentación de cambios realizados
- [ ] Export para análisis

## 🔒 Consideraciones de Privacidad

### Datos NO Disponibles (Por Diseño)
- Información personal identificable (PII)
- Datos de pago o transacciones
- Información demográfica personal
- Historial individual de viajes

### Datos Limitados
- Solo viajes totales, no comportamiento individual
- Sin conexión entre viajes del mismo usuario
- Agregación por station, no por usuario

### Compliance
- ✅ Uso conforme a licencia de datos
- ✅ No PII utilizada en análisis
- ✅ Metodología transparente
- ✅ Resultados agregados y anonimizados

---

**Última Actualización:** 2025-11-14  
**Próximo Paso:** Descarga y exploración inicial de datos  
**Responsable:** Fase 02-prepare/