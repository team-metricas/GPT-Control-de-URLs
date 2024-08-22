# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 09:18:10 2024
@author: 20171078343
"""
import pandas as pd
import os
import sys
import requests
from urllib3.exceptions import InsecureRequestWarning
from requests.exceptions import RequestException
import warnings
import time

# Suprimir advertencias de InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
os.chdir("../data/")

# Encabezados de solicitud personalizados
headers = {
    'User-Agent': 'Usuario Personalizado',
    'Accept-Language': 'es-ES,es;q=0.9',
}

# Nombre del archivo Excel
nombre_archivo = "Links y PDFs Ingestados en GPT.xlsx"

# Intentar leer el archivo Excel
try:
    df = pd.read_excel(nombre_archivo)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{nombre_archivo}'")
    sys.exit()
except ValueError as ve:
    print(f"Error: {str(ve)}")
    sys.exit()
except Exception as e:
    print(f"Error al procesar el archivo: {str(e)}")
    sys.exit()
    
# Verificar si existen las columnas necesarias
columnas_requeridas = ['ESTADO', 'Conteo', 'URL']
for columna in columnas_requeridas:
    if columna not in df.columns:
        raise ValueError(f"La columna '{columna}' no existe en el archivo Excel.")

# Filtrar las filas donde ESTADO no es "BAJA"
df_filtrado = df[df['ESTADO'] != "BAJA"].copy()

# Eliminar filas donde URL está vacío o nulo
df_filtrado = df_filtrado.dropna(subset=['URL'])  # Elimina filas con URL nulo
df_filtrado = df_filtrado[df_filtrado['URL'].str.strip() != '']  # Elimina filas con URL vacío (después de quitar espacios)

# Reiniciar el índice del DataFrame
df_filtrado = df_filtrado.reset_index(drop=True)

print(f"Filas restantes después de eliminar URLs vacías o nulas: {len(df_filtrado)}")

# Dividir el DataFrame filtrado en dos basado en el campo 'Conteo'
df_menor_igual_2 = df_filtrado[df_filtrado['Conteo'] <= 2].copy()
df_mayor_igual_3 = df_filtrado[df_filtrado['Conteo'] >= 3].copy()

def verificar_url(url):
    max_intentos = 5
    intento_actual = 0
    esValida = False
    
    print(f"Procesando URL: {url}")
    
    while intento_actual < max_intentos:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                response = requests.get(url, headers=headers, verify=False, timeout=10)
            
            if response.status_code == 200:
                esValida = True
                print(f"  ✓ URL válida: {url}")
                return True
        except requests.exceptions.RequestException as e:
            print(f"  ✗ Error al acceder a {url}: {e}")
            break
        
        intento_actual += 1
        if intento_actual < max_intentos:
            print(f"  Reintentando ({intento_actual}/{max_intentos})...")
        time.sleep(1)
             
    if not esValida:
        print(f"  ✗ URL inválida: {url}")
        return False
    
def procesar_dataframe(df, nombre_base):
    df = df.copy()  # Crear una copia explícita
    df['URL_activa'] = df['URL'].apply(verificar_url)
    
    # Crear archivo CSV con todas las URLs y su estado
    df[['URL', 'URL_activa']].to_csv(f"{nombre_base}_todas.csv", index=False)
    print(f"Se ha creado el archivo {nombre_base}_todas.csv")
    
    # Crear archivo CSV solo con las URLs inválidas
    df_invalidas = df[~df['URL_activa']]
    df_invalidas[['URL']].to_csv(f"{nombre_base}_invalidas.csv", index=False)
    print(f"Se ha creado el archivo {nombre_base}_invalidas.csv")
    
    # Generar informe resumido
    total_urls = len(df)
    urls_activas = df['URL_activa'].sum()
    urls_inactivas = total_urls - urls_activas
    porcentaje_activas = (urls_activas / total_urls) * 100
    
    informe = f"""
    Informe resumido para {nombre_base}:
    Total de URLs: {total_urls}
    URLs activas: {urls_activas} ({porcentaje_activas:.2f}%)
    URLs inactivas: {urls_inactivas} ({100 - porcentaje_activas:.2f}%)
    """
    
    with open(f"{nombre_base}_informe.txt", "w") as f:
        f.write(informe)
    print(f"Se ha creado el archivo {nombre_base}_informe.txt")
    
    return informe

# Procesar cada DataFrame
informe_menor_igual_2 = procesar_dataframe(df_menor_igual_2, "urls_conteo_menor_igual_2")
informe_mayor_igual_3 = procesar_dataframe(df_mayor_igual_3, "urls_conteo_mayor_igual_3")

# Imprimir informes en consola
print("\n" + informe_menor_igual_2)
print("\n" + informe_mayor_igual_3)