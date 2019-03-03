import random
a = '1ЙЦУКЕНГфвфаШ2ЩЗХЪФЫ3ВАdsfsfQEWRПРОЛДЖЭЯЧ4СМИТЬБЮ5Ё'
print('Строкa из Чисел: ')
b = ''
for i in a:
    if ord(i) >= 48 and ord(i) <= 57:
        b+=i
print(b)
