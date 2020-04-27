import os
from pathlib import Path
import pandas as pd


def validate_args(args):
    valid_args = True
    errors = []
    if args.skiprows < 0 or not isinstance(args.skiprows, int):
        valid_args = False
        errors.append('Parámetro skiprows debe ser entero positivo')

    if not os.path.isdir(args.folder_path):
        valid_args = False
        errors.append(f'Directorio {args.folder_path} no existe')

    if args.output[-5:] != '.xlsx':
        valid_args = False
        errors.append('"output" debe ser un nombre de archivo .xlsx válido')

    return valid_args, errors


def load_file_to_df(df_src, fname, fpath, fext, sep=',', skiprows=0):
    "Toma un archivo y lo carga en un dataframe pandas. "
    try:
        if fext in ['.csv', '.txt']:
            df = pd.read_csv(fpath, sep=sep, skiprows=skiprows)
            df['File Name'] = fpath
        if fext in ['.xlsx', '.xls']:
            # Combinar todos los sheets del archivo de Excel
            # Revisar https://pbpython.com/pandas-excel-tabs.html
            df_subs = pd.read_excel(fpath, sheet_name=None)
            for sheet_name, df_sub in df_subs.items():
                df_sub['File Name'] = f'{fname}_{sheet_name}'
            df = pd.concat(df_subs, ignore_index=True)
        df_result = pd.concat([df_src, df], axis=0, ignore_index=True)
        msg_success = f'Procesado archivo {fpath}'
        return df_result, msg_success

    except Exception as e:
        msg_error = f'Error procesando {fpath}: {str(e)}'
        return df_src, msg_error


def concat_files(folder_path, file_names, sep, skiprows):
    """Toma una lista de archivos y los carga en un df pandas"""
    df = None
    for fname in file_names:
        fpath = os.path.join(folder_path, fname)
        fext = Path(fpath).suffix
        if fext not in ['.csv', '.txt', '.xlsx', '.xls']:
            print(f'Ignorando archivo {fpath}. Formato no soportado')
        else:
            df, result = load_file_to_df(
                df, fname, fpath, fext, sep=sep, skiprows=skiprows)
            print(result)
    return df
