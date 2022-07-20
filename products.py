products = []
with open('products.txt','r') as f:
	for line in f:
		name, price = line.strip().split(',')
		products.append([name, price])

print(products)
		
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

with open('products.txt','w') as f:
	f.write('products,price\n')
	for p in products:
		f.write(p[0]+','+p[1]+'\n')