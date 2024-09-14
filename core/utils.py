import json


def dict_list_to_json(dict_list, filename):
    """
    Преобразует список словарей в JSON-строку и сохраняет её в файл.

    :param dict_list: Список словарей
    :param filename: Имя файла для сохранения JSON-строки
    :return: JSON-строка или None в случае ошибки
    """
    try:
        json_str = json.dumps(dict_list, ensure_ascii=False)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_str)
        return json_str
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при преобразовании списка словарей в JSON или записи в файл: {e}")
        return None


def json_to_dict_list(filename):
    """
    Преобразует JSON-строку из файла в список словарей.

    :param filename: Имя файла с JSON-строкой
    :return: Список словарей или None в случае ошибки
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            json_str = file.read()
            dict_list = json.loads(json_str)
        return dict_list
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при чтении JSON из файла или преобразовании в список словарей: {e}")
        return None


def update_json_file(filename, data):
    """
    Обновляет содержимое JSON-файла.

    :param filename: Имя файла для обновления
    :param data: Новый контент JSON-файла
    :return: True, если обновление прошло успешно, False - в случае ошибки
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Ошибка при обновлении JSON-файла: {e}")
        return False