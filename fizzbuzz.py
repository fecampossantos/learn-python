def fizzbuzz(x):
    if x % 3==0 and x % 5==0:
        return ("FizzBuzz")
    else:
        if x % 3==0 and not x % 5==0:
            return ("Fizz")
        if not x % 3==0 and x % 5==0:
            return ("Buzz")
        if x % 3 != 0 and x % 5 != 0:
            return (x)
