# Reporte de Estadísticas - Limpieza de Datos

## Resumen Ejecutivo

Se completó exitosamente el proceso de limpieza de datos para el análisis de patrones de uso entre miembros anuales y usuarios casuales de Cyclistic. El dataset resultante contiene **5,563,698 registros válidos** con una calidad del 99.9% tras la eliminación de 5,581 registros inconsistentes.

## Métricas del Proceso de Limpieza

### **Volumen de Datos**

- **Archivos procesados:** 12 archivos mensuales (ZIP)
- **Registros iniciales:** 5,569,279
- **Registros válidos finales:** 5,563,698
- **Registros filtrados:** 5,581 (0.1%)
- **Tasa de retención:** 99.9%

## Análisis de Duraciones de Viaje

### **Duración Promedio de Viajes**

- **Tiempo promedio:** 14.5 minutos
- **Rango válido:** 1 segundo - 24 horas
- **Registro más corto eliminado:** < 1 segundo
- **Registro más largo eliminado:** > 24 horas

### **Razones de Filtrado de Registros**

1. **Timestamps nulos** (started_at/ended_at faltantes)
2. **Duraciones negativas** (ended_at anterior a started_at)
3. **Duraciones unrealistas** (< 1 segundo o > 24 horas)

## Estructura Final del Dataset

### **Columnas Originales Conservadas**

- ride_id
- rideable_type
- started_at
- ended_at
- start_station_name
- start_station_id
- end_station_name
- end_station_id
- start_lat
- start_lng
- end_lat
- end_lng
- member_casual

### **Columnas Calculadas Agregadas**

- **ride_length:** Duración del viaje en segundos
- **ride_length_formatted:** Duración en formato HH:MM:SS
- **day_of_week:** Día de la semana (1=Domingo, 7=Sábado)
- **day_name:** Nombre del día de la semanas
