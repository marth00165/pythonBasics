def fizzbuzz(num):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(None)


fizzbuzz(9)
fizzbuzz(20)
fizzbuzz(30)
fizzbuzz(4)

