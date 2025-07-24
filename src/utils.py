import json
import os
from src.product import Product
from src.catecory import Category


def read_json(path: str) -> dict:
    """
    Читает содержимое JSON-файла и возвращает словарь.

    :param path: Относительный или абсолютный путь к файлу
    :return: Содержимое файла в виде словаря
    """
    try:
        full_path = os.path.abspath(path)

        # Проверяем существование файла перед открытием
        if not os.path.isfile(full_path):
            raise FileNotFoundError(f"Файл '{full_path}' не найден")

        with open(full_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return {}


def list_products_and_catecory_from_json(data: dict) -> list:
    """
    Читает содержимое словаря, возращает список категорий
    :param data: словарь
    :return: список категорий
    """
    catecories = []
    for catecory_data in data:
        products = []
        for product in catecory_data["products"]:
            products.append(Product(**product))
        catecory_data["products"] = products
        catecories.append(Category(**catecory_data))
    return catecories


if __name__ == "__main__":
    patch = "../src/products.json"
    read_data = read_json(patch)
    list_catecory = list_products_and_catecory_from_json(read_data)
    print(list_catecory)
