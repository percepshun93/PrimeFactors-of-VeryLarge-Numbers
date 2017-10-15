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
	
fact_list = []

def isFact(n):

	for i in islice(count(1),n):
		if not n%i:
			fact_list.append(i)
	

num = int(input('Enter a number: '))

isFact(num)

prime_fact_list= list(filter(isPrime,fact_list))

print('The prime factors of ',num,'are: ',prime_fact_list)

