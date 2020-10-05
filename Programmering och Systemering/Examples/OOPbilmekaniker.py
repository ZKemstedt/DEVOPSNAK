from typing import Any


class Car(object):
    def __init__(self, state: bool = True, owner: Any = None):
        self.state = state
        self.owner = owner

    def set_working(self):
        self.state = True

    def set_broken(self):
        self.state = False

    def set_owner(self, owner: Any = None):
        self.owner = owner


class Mechanic(object):

    def __init__(self, invoice_template: str, repair_cost: int):
        self.invoice_template = invoice_template.format(repair_cost)
        self.repair_cost = repair_cost

    def fix_car(self, car):
        car.set_working()
        car.owner.receive_invoice(text=self.invoice_template, cost=self.repair_cost)


class Customer(object):
    def __init__(self, name: str = 'Robert', car: Car = None):
        self.name = name
        self.car = car

    def add_car(self, car: Car):
        self.car = car
        self.car.set_owner(self)

    def receive_invoice(self, text: str, cost: int):
        print(f'Customer {self.name} just received an invoice.')
        print(f'{text}')


if __name__ == "__main__":
    mechanic = Mechanic(
        invoice_template='you need to pay {} for your car',
        repair_cost=5000)

    customer = Customer()
    customer.add_car(Car(state=False))
    mechanic.fix_car(customer.car)
