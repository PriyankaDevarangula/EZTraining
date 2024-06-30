#Top down approach

def fibonacci(n, memo = {}):
    if n <= 2: 
        return 1
    elif n in memo: 
        return memo[n]
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

print(fibonacci(10))

#Bottom up approach

def fibonacci(n):
    fib_table = [0, 1] + [0]*(n-1)

    for i in range(2, n+1):
        fib_table[i] = fib_table[i-1] + fib_table[i-2]

    return fib_table[n]

print(fibonacci(10))