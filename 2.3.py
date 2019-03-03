import random
a = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
print('Строкa из 5 символов: ')
b = ''
for i in range(5):
        b+=a[random.randint(0,32)]
print(b)
