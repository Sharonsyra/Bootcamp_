def data_type(rob_): 
	#creates function data_type with argument rob	
    if rob_ is None:
        return 'no value'
        # The function returns no value when there is none string value
    if isinstance(rob_, str):
        return len(rob_)
        # This returns the length of the string
    elif isinstance(rob_, bool):
        return rob_
        #It returns the boolean whether true or false
    elif isinstance(rob_, int):
    	#To check different sizes of the integer
        if rob_ < 100:
            return "less than 100"
        elif rob_ == 100:
            return "equal to 100"
        return "more than 100"
        #returns the array list and checks that the function works for small arrays
    elif type(rob_) == list:
		    if len(rob_) < 3:
			      return None
		    else:
			      return rob_[2]
			
