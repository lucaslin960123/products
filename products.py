import os

def read_file(filename):
	products = []
	with open(filename,'r') as f:
		for line in f:
			if 'products,price' in line:
				continue
		name, price = line.strip().split(',')
		products.append([name, price])
	return products
			
def user_input(products):		
	while True:
		name = input('Enter name of the products:')
		if name == 'q':
			break
		else:
			price = input('Enter the price if the products:')
			p = []
			p = [name, price]
			products.append(p)
	print(products)
	return products

def print_products(products):
	for p in products:
		print(p[0],'cost',p[1])

def write_file(filename,products):
	with open(filename,'w') as f:
		f.write('products,price\n')
		for p in products:
			f.write(p[0]+','+p[1]+'\n')

def main():
	filename = 'products.txt'
	if os.path.isfile(filename):
			print('Found the file')
			products = read_file(filename)

	else:
		print('Did not find the file')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()