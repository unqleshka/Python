import random
my_number=random.randint(-100,100)
user_number = int(input("Введите Число: "))
while my_number <= user_number:
    user_number = int(input("Введите Число: "))
print('Вы угадали число, которое меньше ' + str(my_number))
