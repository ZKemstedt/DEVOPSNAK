class Calculator:

    def parse(self, arg):
        return arg.split(" ")

    def add(self, arg):
        try:
            self.calc_add(self.parse(arg))
            return False
        except Exception as e:
            print(e)
            return True

    def calc_add(self, values):
        result = 0
        for val in values:
            result += int(val)
        print(result)
        return result
