try:
	i=float(input('Введите температуру: '))
	x='ХОЛОДНО' if i<15.5 else ('НОРМАЛЬНО' if i < 28 else 'ЖАРКО')
	print (x)
except ValueError:
	print ('Неправильный формат числа')

