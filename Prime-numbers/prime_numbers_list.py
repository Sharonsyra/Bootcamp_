def primes(n): #creates a function primes
    prime = [] #initializes the list
    if type(n) is int: #only takes integers
    	if n < 2: #n starts from 2
    		return [] 
    	elif n > 1: 
    		for num in range(2, n+1): # from 0 to n
    			if all(num % i != 0 for i in range(2, num)): 
    				prime.append(num)
    		return prime
    else:
    	raise TypeError("use an integer not a string") #raises error when a string is used
    
