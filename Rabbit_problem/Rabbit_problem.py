"""def rabbits(n,k):
    if n==1:
        return 1
    if n==2:
        return k
    onegen=rabbits(n-1,k)
    twogen=rabbits(n-2,k)

    if n<=4:
        return onegen+twogen

    return onegen+twogen*k


"""
def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in xrange(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)

print fib(93,18)