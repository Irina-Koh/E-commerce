def test_catecory_init(first_catecory, second_catecory):
    assert first_catecory.name == "Смартфоны"
    assert (
        first_catecory.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(first_catecory.products) == 2

    assert first_catecory.number_of_categories == 2
    assert second_catecory.number_of_categories == 2

    assert first_catecory.number_of_products == 3
    assert second_catecory.number_of_products == 3
