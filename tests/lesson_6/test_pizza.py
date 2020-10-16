import unittest
from lesson_6.pizza import Pizza


class TestPizza(unittest.TestCase):

    def setUp(self):
        self.pizza = Pizza()

    def test_pizza_create(self):
        self.assertIsInstance(self.pizza, Pizza)

    def test_pizza_create_with_ingredients(self):
        ingredients = ["mushroom", "ham"]
        self.pizza.add_ingredients(ingredients)
        self.assertListEqual(self.pizza.ingredients, ["cheese", "tomato", *ingredients])

    def test_pizza_create_default_ingredients(self):
        self.assertListEqual(self.pizza.ingredients, ["cheese", "tomato"])


if __name__ == "__main__":
    unittest.main()
