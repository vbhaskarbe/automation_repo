from collections import namedtuple

Car = namedtuple('Car', 'color mileage automatic')

car1 = Car('red', 3812.4, True)

print car1

print car1.mileage

car1.mileage = 12


