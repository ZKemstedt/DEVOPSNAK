class Pizza:

    def __init__(self):
        self.ingredients = ["cheese", "tomato"]

    def add_ingredients(self, ingredients):
        self.ingredients.extend(ingredients)
