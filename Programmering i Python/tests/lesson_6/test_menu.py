import unittest
from lesson_6.menu import Menu
from lesson_6.pizza import Pizza


class TestMenuEmpty(unittest.TestCase):

    def setUp(self):
        self.menu = Menu("takeaway")

    def test_menu_create_success(self):
        self.assertIsInstance(self.menu, Menu)

    def test_menu_pizzas_empty_by_default(self):
        self.assertListEqual(self.menu.pizzas, [])

    def test_menu_list_pizzas_return_list(self):
        self.assertIsInstance(self.menu.list_pizzas(), list)


class TestMenuWithPizza(unittest.TestCase):

    def setUp(self):
        margherita = Pizza("margherita")
        vesuvio = Pizza("vesuvio", ["cheese", "tomato", "ham"])
        self.pizzas = [margherita, vesuvio]
        self.menu = Menu("takeaway", self.pizzas.copy())

    def test_menu_create_success(self):
        self.assertIsInstance(self.menu, Menu)

    def test_menu_pizzas_returns_pizzas(self):
        self.assertListEqual(self.menu.pizzas, self.pizzas)

    def test_menu_list_pizzas_return_list(self):
        self.assertIsInstance(self.menu.list_pizzas(), list)


if __name__ == "__main__":
    unittest.main()
