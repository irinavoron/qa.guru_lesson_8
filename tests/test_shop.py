"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from tests.models import Product, Cart

buy_count: int = 1


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity - 1)
        assert not product.check_quantity(product.quantity + 1)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        start_product_quantity = product.quantity
        count_to_buy = product.quantity - 1
        product.buy(count_to_buy)
        assert product.quantity == start_product_quantity - count_to_buy

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError, match='Not enough on stock'):
            product.buy(product.quantity + 1)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, product, cart):
        cart.add_product(product, buy_count)
        assert cart.products[product] == buy_count

    def test_cart_add_product_that_is_in_cart(self, product, cart):
        cart.add_product(product, buy_count)
        cart.add_product(product, buy_count)
        assert len(cart.products) == 1
        assert cart.products[product] == buy_count * 2

    def test_cart_remove_product(self, product, cart):
        cart.add_product(product, buy_count)
        cart.remove_product(product)
        assert product not in cart.products

        cart.add_product(product, buy_count)
        cart.remove_product(product, buy_count * 2)
        assert product not in cart.products

    def test_cart_remove_product_partially(self, product, cart):
        cart.add_product(product, buy_count * 2)
        cart.remove_product(product, buy_count)
        assert cart.products[product] == buy_count

    def test_cart_clear(self, product, cart):
        cart.add_product(product, buy_count)
        cart.clear()
        assert len(cart.products) == 0

    def test_cart_get_total_price(self, product, cart):
        assert cart.get_total_price() == 0
        count_to_buy = buy_count * 2
        cart.add_product(product, count_to_buy)
        assert cart.get_total_price() == count_to_buy * product.price

    def test_cart_buy(self, product, cart):
        start_product_quantity = product.quantity
        cart.add_product(product, buy_count)
        cart.buy()
        assert product.quantity == start_product_quantity - buy_count

    def test_cart_buy_more_than_available(self, product, cart):
        cart.add_product(product, product.quantity + 1)
        with pytest.raises(ValueError, match='Not enough on stock'):
            cart.buy()
