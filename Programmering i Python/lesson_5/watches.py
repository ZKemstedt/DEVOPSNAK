class Watches:
    def __init__(self, brand, time_format="24"):
        self.time_format = time_format
        self.brand = brand
        self.value = 0

    def __str__(self):
        return f'Watch brand: {self.brand} with time_format: {self.time_format}'
