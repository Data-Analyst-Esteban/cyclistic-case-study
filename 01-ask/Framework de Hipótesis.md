# 🔬 Framework de Hipótesis

### Hipótesis Principal
**H₀ (Nula):** Los miembros anuales y usuarios casuales usan Cyclistic de manera indistinguible en términos de patrones temporales, frecuencia y duración de viajes.

**H₁ (Alternativa):** Existen diferencias significativas y medibles en los patrones de uso entre miembros anuales y usuarios casuales que revelan oportunidades específicas de conversión.

### Hipótesis Específicas por Dimensión

## 📅 Dimensión Temporal

### Hipótesis 1.1: Patrones de Uso por Día de Semana
**H₁₁:** Los usuarios casuales utilizan Cyclistic principalmente durante fines de semana (sábado-domingo) para actividades recreativas, mientras que los miembros anuales muestran patrones más consistentes durante días laborables.

**Evidencia Esperada:**
- Casual users: 60-70% viajes fines de semana
- Annual members: 60-70% viajes días laborables
- Diferencia estadísticamente significativa (p < 0.05)

**Implicaciones de Negocio:**
- Campañas de "weekend membership" para casuales
- Targeteo basado en patrones de uso temporal

### Hipótesis 1.2: Estacionalidad
**H₁₂:** Los usuarios casuales muestran mayor variabilidad estacional con picos en meses de verano, mientras que los miembros anuales mantienen uso más consistente durante todo el año.

**Evidencia Esperada:**
- Casual users: Coeficiente de variación estacional > 0.3
- Annual members: Coeficiente de variación estacional < 0.2
- Peak en mayo-agosto para casuales

**Implicaciones de Negocio:**
- Promociones estacionales antes del peak
- Membresías "temporada de verano"

## ⏱️ Dimensión de Duración

### Hipótesis 2.1: Tiempo Promedio de Viaje
**H₁₃:** Los usuarios casuales realizan viajes de mayor duración promedio, mientras que los miembros anuales usan Cyclistic para trayectos más cortos y eficientes.

**Evidencia Esperada:**
- Casual users: Duración promedio > 25 minutos
- Annual members: Duración promedio < 20 minutos
- Diferencia estadísticamente significativa

**Implicaciones de Negocio:**
- Posicionamiento de membresía como "ahorro en transporte frecuente"
- Promociones para usuarios de viajes largos regulares

## 🚦 Dimensión de Frecuencia

### Hipótesis 3.1: Número de Viajes por Usuario
**H₁₄:** Los miembros anuales generan significativamente más viajes por usuario que los casuales, indicando patrones de uso más frecuentes y sistemáticos.

**Evidencia Esperada:**
- Annual members: >20 viajes por usuario/año
- Casual users: <5 viajes por usuario/año
- Ratio mínimo de 4:1

**Implicaciones de Negocio:**
- Lifetime value diferencia significativa
- Estrategias de retención diferenciadas

## 📍 Dimensión Geográfica

### Hipótesis 4.1: Patrones de Estaciones
**H₁₅:** Los usuarios casuales prefieren estaciones en zonas turísticas/recreativas, mientras que los miembros anuales utilizan estaciones en áreas residenciales/comerciales.

**Evidencia Esperada:**
- Casual: Alta concentración en áreas recreativas
- Members: Distribución más homogénea, mayor densidad en zonas laborales

**Implicaciones de Negocio:**
- Targeteo geográfico para campañas
- Instalaciones estratégicas para conversión

## 🎯 Segmentación Esperada de Usuarios Casuales

### Segmento A: "Weekend Warriors"
**Características:**
- 70%+ uso en fines de semana
- Duración de viaje variable (30-45 min promedio)
- Estaciones recreativas preferidas

**Estrategia de Conversión:**
- "Weekend Membership" con beneficios específicos
- Pricing orientado a fines de semana

### Segmento B: "Summer Enthusiasts"
**Características:**
- Picos estacionales fuertes (>50% viajes en verano)
- Variación geográfica (estaciones turísticas)
- Duración de viaje más larga

**Estrategia de Conversión:**
- "Seasonal Pass" con flexibilidad anual
- Membresía con beneficios de temporada

### Segmento C: "Commuter Leavers"
**Características:**
- Uso ocasional pero consistente
- Estaciones cerca de transporte público
- Patrones que sugieren interés en movilidad regular

**Estrategia de Conversión:**
- Targeteo en horarios de commuting
- Benefits de conectividad con transporte público

## 📊 Metodología de Validación

### Tests Estadísticos Planificados
1. **T-test:** Para diferencias en duración promedio
2. **Chi-square:** Para distribución por día de semana
3. **ANOVA:** Para diferencias entre múltiples segmentos
4. **Clustering (K-means):** Para identificación de segmentos naturales

### Criterios de Significancia
- **Nivel de confianza:** 95% (α = 0.05)
- **Tamaño de efecto mínimo:** Cohen's d > 0.5 (medium effect)
- **Tamaño de muestra:** n > 30 por grupo para análisis robusto

## 🎯 Resultados Esperados vs Insights Accionables

### Si las Hipótesis se Confirman:
- **Segmentación robusta** con al menos 3 grupos distintos
- **Diferencias estadísticamente significativas** en todas las dimensiones clave
- **Patrones predictivos** para identificar usuarios casuales de alta conversión

### Traducción a Insights de Negocio:
Cada hipótesis confirmada se traducirá en:
1. **Oportunidad de conversión específica**
2. **Propuesta de valor diferenciada**
3. **Canal de marketing recomendado**
4. **ROI proyectado** para esa estrategia

---

**Framework Documentado:** 2025-11-14  
**Próxima Validación:** Post-limpieza de datos  
**Responsable:** Análisis en fase 04-analyze/