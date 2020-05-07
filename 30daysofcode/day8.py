def fastSum(n):
    '''
    A function that takes in a parameter n
    Returns the sum of n to the nth term
    '''
    return n*(n+1)//2

print(fastSum(1_000)) #500500
print(fastSum(1_000_000_000)) #500000000500000000