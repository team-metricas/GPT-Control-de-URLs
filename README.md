# GPT-Control-de-URLs
Controlar las Urls ingestadas en GPT 

Fuente de Información : https://gcaba.sharepoint.com/:x:/r/sites/SSCIUI_DGCDI-MejoraContinuaCanales/Documentos%20compartidos/Mejora%20Continua%20Canales/Boti/Squad%20Investigaci%C3%B3n%20%F0%9F%9A%80/Nuevo%20modelo%20IA/OPEN%20AI%20-%20GPT/Links%20y%20PDFs%20Ingestados%20en%20GPT.xlsx?d=w01eee6277c95408d9c432abab13b0cad&csf=1&web=1&e=ccJxuc 


## Objetivos

 - Separar las Urls dadas de baja 
 - Separar las urls vencidas y armar un reporte en excel 
 - Separar las urls Ingestadas y vigentes por columna Conteo <= 2 y >=3 y armar 2 archivos tipo txt (una url debajo de la otra) 

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Contribución](#contribución)
- [Licencia](#licencia)
- [Contacto](#contacto)

### Instalación

#### Requisitos Previos

- Python 3.11 o superior
- pip

#### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/team-metricas/GPT-Control-de-URLs

# Entrar al directorio del proyecto
cd src

# Instalar las dependencias
pip install pandas
pip install openpyxl
pip install requests

```

### Uso
 
En la carpeta `/data` se hallan los Archivo de input.


Ejecutar el programa en `/src`   
GPT-Control-de-URLs.py   


### Características  

Toma la planilla excel descargada del sharepoint y realiza los siguientes filtros.
 - Estado distinto de "BAJA"   -  excluyente
 - Filas donde "CONTEO" es menor o igual a 2  
 - Filas donde "CONTEO" es mayor o igual a 3  

De los 2 grupos identificados, chequea que las URLs sean validas.

#### Entregables ##  
En la raiz del repositorio   
`urls_conteo_mayor_igual_3_validas.csv`  
`urls_conteo_menor_igual_2_validas.csv`  

En la carpeta Data   
`urls_conteo_mayor_igual_3_informe.txt`  
`urls_conteo_menor_igual_2_informe.txt`    
`urls_conteo_mayor_igual_3_invalidas.csv`    
`urls_conteo_mayor_igual_3_invalidas.csv`  


### Contribución  
¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama para tu funcionalidad o corrección de errores (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commits con mensajes claros y concisos (`git commit -m 'Descripción de los cambios'`).
4. Sube tus cambios a tu repositorio (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request en el repositorio original y describe los cambios que has realizado.

Por favor, asegúrate de que tu código sigue los estándares de estilo del proyecto y que todas las pruebas pasan correctamente antes de enviar tu Pull Request.


### Licencia 

Este proyecto está bajo la Licencia MIT.

MIT License

Derechos de autor (c) [2024] [Eduardo Damian Veralli]

Se concede permiso por la presente, sin cargo, a cualquier persona que obtenga una copia
de este software y los archivos de documentación asociados (el "Software"), para tratar
en el Software sin restricciones, incluidos, entre otros, los derechos
para usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender
copias del Software, y para permitir a las personas a quienes se les proporcione el Software
hacerlo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todos
copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O
IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O
LOS TITULARES DEL COPYRIGHT SERÁN RESPONSABLES POR CUALQUIER RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD,
YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, QUE SURJA DE, FUERA DE O EN
CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL SOFTWARE.


### Contacto 

Para preguntas, sugerencias o comentarios, puedes contactar a:

Eduardo Damián Veralli - [@edveralli](https://x.com/EdVeralli) - edveralli@gmail.com

Enlace del Proyecto: [https://github.com/team-metricas/GPT-Control-de-URLs](https://github.com/team-metricas/GPT-Control-de-URLs)


