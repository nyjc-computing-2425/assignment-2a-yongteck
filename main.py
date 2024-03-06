num = input('Enter a number (decimal or integer): ').strip(" ")
num1 = num.replace(".","").lstrip("0")
# type your code here
sf = len(num1)
# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
