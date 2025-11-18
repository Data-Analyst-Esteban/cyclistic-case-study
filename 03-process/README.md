# Fase PROCESS - Cyclistic Case Study

**Autor:** Esteban Alonso Molina Morales  
**Fecha:** 2025-11-19  
**Fase:** 3/6 - PROCESS

## 🎯 Objetivo

Limpiar, validar y preparar datos de Divvy para análisis, siguiendo metodología del caso de estudio Cyclistic.

## 📊 Datos de Entrada

**Fuente:** 12 archivos ZIP descargados en fase PREPARE  
**Ubicación:** `cyclistic-case-study/data/raw/`  
**Período:** Nov 2024 - Oct 2025

## 🔧 Herramientas Recomendadas

- **Python:** Limpieza automática y validación
- **Excel/Google Sheets:** Manipulación manual de datos
- **RStudio:** Para datasets grandes

## 📋 Proceso de Limpieza

### Paso 1: Verificar Integridad
- Comprobar archivos descargados (12/12 disponibles)
- Validar estructura CSV
- Identificar errores y datos corruptos

### Paso 2: Organizar Archivos
```
03-process/
├── data/
│   ├── raw/          # ZIPs originales
│   ├── extracted/    # CSV extraídos
│   └── cleaned/      # Datos procesados
└── scripts/          # Scripts de limpieza
```

### Paso 3: Crear Columnas Calculadas
- **ride_length:** duración del viaje (ended_at - started_at)
- **day_of_week:** día de la semana del viaje (1=Domingo, 7=Sábado)

### Paso 4: Limpiar Datos
- Remover registros inválidos
- Validar fechas y horas
- Verificar coordenadas geográficas
- Consolidar tipos de usuario

## 📋 Checklist de Validación

- [ ] Verificar descarga de archivos
- [ ] Extraer CSVs de archivos ZIP
- [ ] Validar estructura de columnas
- [ ] Crear columna ride_length
- [ ] Crear columna day_of_week
- [ ] Limpiar datos inválidos
- [ ] Documentar proceso de limpieza

## 🚀 Siguiente Fase

**Fase 4:** Análisis - Análisis descriptivo y exploración de datos

## 📝 Documentación

Todo el proceso de limpieza se documenta para:
- Reproducibilidad del análisis
- Validación de resultados
- Transparencia metodológica

---

**Nota:** Los datos limpios se preparan para análisis estadístico en la siguiente fase.