# Plan de Descarga de Datos

## Objetivo

Descargar y procesar 12 meses de datos de viajes de Divvy (Nov 2024 - Oct 2025) para análisis de comportamiento de usuarios casual vs member.

## Archivos a Descargar

### Dataset Completo (Nov 2024 - Oct 2025)

**Base URL:** `https://divvy-tripdata.s3.amazonaws.com/`

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

**Total:** 215.44 MB de datos ZIP comprimidos

## Limitaciones de Privacidad

1. **Datos Personales:** Solo para suscriptores (miembros)
   - GENDER: disponible solo para usuarios registrados
   - BIRTH_YEAR: disponible solo para usuarios registrados

2. **Anonimización:**
   - No hay información personal identificable
   - IDs de viaje anonimizados
   - No hay información de tarjetas de crédito o pagos

## Pasos

1. Ejecutar script de descarga
2. Validar integridad de datos
3. Comenzar análisis exploratorio (EDA)
4. Identificar y documentar anomalías
5. Proceder con limpieza y procesamiento

---

**Nota:** Los datos raw NO se incluirán en el repositorio de GitHub debido a su tamaño. Solo se incluirán scripts y datasets procesados/manipulados.
