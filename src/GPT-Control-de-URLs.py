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
#from requests.exceptions import RequestException
import warnings
import time

# Suprimo advertencias de InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Cambio a mi directorio de datos, siempre es ../data en cada repo
os.chdir("../data/")

# Encabezados de solicitud personalizados para hacer los requests mas humanos
headers = {
    'User-Agent': 'Usuario Personalizado',
    'Accept-Language': 'es-ES,es;q=0.9',
}

el_excell = "Links y PDFs Ingestados en GPT.xlsx"

try:
    df = pd.read_excel(el_excell)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{el_excell}'")
    sys.exit()
except ValueError as ve:
    print(f"Error: {str(ve)}")
    sys.exit()
except Exception as e:
    print(f"Error al procesar el archivo: {str(e)}")
    sys.exit()
    
# SOLO tomo donde no es "BAJA"
df_filtrado = df[df['ESTADO'] != "BAJA"].copy()

# Elimino donde URL está vacío o nulo
df_filtrado = df_filtrado.dropna(subset=['URL'])  
df_filtrado = df_filtrado[df_filtrado['URL'].str.strip() != '']  

df_filtrado = df_filtrado.reset_index(drop=True)


# Divido segun valores en Conteo
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
                print(f"  URL válida: {url}")
                return True
        except requests.exceptions.RequestException as e:
            print(f" X Error al acceder a {url}: {e}")
            break
        
        intento_actual += 1
        if intento_actual < max_intentos:
            print(f"  Reintentando ({intento_actual}/{max_intentos})...")
        time.sleep(1)
             
    if not esValida:
        print(f" X  URL inválida: {url}")
        return False
    
import os

import os

import os

def procesar_dataframe(df, nombre_base):
    df = df.copy()
    df['URL_activa'] = df['URL'].apply(verificar_url)
    
    # Genero un archivo CSV con URLs inválidas (en la carpeta actual)
    df_invalidas = df[~df['URL_activa']]
    df_invalidas[['URL']].to_csv(f"{nombre_base}_invalidas.csv", index=False)
    print(f"Archivo de URLs inválidas exportado: {nombre_base}_invalidas.csv")
    
    # Genero un archivo CSV con URLs válidas en la carpeta "../"
    df_validas = df[df['URL_activa']]
    ruta_validas = os.path.join("../", f"{nombre_base}_validas.csv")
    df_validas[['URL']].to_csv(ruta_validas, index=False)
    print(f"Archivo de URLs válidas exportado: {ruta_validas}")
    
    # Calculo algunos descriptores
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
    print(f"Exportados los descriptores estadísticos básicos: {nombre_base}_informe.txt")
    
    return informe


# Proceso cada uno de los dataframes ya dividos
informe_menor_igual_2 = procesar_dataframe(df_menor_igual_2, "urls_conteo_menor_igual_2")
informe_mayor_igual_3 = procesar_dataframe(df_mayor_igual_3, "urls_conteo_mayor_igual_3")

# Muestro por Standard Output los descriptores
print("\n" + informe_menor_igual_2)
print("\n" + informe_mayor_igual_3)