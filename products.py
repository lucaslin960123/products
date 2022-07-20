products = []
while True:
	name = input('Enter name of the products:')
	if name == 'q':
		break
	else:
		price = input('Enter the price if the products:')
		p = []
		p = [name, price]
		products.append(p)

for p in products:
	print(p[0],'cost',p[1])