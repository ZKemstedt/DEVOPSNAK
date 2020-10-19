import cmd
from calculator import Calculator


class CalculatorTool(cmd.Cmd):
    intro = 'Welcome to the calculator tool. Type help or ? to list commands.\n'
    prompt = '(Calculator tool) '
    calc = Calculator()

    def do_bye(self, arg):
        'Close the calculator tool, and exit'
        return True

    def do_add(self, arg):
        'add two numbers'
        return self.calc.add(arg)


if __name__ == '__main__':
    CalculatorTool().cmdloop()
