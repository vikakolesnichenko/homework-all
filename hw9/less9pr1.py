import math
number = int(input('Please enter a number: '))
floors = 9
entrance = 4
number_of_apartments_per_floor = 4

def my_func(number):

 appartments_per_entrsnce = number_of_apartments_per_floor * floors
 result_entrace = math.ceil(number / appartments_per_entrsnce)
 print('Entrance: ' + str(result_entrace))
 result_floor = (result_entrace * appartments_per_entrsnce - number) // number_of_apartments_per_floor
 print('Floor: ' + str(floors - result_floor))

my_func(number)