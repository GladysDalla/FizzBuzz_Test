def fizz_buzz(num):
  """ This returns outputs depending on the argument received """
  if num % 3 == 0:
    return "Fizz"
  elif num % 5 == 0:
    return "Buzz"
  elif (num % 3 == 0) and (num % 5 == 0):
    return "FizzBuzz"
  else:
    return num