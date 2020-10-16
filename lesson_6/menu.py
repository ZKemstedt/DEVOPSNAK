from lesson_6.pizza import Pizza


class Menu:

    def __init__(self, name, pizzas=[]):
        self.name = name
        self.pizzas = pizzas

    def list_pizzas(self):
        return self.pizzas

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def load_file(self, file_handler):
        pizzas = file_handler.load()
        for pizza in pizzas.items():
            self.add_pizza(Pizza(pizza[0], pizza[1]))

    # List pizzas
    # 1. Price Group / price
        # Pizza 1
        # Name
        # Ingredients

        # Pizza 2
        # Name
        # Ingredients
    # 2. Price Group / price
        # Pizza 3
        # Name
        # Ingredients
