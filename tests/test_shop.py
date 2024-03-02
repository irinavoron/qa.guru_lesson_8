"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from tests.models import Product, Cart

BUY_COUNT: int = 1


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
        assert product.check_quantity(999)
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        start_product_quantity = product.quantity
        buy_count = product.quantity - 1
        product.buy(buy_count)
        assert product.quantity == start_product_quantity - buy_count

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError, match='Not enough Product on stock'):
            product.buy(product.quantity + 1)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, product, cart):
        cart.add_product(product, BUY_COUNT)
        assert cart.products[product] == BUY_COUNT

    def test_cart_add_product_that_is_in_cart(self, product, cart):
        cart.add_product(product, BUY_COUNT)
        cart.add_product(product, BUY_COUNT)
        assert len(cart.products) == 1
        assert cart.products[product] == BUY_COUNT * 2

    def test_cart_remove_product(self, product, cart):
        cart.add_product(product, BUY_COUNT)
        cart.remove_product(product)
        assert product not in cart.products
        cart.add_product(product, BUY_COUNT)
        cart.remove_product(product, BUY_COUNT * 2)
        assert product not in cart.products

    def test_cart_remove_product_partially(self, product, cart):
        cart.add_product(product, BUY_COUNT * 2)
        cart.remove_product(product, BUY_COUNT)
        assert cart.products[product] == BUY_COUNT

    def test_cart_clear(self, product, cart):
        pass