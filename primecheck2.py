from math import sqrt
from itertools import count, islice


def isPrime(n):
	if n<2:
		return False
	if n==2:
		return True
	
	for i in islice(count(2), int(sqrt(n)-1)):
		
		if not n%i:
			return False
			
	return True
	
num = int(input('Enter a number: '))
x = isPrime(num)

if x:
	print(num, ' is a prime number')
	
if not x:
	print(num, ' is NOT a prime number')