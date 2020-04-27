## Descripción

Esta utilidad combina múltiples archivos de Excel, .csv o .txt en un sólo archivo .xlsx.

Los archivos de entrada deben encontrarse en una directorio específico y tener la misma estructura de columnas. La utilidad intentará unir **todos** los archivos .txt, .csv, .xls y/o .xlsx dentro de la ruta de entrada.

Supongamos que en la ruta **/input/** tenemos dos archivos de Excel como siguen

**_archivo1.xlsx_**

| Fecha      | Cantidad |
| ---------- | -------- |
| 2020-04-26 | 12       |
| 2020-04-26 | 36       |
| 2020-04-26 | 8        |

**_archivo2.xlsx_**

| Fecha      | Cantidad |
| ---------- | -------- |
| 2020-04-27 | 95       |
| 2020-04-27 | 102      |
| 2020-04-27 | 98       |

Al ejecutar `python merge.py` obtenemos el siguiente resultado:

**_Resultado.xlsx_**
| Fecha | Cantidad  
| ------------- |-------------
| 2020-04-26 | 12
| 2020-04-26 | 36
| 2020-04-26 | 8
| 2020-04-27 | 95
| 2020-04-27 | 102
| 2020-04-27 | 98

## Instrucciones:

1. Instalar dependencias usando pipenv o pip (se provee Pipfile y requirements.txt)
2. Ejecutar `python merge.py`

## Argumentos opcionales

**--folder_path**

- Directorio donde se encuentran los archivos a combinar. Por defecto es "input/"

**--sep**

- Separador de columnas. Opciones: Tabulación: t, Coma: c, Espacio: s

**--skiprows**

- Número de filas a omitir al principio del archivoPor ejemplo, si los encabezados de la tabla están en la fila 5se configura skiprows=4

**--output**

- Nombre del archivo de Excel de resultado. Valor por defecto: "Resultado.xlsx"

**--help**

- Ayuda

## Ejemplos

- Combinar archivos en la ruta _C:\Users\luisc\Documents\mediciones_

  `python merger.py --folder_path "C:\Users\luisc\Documents\mediciones"`

- Combinar archivos .txt con columnas separadas por tabulaciones en la ruta relativa _/input/_, donde los encabezados están en la fila 5

  `python merger.py --sep t --skiprows 4`

## Generar ejecutable (windows)

`pyinstaller merger.py --onefile --hidden-import="pkg_resources.py2_warn"`
