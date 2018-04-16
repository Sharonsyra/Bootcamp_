def data_type(rob): 
	#creates function data_type with argument rob	
    if rob is None:
        return 'no value'
        # The function returns no value when there is none string value
    if isinstance(rob, str):
        return len(rob)
        # This returns the length of the string
    elif isinstance(rob, bool):
        return rob
        #It returns the boolean whether true or false
    elif isinstance(rob, int):
    	#To check different sizes of the integer
        if rob < 100:
            return "less than 100"
        elif rob == 100:
            return "equal to 100"
        return "more than 100"
        #returns the array list and checks that the function works for small arrays
    elif type(rob) == list:
		    if len(rob) < 3:
			      return None
		    else:
			      return rob[2]
			  
