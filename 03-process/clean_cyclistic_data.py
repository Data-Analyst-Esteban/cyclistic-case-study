#!/usr/bin/env python3
"""
Script: Limpieza de Datos - Cyclistic
Autor: Esteban Alonso Molina Morales
Descripción: Limpia y prepara datos de Divvy siguiendo metodología del caso de estudio.
"""

import pandas as pd
import zipfile
import os
from pathlib import Path
from datetime import datetime

# Configuración
data_dir = Path("cyclistic-case-study/data")
input_dir = data_dir / "raw"
output_dir = data_dir / "processed"

# Crear directorio de salida
output_dir.mkdir(parents=True, exist_ok=True)

def extract_csv_files():
    """Extraer archivos CSV de archivos ZIP"""
    print("Extrayendo archivos CSV...")
    
    extracted_dir = data_dir / "extracted"
    extracted_dir.mkdir(parents=True, exist_ok=True)
    
    extracted_files = []
    zip_files = list(input_dir.glob("*-divvy-tripdata.zip"))
    
    for zip_file in zip_files:
        print(f"Procesando: {zip_file.name}")
        
        with zipfile.ZipFile(zip_file, 'r') as z:
            csv_files = [f for f in z.namelist() if f.endswith('.csv')]
            if csv_files:
                z.extract(csv_files[0], extracted_dir)
                extracted_files.append(extracted_dir / csv_files[0])
                print(f"OK: {csv_files[0]}")
    
    return extracted_files

def validate_and_clean_data(files):
    """Validar y limpiar datos"""
    print("\nValidando y limpiando datos...")
    
    all_data = []
    total_rows = 0
    
    for file_path in files:
        print(f"Validando: {file_path.name}")
        
        try:
            # Leer CSV con validación básica
            df = pd.read_csv(file_path, low_memory=False)
            
            # Validaciones básicas
            if len(df) == 0:
                print(f"ADVERTENCIA: {file_path.name} está vacío")
                continue
            
            # Renombrar columnas para consistencia
            df.columns = df.columns.str.lower()
            
            # Filtrar registros válidos básicos
            initial_rows = len(df)
            
            # Remover filas con timestamps nulos
            df = df.dropna(subset=['started_at', 'ended_at'])
            
            # Remover duraciones negativas o muy cortas
            df['ride_length'] = (pd.to_datetime(df['ended_at']) - 
                               pd.to_datetime(df['started_at'])).dt.total_seconds()
            df = df[df['ride_length'] > 0]
            
            # Remover duraciones muy largas (>24 horas)
            df = df[df['ride_length'] < 86400]
            
            final_rows = len(df)
            
            if initial_rows != final_rows:
                print(f"Filtrados: {initial_rows - final_rows} registros inválidos")
            
            all_data.append(df)
            total_rows += final_rows
            
        except Exception as e:
            print(f"ERROR: {file_path.name} - {e}")
    
    print(f"\nTotal registros válidos: {total_rows:,}")
    return all_data

def create_calculated_columns(all_data):
    """Crear columnas calculadas según caso de estudio"""
    print("\nCreando columnas calculadas...")
    
    for i, df in enumerate(all_data):
        print(f"Procesando archivo {i+1}/{len(all_data)}")
        
        # Crear ride_length (en formato HH:MM:SS)
        df['ride_length_formatted'] = pd.to_timedelta(df['ride_length'], unit='s')
        
        # Crear day_of_week (1=Domingo, 7=Sábado)
        df['day_of_week'] = pd.to_datetime(df['started_at']).dt.dayofweek + 1
        
        # Mapear nombres de días
        days_map = {1: 'Domingo', 2: 'Lunes', 3: 'Martes', 4: 'Miércoles',
                   5: 'Jueves', 6: 'Viernes', 7: 'Sábado'}
        df['day_name'] = df['day_of_week'].map(days_map)
        
        all_data[i] = df
    
    return all_data

def combine_and_save_data(all_data):
    """Combinar y guardar datos limpios"""
    print("\nCombinando y guardando datos...")
    
    if not all_data:
        print("ERROR: No hay datos para combinar")
        return
    
    # Combinar todos los dataframes
    combined_df = pd.concat(all_data, ignore_index=True)
    
    print(f"Dataset combinado: {len(combined_df):,} registros")
    
    # Guardar dataset limpio
    output_file = output_dir / "cyclistic_clean_data.csv"
    combined_df.to_csv(output_file, index=False)
    print(f"Guardado: {output_file}")
    
    # Generar estadísticas básicas
    print("\n=== ESTADÍSTICAS BÁSICAS ===")
    print(f"Total registros: {len(combined_df):,}")
    
    if 'usertype' in combined_df.columns:
        user_counts = combined_df['usertype'].value_counts()
        print(f"Distribución usuarios:")
        for user_type, count in user_counts.items():
            pct = (count / len(combined_df)) * 100
            print(f"  {user_type}: {count:,} ({pct:.1f}%)")
    
    if 'ride_length' in combined_df.columns:
        avg_duration = combined_df['ride_length'].mean() / 60  # minutos
        print(f"Duración promedio: {avg_duration:.1f} minutos")
    
    return combined_df

def main():
    """Función principal"""
    print("=== PROCESO DE LIMPIEZA CYCLISTIC ===")
    
    # Verificar que existen los archivos de entrada
    if not input_dir.exists():
        print(f"ERROR: Directorio {input_dir} no existe")
        return
    
    zip_count = len(list(input_dir.glob("*-divvy-tripdata.zip")))
    if zip_count == 0:
        print(f"ERROR: No se encontraron archivos ZIP en {input_dir}")
        return
    
    print(f"Archivos encontrados: {zip_count}")
    
    try:
        # Paso 1: Extraer CSV files
        extracted_files = extract_csv_files()
        
        if not extracted_files:
            print("ERROR: No se extrajeron archivos CSV")
            return
        
        # Paso 2: Validar y limpiar datos
        all_data = validate_and_clean_data(extracted_files)
        
        if not all_data:
            print("ERROR: No hay datos válidos después de la validación")
            return
        
        # Paso 3: Crear columnas calculadas
        all_data = create_calculated_columns(all_data)
        
        # Paso 4: Combinar y guardar
        combined_df = combine_and_save_data(all_data)
        
        print("\n✅ LIMPIEZA COMPLETADA EXITOSAMENTE")
        print(f"Datos guardados en: {output_dir}")
        
    except Exception as e:
        print(f"ERROR CRÍTICO: {e}")

if __name__ == "__main__":
    main()