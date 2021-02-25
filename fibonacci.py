# CS362_Winter21
# Class Activity
# Program: fibonacci.py
# Author: Kwanghyuk Kim

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);

def fibonacci(n):
	a = 0
	b = 1

	if n < 0:
		print("Invalid input!")
		
	elif n == 0:
		return 0
	
	elif n == 1:
		return b

	else:
		for i in range(1, n):
			c = a + b
			a = b
			b = c
		return b
        

num = 5;

print(factorial(num))

for i in range(num + 1):
       print(fibonacci(i), end=" ")

