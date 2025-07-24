class Category:
    """Класс для представления категории."""
    name: str
    description: str
    products: list
    number_of_categories = 0
    number_of_products = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.number_of_categories += 1
        Category.number_of_products += len(products) if products else 0
