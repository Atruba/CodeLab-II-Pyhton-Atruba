for FizzBuzz in range(101):
    if FizzBuzz % 5 == 0 and FizzBuzz % 3 == 0:
        print("FizzBuzz")
        continue
    elif FizzBuzz % 5 == 0:
        print("Buzz")
        continue
    elif FizzBuzz % 3 == 0:
        print("Fizz")
        continue
    print(FizzBuzz)