class Transport:
    def __init__(self, move_type, size):
        self.move_type = move_type
        self.size = size

    def __str__(self):
        return (f'Transport {self.move_type}, {self.size}')



class Auto(Transport):
    def __init__(self, auto_type, size):
        super().__init__('Automobiles', size)
        self.auto_type = auto_type

    def __str__(self):
        return f'{super().__str__()} {self.auto_type}'


class Plain(Transport):
    def __init__(self, plain_type, size):
        super().__init__('Plains', size)
        self.plain_type = plain_type
        self.in_air = False

    def start_fly(self):
        self.in_air = True
        print(f'Plain {self.plain_type} start flying')


car = Auto("Sedan", "Medium")
plain = Plain("Airbus", "Large")
print(car)
print(plain.start_fly())
