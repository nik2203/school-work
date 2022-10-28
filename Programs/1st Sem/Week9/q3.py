def fib(n):
    if n==0:#base condition
        return 0
    if n==1:#base condition
        return 1
    else:
        return fib(n-1)+fib(n-2)#recursive statement

def rem(f):
    memo={}
    def rec(n):
        if n not in memo:
            memo[n]=f(n)
        return memo[n]
    return rec

fibo=rem(fib)
n=int(input('Enter which term of fibonacci sequence to find\n'))
print(fibo(n))#recursive call