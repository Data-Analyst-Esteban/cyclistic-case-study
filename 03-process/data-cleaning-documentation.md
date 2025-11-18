# Data Cleaning Documentation

## 🧹 Documentación de Limpieza de Datos

**Fecha de Inicio:** 2025-11-14  
**Status:** 🔄 EN PROGRESO  

## 📋 Checklist de Limpieza

### Validaciones Iniciales
- [ ] **Completeness Check**
  - [ ] Count total de registros por archivo
  - [ ] Porcentaje de valores nulos por columna
  - [ ] Identificación de columnas críticas faltantes

- [ ] **Accuracy Check**
  - [ ] Validación de rangos de fechas
  - [ ] Verificación de coordenadas geográficas
  - [ ] Validación de tipos de usuario (member/casual)

- [ ] **Consistency Check**
  - [ ] Formato de fechas consistente
  - [ ] Códigos de estaciones válidos
  - [ ] Tipos de bicicleta reconocidos

### Transformaciones Realizadas

#### Variables Derivadas
- [ ] **ride_length**: Diferencia entre ended_at y started_at
- [ ] **day_of_week**: Día de la semana que inició el viaje (1=Domingo, 7=Sábado)
- [ ] **hour_of_day**: Hora del inicio del viaje
- [ ] **month**: Mes del viaje
- [ ] **season**: Estación del año (Winter, Spring, Summer, Fall)

#### Filtros Aplicados
- [ ] **Duration Filter**: Eliminar viajes < 1 minuto y > 24 horas
- [ ] **Geographic Filter**: Mantener solo viajes dentro de Chicago metro
- [ ] **Complete Records**: Eliminar viajes con información crítica faltante
- [ ] **Duplicate Check**: Identificar y manejar registros duplicados

#### Calidad de Datos por Archivo
```
Archivo: [FECHA].csv
├─ Total registros: [NÚMERO]
├─ Registros válidos: [NÚMERO] ([PORCENTAJE]%)
├─ Registros filtrados: [NÚMERO] ([PORCENTAJE]%)
└─ Campos con nulls: [LISTA DE CAMPOS]
```

## 🔍 Detalles de Transformaciones

### [PENDIENTE - A COMPLETAR DURANTE LIMPIEZA]

### ride_length Calculation
```python
# Pseudocódigo para documentación
ride_length = ended_at - started_at
Formato: HH:MM:SS (pueden usar duración en minutos para análisis)
```

### day_of_week Calculation  
```python
# Pseudocódigo para documentación
day_of_week = WEEKDAY(started_at, 1)
# Donde 1 = Domingo, 2 = Lunes, ..., 7 = Sábado
```

### Geographic Validation
```python
# Bordes aproximados de Chicago
Latitude bounds: 41.6 - 42.1
Longitude bounds: -87.9 - -87.5
```

## 📊 Métricas de Calidad Final

### Completeness Metrics
```
Campo                | Porcentaje Completo
--------------------|--------------------
ride_id             | [PORCENTAJE]%
member_casual       | [PORCENTAJE]%
started_at          | [PORCENTAJE]%
ended_at            | [PORCENTAJE]%
start_station_id    | [PORCENTAJE]%
end_station_id      | [PORCENTAJE]%
rideable_type       | [PORCENTAJE]%
```

### Outliers Identificados
- **Duración extrema mínima:** [VALOR] minutos
- **Duración extrema máxima:** [VALOR] minutos
- **Viajes con coordenadas inválidas:** [NÚMERO]
- **Registros duplicados:** [NÚMERO]

## 🗂️ Archivos de Salida

### Datos Limpios por Mes
```
/data/processed/monthly_cleaned/
├── clean_2024_01.csv
├── clean_2024_02.csv
├── ...
└── clean_2025_01.csv
```

### Dataset Combinado
```
/data/processed/combined_full_year.csv
├── Estructura: [DESCRIPCIÓN]
├── Registros totales: [NÚMERO]
├── Periodo: [FECHAS]
└── Calidad: [DESCRIPCIÓN]
```

### Variables Derivadas
```
/data/processed/derived_variables/
├── ride_length.csv
├── day_of_week.csv
├── seasonality_flags.csv
└── geographic_validation.csv
```

## ✅ Validación Final

### Data Integrity Check
- [ ] **Total de registros** = Suma de archivos individuales
- [ ] **Distribución temporal** = Distribución esperada por mes
- [ ] **Distribución de usuario** = Ratio member/casual razonable
- [ ] **Completitud de campos** = >95% en campos críticos

### Statistical Validation
- [ ] **Duración promedio** dentro de rangos esperados
- [ ] **Distribución geográfica** dentro de límites de Chicago
- [ ] **Patrones temporales** consistentes con behavior esperado

---

**Responsable:** Data Processing Team  
**Próxima Revisión:** Post-cleaning completión  
**Estado Actual:** Template preparado para completar