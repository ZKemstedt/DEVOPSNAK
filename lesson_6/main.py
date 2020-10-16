from lesson_6.menu import Menu
from lesson_6.pizza import Pizza


def main():
    margherita = Pizza("margherita")
    vesuvio = Pizza("vesuvio", ["cheese", "tomato", "ham"])
    menu = Menu("takeaway", [margherita, vesuvio])
    print(menu.list_pizzas())


if __name__ == "__main__":
    main()
