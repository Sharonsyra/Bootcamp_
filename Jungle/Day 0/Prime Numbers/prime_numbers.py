def primes(n): #creates a function primes
    pr = [] #initializes the list
    if type(n) is int:
    	if n < 0:
    		return []
    	elif n > 0:
    		for num in range(2, n+1):
    			if all(num % i != 0 for i in range(2, num)):
    				pr.append(num)
    		return pr
    else:
    	raise TypeError("use an integer not a string")
    
print(primes(100))
#prints all the prime numbers to the test number.
