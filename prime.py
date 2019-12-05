def prime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            print(i)
            if (num % i) == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")


prime(2)
prime(4)
prime(13)
prime(25)
