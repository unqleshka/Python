a = float(input("введите a:"))
b = float(input("введите b:"))
c = float(input("введите c:"))
k = float(input("введите k:"))
if  a+b+c*(k-a/pow(b,3)) == 0  or b == 0 or a == 0:
	print("Деление на ноль")
else:
	print("Ответ:"+str(abs((pow(a,2)/pow(b,2)+pow(c,2)*pow(a,2))/(a+b+c*(k-a/pow(b,3)))+c+(k/b-k/a)*c)))

