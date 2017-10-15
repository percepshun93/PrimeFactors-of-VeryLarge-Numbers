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
	
def highest_prime_factor(n):
   if isPrime(n):
      return n
   for x in range(2, int(sqrt(n)+1)):
      if not n % x:
         return highest_prime_factor(n/x)

fact_list = []

def isPrimeFact(n):

	for i in islice(count(1), n):
		if not n%i:
			if isPrime(i):
				fact_list.append(i)
								

num = int(input('Enter a number: '))

if len(str(num)) >= 8:
	x1 = int(highest_prime_factor(num))
	#print('Highest Prime Factor of',num,'is:',x1)
	fact_list.append(x1)	
	
	if len(str(x1)) >= 8:
			x2 = int(highest_prime_factor(x1-1))
			fact_list.append(x2)
			x3 = x2-1
			isPrimeFact(x3)
			fact_list.sort()
			print('Prime factors of',num,'are:',fact_list)
			

else:
	isPrimeFact(num)
	print('Prime factors of',num,'are:',fact_list)