# Estadísticas Descriptivas

## Resumen del Dataset

### Información General

- **Dataset**: Cyclistic bike-share data
- **Período**: 2024-10-31 a 2025-10-31 (1 año completo)
- **Total de registros**: 5,421,090 viajes
- **Total de columnas**: 17 columnas validadas
- **Calidad de datos**: Datos limpios, duraciones corregidas exitosamente

### Estructura de Datos

| Columna | Descripción | Tipo |
|---------|-------------|------|
| ride_id | Identificador único del viaje | object |
| rideable_type | Tipo de bicicleta | object |
| started_at | Fecha y hora de inicio | object |
| ended_at | Fecha y hora de fin | object |
| start_station_name | Nombre de estación de inicio | object |
| end_station_name | Nombre de estación de fin | object |
| member_casual | Tipo de usuario (member/casual) | object |
| ride_length | Duración del viaje en minutos | float64 |
| day_of_week | Día de la semana (1=domingo) | int64 |
| day_name | Nombre del día de la semana | object |

---

## Estadísticas Generales

### Duración de Viajes

- **Promedio**: 14.87 minutos
- **Mediana**: 9.66 minutos
- **Mínimo**: 1.00 minutos
- **Máximo**: 1,439.98 minutos (24 horas - filtrado)
- **Desviación estándar**: 28.27 minutos

### Distribución por Tipo de Usuario

- **Member**: 3,499,202 registros (64.5%)
- **Casual**: 1,921,888 registros (35.5%)

### Distribución por Día de la Semana

- **Viernes**: 832,901 registros (15.4%) - Día más activo
- **Jueves**: 831,894 registros (15.3%)
- **Miércoles**: 802,945 registros (14.8%)
- **Lunes**: 773,004 registros (14.3%)
- **Martes**: 745,370 registros (13.7%)
- **Domingo**: 728,327 registros (13.4%)
- **Sábado**: 706,649 registros (13.0%) - Día menos activo

---

## Análisis por Tipo de Usuario

### Member Users

- **Registros**: 3,499,202
- **Porcentaje del total**: 64.5%
- **Duración promedio**: 12.08 minutos
- **Duración mediana**: 8.71 minutos
- **Comportamiento**: Viajes más eficientes, probablemente commuting

### Casual Users

- **Registros**: 1,921,888
- **Porcentaje del total**: 35.5%
- **Duración promedio**: 19.94 minutos
- **Duración mediana**: 11.90 minutos
- **Comportamiento**: Viajes más largos, probablemente recreativos/turísticos

---

## Hallazgos Principales

### Insights Clave

1. **DURACIÓN REAL CONFIRMADA**: Los datos muestran duración promedio de 14.87 minutos, coherente con estándares de bike-sharing (Chicago Divvy: 13.8 min)
2. **PATRÓN DE COMPORTAMIENTO DIFERENCIADO**: Los miembros usan el servicio más frecuentemente (64.5%) pero con viajes más eficientes (12.08 min), sugiriendo uso para commuting
3. **USUARIOS CASUALES CON VIAJES MÁS LARGOS**: Los usuarios casuales (35.5%) tienen viajes 7.86 minutos más largos en promedio (19.94 vs 12.08 min), sugiriendo uso recreativo/turístico
4. **VIERNES COMO DÍA PICO**: Los viernes concentran el mayor volumen de viajes (15.4%), indicando patrones de fin de semana/semana laboral
5. **DATOS VALIDADOS**: Filtrado exitoso de outliers extremos manteniendo 95%+ de los datos, base sólida para análisis estratégico
6. **CALIDAD EMPRESARIAL**: Los datos corregidos son válidos para análisis estratégico y toma de decisiones empresariales

### Comparación Member vs Casual

- **Diferencia en duración**: 7.86 minutos más para usuarios casual (19.94 vs 12.08 min)
- **Patrón de uso predominante**: Members dominan en volumen (64.5% vs 35.5%)
- **Día de mayor uso**: Viernes es el día más activo para ambos tipos de usuario
- **Comportamiento**: Members parecen usar para commuting (viajes eficientes), casuales para recreación (viajes largos)
- **Oportunidad de negocio**: Conversión de casuales a members podría aumentar frecuencia de uso

---

## Conclusiones

### Datos del Análisis

**Hallazgos Clave**:

- **Dataset Completo**: 5.4M registros de un año completo (Oct 2024 - Oct 2025)
- **Duraciones**: 14.87 min promedio, coherentes con bike-sharing urbano
- **Comportamiento Diferenciado**: Members (12.08 min) vs Casual (19.94 min) - diferencia de 7.86 min
- **Patrones Temporales**: Viernes como día pico (15.4% del tráfico semanal)
- **Oportunidad Estratégica**: 35.5% de usuarios casuales como target para conversión
