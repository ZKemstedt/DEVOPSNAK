from watches import Watches


class Mora(Watches):
    brand = "not set"

    def __init__(self, brand, height, time_format="24"):
        super().__init__(brand, time_format)
        self.height = height

    @classmethod
    def get_default_watch(cls):
        return cls("noname", 100, "12")

    @staticmethod
    def add(a, b):
        return a + b

    def get_instance_brand(self):
        return self.brand

    def __str__(self):
        return f'Mora watch height {self.height} with time_format: {self.time_format}'
