#This program is based on the idea that a prime number is always of the form 6n-1 or 6n+1,
#Where n is a whole number. So the remainder of (number-1)/6 will always be 0.
def isPrime(n):
	
	if n==0 or n==1:
		return False
	if n==2 or n==3:
		return True
		
	n_prime = n+1
	if n_prime%6==0:
		return True
		
	n_prime = n-1
	if n_prime%6==0:
		return True
		
	else:
		return False
	
		


num = int(input('Enter a number to check: '))

if isPrime(num)==True:
	print(num,' is a prime number')
else:
	print(num,' is not a prime number')
