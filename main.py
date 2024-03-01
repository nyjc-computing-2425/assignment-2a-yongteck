num = input('Enter a number (decimal or integer): ').split()[0]
# type your code here
sf = 0
nums = "123456789"
place = 0
while num[place] not in nums: #looks past the leading 0s
  place += 1
if float(num) < 1:
    sf = len(num) - place
else:
    sf = len(num) - 1 - place #12.01 sf is 4

# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
