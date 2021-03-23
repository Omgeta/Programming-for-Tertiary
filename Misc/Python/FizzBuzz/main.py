for x in range(100):
    r = ""
    
    if x % 3 == 0:
        r += "Fizz"
    if x % 5 == 0:
        r += "Buzz"
    r = x if not r

    print(r)