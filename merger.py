import os
import argparse
from processing import concat_files, validate_args


def main():
    """Función principal"""

    # Tomar parámetros de línea de comandos
    parser = argparse.ArgumentParser(
        description='Utilidad para combinar archivos de Excel, CSV o TXT '
                    'en un único archivo de EXCEL')

    parser.add_argument(
        '-i', '--folder_path',
        default='input/',
        help='Opcional. Ruta donde se encuentran los archivos a combinar.'
             'Por defecto es "input/"'
    )

    parser.add_argument(
        '-s', '--sep',
        choices=['t', 'c', 's'],
        default='c',
        help='Opcional. Separador de columnas.'
             'Opciones: Tabulación: t, Coma: c, Espacio: s'
    )

    parser.add_argument(
        '-r', '--skiprows',
        type=int,
        default=0,
        help='Opcional. Número de filas a omitir al principio del archivo'
             'Por ejemplo, si los encabezados de la tabla están en la fila 5'
             'se configura skiprows=4'
    )

    parser.add_argument(
        '-o', '--output',
        default='Resultado.xlsx',
        help='Opcional. Nombre del archivo de Excel de resultado\n'
             'Valor por defecto: "Resultado.xlsx"'
    )

    args = parser.parse_args()

    valid_args, errors = validate_args(args)

    if valid_args:
        file_names = os.listdir(args.folder_path)
        sep = args.sep
        skiprows = args.skiprows
        output_fname = args.output
        merged_df = concat_files(args.folder_path, file_names, sep, skiprows)
        merged_df.to_excel(output_fname, sheet_name='merged_data', index=False)
    else:
        error_msg = ', '.join(errors)
        print(f'Ocurrió un error, {error_msg}')


if __name__ == '__main__':
    main()
