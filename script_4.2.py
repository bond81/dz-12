import os

def get_size_format(size, factor=1024, suffix="B"):
    """Конвертирует размер файла в удобочитаемый формат (B, KB, MB, GB, TB)"""
    for unit in ["", "K", "M", "G", "T"]:
        if size < factor:
            return f"{size:.2f} {unit}{suffix}"
        size /= factor
    

def list_files_and_folders(path='.'):
    items = []
    
    # Перебираем файлы и папки только в текущей директории
    for name in os.listdir(path):
        item_path = os.path.join(path, name)
        try:
            # Если это файл, получаем его размер напрямую
            if os.path.isfile(item_path):
                size = os.path.getsize(item_path)
            # Если это папка, суммируем размеры всех файлов в ней 
            elif os.path.isdir(item_path):
                size = sum(
                    os.path.getsize(os.path.join(item_path, f))
                    for f in os.listdir(item_path)
                    if os.path.isfile(os.path.join(item_path, f))
                )
            else:
                continue  # пропускаем символические ссылки и другие типы
            # Добавляем в список
            items.append((size, name))
        except FileNotFoundError:
            # Игнорируем файлы, которые были удалены или недоступны
            continue

    # Сортировка по размеру и по убыванию
    items.sort(reverse=True, key=lambda x: x[0])

    # Вывод
    for size, name in items:
        print(f"{get_size_format(size):>10}  {name}")

# Запускаем функцию для текущей директории
list_files_and_folders()
