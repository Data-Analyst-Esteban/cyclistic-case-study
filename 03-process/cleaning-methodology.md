# Metodología de Limpieza - Cyclistic Case Study

**Autor:** Esteban Alonso Molina Morales  
**Fecha:** 2025-11-19  
**Fase:** 3/6 - PROCESS

## 🎯 Objetivo

Limpiar y preparar datos de Divvy para análisis, siguiendo recomendaciones del caso de estudio Cyclistic.

## 📋 Pasos Ejecutados

### 1. Verificación de Integridad
- Comprobar archivos ZIP descargados (12/12 disponibles)
- Validar estructura CSV de archivos
- Identificar errores y datos corruptos

### 2. Extracción de Datos
- Descomprimir archivos ZIP de datos
- Extraer archivos CSV individuales
- Organizar datos por mes (Nov 2024 - Oct 2025)

### 3. Limpieza Básica
- Remover registros con timestamps nulos
- Filtrar duraciones negativas o inválidas
- Validar rangos de tiempo (1 segundo - 24 horas)
- Consolidar nombres de columnas

### 4. Columnas Calculadas (Caso de Estudio)
- **ride_length:** duración del viaje (ended_at - started_at)
  - Formato: HH:MM:SS (temporal)
  - También en segundos para cálculos
- **day_of_week:** día de la semana (1=Domingo, 7=Sábado)
- **day_name:** nombre del día (Lunes, Martes, etc.)

### 5. Consolidación
- Combinar todos los archivos mensuales en dataset único
- Generar estadísticas básicas del dataset limpio
- Validar distribución de tipos de usuario

## 🛠️ Herramientas Utilizadas

- **Python 3.11:** Procesamiento principal
- **Pandas:** Manipulación de datos
- **Zipfile:** Extracción de archivos
- **Pathlib:** Gestión de archivos

## 📊 Proceso Paso a Paso

1. **Extraer:** ZIP → CSV
2. **Validar:** Estructura y datos
3. **Limpiar:** Filtrar registros inválidos
4. **Calcular:** ride_length y day_of_week
5. **Combinar:** Dataset único
6. **Guardar:** cyclistic_clean_data.csv

## 📝 Entregable

- **Dataset limpio:** `cyclistic_clean_data.csv`
- **Estadísticas básicas:** Reporte en consola
- **Proceso documentado:** Este archivo

## ✅ Validación

- [x] Archivos extraídos sin errores
- [x] Datos validados y limpios
- [x] Columnas calculadas según especificaciones
- [x] Dataset consolidado
- [x] Estadísticas generadas

---

**Nota:** Datos listos para fase de análisis (Phase 4)