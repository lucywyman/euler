def fib():
    x = 1
    y = 1
    total = 0
    while y<4000000:
        old = y
        y = x + old
        x = old
        if y%2 == 0:
            total = total+y
    print total

fib()
        
        
