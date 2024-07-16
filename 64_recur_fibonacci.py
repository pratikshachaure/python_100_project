def sum_fibonacci(n, first=0, second=1):
    if n > 0:
        print(first,"      ")
        third = first + second
        first = second
        second = third
        sum_fibonacci(n-1, first, second) 
sum_fibonacci(10)
