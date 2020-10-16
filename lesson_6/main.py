from lesson_6.menu import Menu
from lesson_6.pizza import Pizza
from lesson_6.file_handler import FileHandler


def main():
    menu = Menu("takeaway")
    menu.load_file(FileHandler("lesson_6/pizzas.json"))
    print(menu.list_pizzas())


if __name__ == "__main__":
    main()
