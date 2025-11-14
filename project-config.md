# Project Configuration

## 🔧 Configuración del Proyecto Cyclistic

**Versión:** 1.0  
**Fecha de Creación:** 2025-11-14  
**Mantenido por:** Data Analytics Team  

## 📁 Estructura de Directorios

```bash
cyclistic-case-study/
├── README.md                           # Presentación principal
├── 01-ask/                             # Fase 1: Business Problem
├── 02-prepare/                         # Fase 2: Data Preparation
├── 03-process/                         # Fase 3: Data Processing
├── 04-analyze/                         # Fase 4: Analysis
├── 05-share/                           # Fase 5: Visualization & Sharing
├── 06-act/                             # Fase 6: Action & Recommendations
└── data/                               # Datasets
    ├── raw/                           # Datos originales
    ├── processed/                     # Datos procesados
    └── final/                         # Dataset para análisis
```

## 🛠️ Configuración de Herramientas

### Python Environment
**Versiones Recomendadas:**
- Python: 3.8+
- Pandas: 1.3+
- NumPy: 1.21+
- Matplotlib: 3.4+
- Seaborn: 0.11+
- Scikit-learn: 1.0+
- SciPy: 1.7+

**Librerías Adicionales:**
```txt
jupyter>=1.0.0
plotly>=5.0.0
folium>=0.12.0
```

### Excel/SQL Setup
- **Excel 2016+** o **Google Sheets**
- **SQL Editor:** BigQuery, PostgreSQL, o SQLite
- **ODBC Driver:** Para conexión con bases de datos

### Tableau/Power BI
- **Tableau Desktop:** Latest version
- **Power BI Desktop:** Latest version
- **Conectores:** CSV, Excel, PostgreSQL

## 📊 Nomenclatura de Archivos

### Datos
```
raw_data/
├── divvy_2024_01.csv
├── divvy_2024_02.csv
└── ...

processed_data/
├── clean_monthly_2024_01.csv
├── clean_monthly_2024_02.csv
├── combined_year_2024.csv
└── final_analysis_dataset.csv
```

### Análisis
```
analysis_notebooks/
├── 01_exploratory_analysis.ipynb
├── 02_segmentation_analysis.ipynb
├── 03_statistical_validation.ipynb
└── 04_insights_generation.ipynb
```

### Visualizaciones
```
visualizations/
├── dashboards/
├── static_charts/
└── interactive_maps/
```

## 🔧 Scripts y Automatización

### Python Scripts
```python
# scripts/
├── data_loader.py          # Carga y valida datos
├── data_cleaner.py         # Limpieza y transformación
├── segmentation.py         # Clustering y segmentación
├── statistical_tests.py    # Tests estadísticos
└── report_generator.py     # Generación de reportes
```

### SQL Queries
```sql
-- queries/
├── exploration/
│   ├── basic_stats.sql
│   └── data_quality.sql
├── analysis/
│   ├── user_behavior.sql
│   └── seasonal_patterns.sql
└── reporting/
    ├── summary_metrics.sql
    └── segment_profiles.sql
```

## 📝 Estándares de Documentación

### Naming Conventions
- **Archivos:** snake_case (ej: `data_cleaning_documentation.md`)
- **Variables:** camelCase (ej: `memberCasual`)
- **Funciones:** snake_case (ej: `calculate_ride_length()`)
- **Clases:** PascalCase (ej: `UserSegmentation`)

### Comment Standards
```python
def calculate_ride_length(start_time, end_time):
    """
    Calculate ride duration in minutes.
    
    Args:
        start_time (datetime): Trip start timestamp
        end_time (datetime): Trip end timestamp
    
    Returns:
        float: Duration in minutes
    
    Raises:
        ValueError: If start_time >= end_time
    """
    pass
```

## 🎯 Métricas de Éxito del Proyecto

### Objetivos Técnicos
- **Precisión de limpieza:** >99% de datos válidos
- **Significancia estadística:** p-value < 0.05 en tests clave
- **Separación de segmentos:** Silhouette score > 0.5
- **Cobertura de análisis:** 100% de hipótesis validadas

### Objetivos de Negocio
- **Segmentación:** Mínimo 3 segmentos identificables
- **Insights accionables:** 3+ recomendaciones específicas
- **ROI proyectado:** Cálculo cuantificado por recomendación
- **Adopción por stakeholders:** Aprobación del 90%+ de recomendaciones

## 🚨 Troubleshooting Guide

### Problemas Comunes

#### Data Loading Issues
```
Error: "File not found"
Solution: Verificar ruta de datos y permisos de acceso
```

#### Memory Issues in Python
```
Error: "Out of memory"
Solution: Usar chunking o reducir dataset size
```

#### SQL Performance
```
Error: "Query timeout"
Solution: Index optimization o particionado de datos
```

## 📞 Contactos y Responsabilidades

| Rol | Responsable | Área de Responsabilidad |
|-----|-------------|------------------------|
| **Project Lead** | [Nombre] | Coordinación general |
| **Data Analyst** | [Nombre] | Análisis técnico |
| **Business Analyst** | [Nombre] | Insights de negocio |
| **Visualization Specialist** | [Nombre] | Dashboards y reportes |

---

**Última Actualización:** 2025-11-14  
**Próxima Revisión:** Post-Fase Prepare  
**Owner:** Project Lead