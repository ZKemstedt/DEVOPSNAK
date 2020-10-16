class Pizza:
    price_groups = {
        1: 80,
        2: 90
    }

    ingredients_valuation = {
        "mozzarella": 1,
        "pepperoni": 1
    }

    def __init__(self):
        self.ingredients = ["cheese", "tomato"]

    def add_ingredients(self, ingredients):
        self.ingredients.extend(ingredients)

    @property
    def price_group(self):
        price_group = 1
        for ingredient in self.ingredients:
            if(ingredient in Pizza.ingredients_valuation):
                price_group += Pizza.ingredients_valuation[ingredient]
        return price_group

    @property
    def price(self):
        return Pizza.price_groups[self.price_group]
