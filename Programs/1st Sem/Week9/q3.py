def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def rem(f):
    memo={}
    def rec(n):
        if n not in memo:
            memo[n]=f(n)
        return memo[n]
    return rec

fibo=rem(fib)
n=int(input('Enter which term of fibonacci sequence to find\n'))
print(fibo(n))