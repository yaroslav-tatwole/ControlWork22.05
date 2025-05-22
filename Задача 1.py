import pandas as pd
def display_excel_row(file_path):
    """
    Функция для вывода конкретной строки из Excel файла по запросу пользователя.

    :param file_path: Путь к Excel файлу
    """
    try:
        # Чтение Excel файла
        df = pd.read_excel(file_path)
        # Вывод общего количества строк
        print(f"\nФайл содержит {len(df)} строк данных (не считая заголовков).")
        print("Столбцы:", list(df.columns))
        while True:
            # Запрос номера строки у пользователя
            row_num = input("\nВведите номер строки для вывода (1 - первая строка данных, 'q' для выхода): ")
            if row_num.lower() == 'q':
                break
            try:
                row_num = int(row_num)
                if 1 <= row_num <= len(df):
                    # Вывод выбранной строки
                    print(f"\nСтрока {row_num}:")
                    print(df.iloc[row_num - 1])
                else:
                    print(f"Ошибка: Номер строки должен быть от 1 до {len(df)}")
            except ValueError:
                print("Ошибка: Введите целое число или 'q' для выхода")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
if name == "main":
    # Укажите путь к вашему Excel файлу
    excel_file = input("Введите путь к Excel файлу: ")
    display_excel_row(excel_file)