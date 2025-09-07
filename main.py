import os
import sys
from itertools import count
from pathlib import Path
from PIL import Image
import pillow_heif
from mpmath.libmp import to_int
from sympy.codegen.ast import continue_
from tblib.decorators import returns_errors

pillow_heif.register_heif_opener()

def convert_heic_to_png(input_folder, output_folder):
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    converted_count = 0

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.heic', '.heif')):
            input_path = os.path.join(input_folder, filename)
            output_filename = f"{Path(filename).stem}.png"
            output_path = os.path.join(output_folder, output_filename)

            try:
                if os.path.exists(output_path):
                    print(f"Пропускаем {filename} - уже существует")
                    continue

                image = Image.open(input_path)

                image.save(output_path, "PNG")
                print(f"Конвертирован: {filename} -> {output_filename}")
                converted_count += 1

            except Exception as e:
                print(f"Ошибка при конвертации {filename}: {str(e)}")

    return converted_count

def print_files_to_convert():
    print("Будут конвертированы: ")
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.heic', '.heif')):
            print(filename)

if __name__ == "__main__":
    print("Введите путь к папке с HEIC файлами (по умолчанию текущая папка, ",
          os.path.abspath(""), "):")
    input_folder = input()

    print("Введите путь для сохранения PNG файлов (по умолчанию ",
          os.path.abspath("converted"), "):")
    output_folder = input()

    if not input_folder:
        input_folder = "."
    if not output_folder:
        output_folder = "converted"

    format_convert = "0"
    print("Выберите формат для конвертации: (по умолчанию PNG)\n"
          "[0] - PNG, [1] - JPEG")
    format_convert = input()

    if format_convert == "":
        print("Выбран формат PNG\n")
    elif format_convert == "0":
        format_convert = int(format_convert)
        print("Z")
    elif format_convert == "1":
            format_convert = int(format_convert)
    else:
        print("Введите 0 или 1")
        sys.exit(1)

    print_files_to_convert()

    print("Нажмите Enter, чтобы продолжить. Для выхода введите другой символ.", flush=True)
    last_continue = input()
    if last_continue == "":
        print("Начинаем конвертацию...")
        convert_heic_to_png(input_folder, output_folder)
    else:
        print("Выход...")
        sys.exit(2)

    print("\nПрограмма завершила свою работу. Нажмите любую клавишу для выхода.", flush=True)
    last_continue = input()