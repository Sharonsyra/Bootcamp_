def primes(n): #creates a function primes
    prime = [] #initializes the list
    if type(n) is int:
    	if n <= 1:
    		return []
    	elif n > 1:
    		for num in range(2, n+1):
    			if all(num % i != 0 for i in range(2, num)):
    				prime.append(num)
    		return prime
    else:
    	raise TypeError("use an integer not a string")
        
    
