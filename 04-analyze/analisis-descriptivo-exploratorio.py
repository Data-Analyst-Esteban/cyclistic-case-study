"""
Análisis Descriptivo Exploratorio 
Autor: Esteban Alonso Molina Morales
descripción: Este script realiza un análisis descriptivo exploratorio del dataset
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def cargar_datos():
    """
    Cargar y validar el dataset de Cyclistic.
    """
    try:
        print("Cargando datos de Cyclistic...")
        
        # Ruta correcta para tu estructura de carpetas
        ruta_archivo = "cyclistic-case-study\data\processed\cyclistic_clean_data.csv"
        
        df = pd.read_csv(ruta_archivo)
        
        # Validación básica
        print(f"Datos cargados exitosamente: {len(df):,} registros")
        print(f"Período de datos: {df['started_at'].min()} a {df['started_at'].max()}")
        
        return df
        
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en {ruta_archivo}")
        print("Verifica que el archivo esté en: data/processed/")
        return None
    except Exception as e:
        print(f"Error cargando datos: {str(e)}")
        return None

def analizar_estructura_datos(df):
    """
    Analizar la estructura básica del dataset.
    """
    print("\n" + "="*50)
    print("ANÁLISIS DE ESTRUCTURA DE DATOS")
    print("="*50)
    
    # Información general
    print(f"Total de registros: {len(df):,}")
    print(f"Total de columnas: {len(df.columns)}")
    
    # Columnas disponibles
    print(f"\nColumnas disponibles:")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i:2d}. {col}")
    
    # Tipos de datos
    print(f"\nTipos de datos:")
    print(df.dtypes)
    
    # Valores nulos
    print(f"\nValores nulos por columna:")
    valores_nulos = df.isnull().sum()
    for col, nulos in valores_nulos.items():
        if nulos > 0:
            print(f"  {col}: {nulos:,} ({nulos/len(df)*100:.2f}%)")
    
    return {
        'total_registros': len(df),
        'total_columnas': len(df.columns),
        'valores_nulos': valores_nulos.to_dict()
    }

def estadisticas_generales(df):
    """
    Calcular estadísticas descriptivas generales.
    """
    print("\n" + "="*50)
    print("ESTADÍSTICAS GENERALES")
    print("="*50)
    
    # Estadísticas de ride_length
    print("Duración de viajes (ride_length en minutos):")
    ride_stats = df['ride_length'].describe()
    print(f"  • Promedio: {ride_stats['mean']:.2f} minutos")
    print(f"  • Mediana: {ride_stats['50%']:.2f} minutos")
    print(f"  • Mínimo: {ride_stats['min']:.2f} minutos")
    print(f"  • Máximo: {ride_stats['max']:.2f} minutos")
    print(f"  • Desviación estándar: {ride_stats['std']:.2f} minutos")
    
    # Distribución por tipo de usuario
    print(f"\nDistribución por tipo de usuario:")
    user_dist = df['member_casual'].value_counts()
    user_pct = df['member_casual'].value_counts(normalize=True) * 100
    
    for user_type in user_dist.index:
        count = user_dist[user_type]
        pct = user_pct[user_type]
        print(f"  • {user_type}: {count:,} registros ({pct:.1f}%)")
    
    # Distribución por día de semana
    print(f"\nDistribución por día de semana:")
    if 'day_name' in df.columns:
        day_dist = df['day_name'].value_counts()
        for day, count in day_dist.items():
            pct = count / len(df) * 100
            print(f"  • {day}: {count:,} registros ({pct:.1f}%)")
    
    return {
        'ride_length_stats': {
            'promedio': ride_stats['mean'],
            'mediana': ride_stats['50%'],
            'minimo': ride_stats['min'],
            'maximo': ride_stats['max'],
            'std': ride_stats['std']
        },
        'distribucion_usuarios': user_dist.to_dict(),
        'distribucion_dias': day_dist.to_dict() if 'day_name' in df.columns else {}
    }

def analizar_por_tipo_usuario(df):
    """
    Análisis detallado por tipo de usuario.
    """
    print("\n" + "="*50)
    print("ANÁLISIS POR TIPO DE USUARIO")
    print("="*50)
    
    resultados_por_usuario = {}
    
    for user_type in df['member_casual'].unique():
        subset = df[df['member_casual'] == user_type]
        
        print(f"\n{user_type.upper()}:")
        print(f"  Registros: {len(subset):,}")
        
        # Duración promedio
        duracion_promedio = subset['ride_length'].mean()
        duracion_mediana = subset['ride_length'].median()
        
        print(f"  Duración promedio: {duracion_promedio:.2f} minutos")
        print(f"  Duración mediana: {duracion_mediana:.2f} minutos")
        
        # Porcentaje del total
        pct_total = len(subset) / len(df) * 100
        print(f"  Porcentaje del total: {pct_total:.1f}%")
        
        resultados_por_usuario[user_type] = {
            'registros': len(subset),
            'duracion_promedio': duracion_promedio,
            'duracion_mediana': duracion_mediana,
            'porcentaje_total': pct_total
        }
    
    return resultados_por_usuario

def generar_resumen_ejecutivo(estadisticas_estructura, stats_generales, resultados_usuario):
    """
    Generar resumen ejecutivo del análisis.
    """
    print("\n" + "="*50)
    print("RESUMEN EJECUTIVO")
    print("="*50)
    
    print(f"Dataset analizado: {estadisticas_estructura['total_registros']:,} registros")
    print(f"Período completo de datos disponibles")
    print(f"Datos limpios sin valores nulos críticos")
    
    print(f"\nHallazgos principales:")
    
    # Duración promedio general
    print(f"  • Duración promedio general: {stats_generales['ride_length_stats']['promedio']:.1f} minutos")
    
    # Distribución de usuarios
    for user_type, stats in resultados_usuario.items():
        print(f"  • {user_type}: {stats['porcentaje_total']:.1f}% de usuarios, promedio {stats['duracion_promedio']:.1f} minutos")
    
    # Comparación entre tipos de usuario
    member_avg = resultados_usuario.get('member', {}).get('duracion_promedio', 0)
    casual_avg = resultados_usuario.get('casual', {}).get('duracion_promedio', 0)
    
    if member_avg > 0 and casual_avg > 0:
        if casual_avg > member_avg:
            diff = casual_avg - member_avg
            print(f"  • Los usuarios casuales viajan {diff:.1f} minutos más en promedio que los miembros")
        else:
            diff = member_avg - casual_avg
            print(f"  • Los miembros viajan {diff:.1f} minutos más en promedio que los casuales")

def main():
    """
    Función principal del análisis.
    """
    print("Iniciando Análisis Descriptivo Exploratorio - Cyclistic")
    print("=" * 60)
    
    # Cargar datos
    df = cargar_datos()
    if df is None:
        print("No se pudo cargar el dataset. Verificar ubicación del archivo.")
        return
    
    # Análisis de estructura
    stats_estructura = analizar_estructura_datos(df)
    
    # Estadísticas generales
    stats_generales = estadisticas_generales(df)
    
    # Análisis por tipo de usuario
    resultados_usuario = analizar_por_tipo_usuario(df)
    
    # Resumen ejecutivo
    generar_resumen_ejecutivo(stats_estructura, stats_generales, resultados_usuario)
    
    # Guardar resultados en JSON para documentación
    resultados_completos = {
        'timestamp': datetime.now().isoformat(),
        'estadisticas_estructura': stats_estructura,
        'estadisticas_generales': stats_generales,
        'resultados_por_usuario': resultados_usuario
    }
    
    with open('resultados_analisis_descriptivo.json', 'w', encoding='utf-8') as f:
        json.dump(resultados_completos, f, indent=2, ensure_ascii=False)
    
    print(f"\nResultados guardados en: resultados_analisis_descriptivo.json")
    print("\nAnálisis Descriptivo Exploratorio completado!")

if __name__ == "__main__":
    main()