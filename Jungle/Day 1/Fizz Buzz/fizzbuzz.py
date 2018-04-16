def fizz_buzz(rob):
  
  if rob%15 == 0:  
    return "FizzBuzz"

  elif rob%3==0:
    return "Fizz"

  elif rob%5==0:
    return "Buzz"

  else:
    return rob
