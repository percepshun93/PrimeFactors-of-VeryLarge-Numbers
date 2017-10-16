# PrimeFactors-of-VeryLarge-Numbers
Python 3 code for finding the all the prime factors of numbers containing 0-15 digits.

Define a function to check if a number is prime or not - isPrime(n)
Define a function to find the factors of a number which are also prime - isPrimeFact(n)
Define a function to find the largest prime of a very large number - highest_prime_factor(n)

Essentially if a number has less than 8 digits, python on a normal computer can process it quite fast. So i use the isPrime and isPrimeFact functions to get a list of all prime factors easily

The problem comes when there is a number with over 8 digits. 
In such cases, first find the highest prime factor of that number using the highest_prime_factor() function, then find the number of primes upto that number. If the highest prime number also has greater than 8 digits, then repeat this process again.
