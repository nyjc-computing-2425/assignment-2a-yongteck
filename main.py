num = input('Enter a number (decimal or integer): ').strip(" ").lstrip("0")
# type your code here
sf = len(num.replace(".",""))
# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
