import unittest
from lesson_6.pizza import Pizza


class TestPizza(unittest.TestCase):

    def setUp(self):
        self.pizza = Pizza()

    def test_pizza_create_success(self):
        self.assertIsInstance(self.pizza, Pizza)

    def test_pizza_create_with_ingredients_return_list(self):
        ingredients = ["mushroom", "ham"]
        self.pizza.add_ingredients(ingredients)
        self.assertListEqual(self.pizza.ingredients, ["cheese", "tomato", *ingredients])

    def test_pizza_create_default_ingredients_return_list(self):
        self.assertListEqual(self.pizza.ingredients, ["cheese", "tomato"])

    # UnitOfWork_StateUnderTest_ExpectedBehavior
    def test_pizza_price_group_default_1(self):
        self.assertEqual(self.pizza.price_group, 1)

    def test_pizza_price_price_group_1_returns_price(self):
        self.assertEqual(self.pizza.price, 80)

    def test_Pizza_price_groups_exists(self):
        self.assertIsInstance(Pizza.price_groups, dict)

    def test_Pizza_price_groups_1_is_int(self):
        self.assertIsInstance(Pizza.price_groups[1], int)

    def test_pizza_add_pepperoni_returns_price_group_2(self):
        ingredients = ["pepperoni"]
        self.pizza.add_ingredients(ingredients)
        self.assertEqual(self.pizza.price_group, 2)

    def test_pizza_price_price_group_2_returns_price(self):
        ingredients = ["pepperoni"]
        self.pizza.add_ingredients(ingredients)
        self.assertEqual(self.pizza.price, 90)

    def test_pizza_ingredients_valuation_dict(self):
        self.assertIsInstance(Pizza.ingredients_valuation, dict)

    def test_pizza_mozzarella_returns_price_group_2(self):
        ingredients = ["mozzarella"]
        self.pizza.add_ingredients(ingredients)
        self.assertEqual(self.pizza.price_group, 2)

    def test_pizza_mozzarella_and_pepperoni_returns_price_group_3(self):
        ingredients = ["mozzarella", "pepperoni"]
        self.pizza.add_ingredients(ingredients)
        self.assertEqual(self.pizza.price_group, 3)


if __name__ == "__main__":
    unittest.main()
