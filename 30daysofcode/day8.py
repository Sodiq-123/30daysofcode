def fastSum(n):
    '''
    A function that takes in a parameter n
    Returns the sum of n to the nth term
    '''
    return n*(n+1)//2

print(fastSum(1_000)) #500500
print(fastSum(1_000_000_000)) #500000000500000000
print(fastSum(50_505_050))
print(fastSum(999_999_999_999_999))
print(fastSum(8_192_892_819_891_112_282_728_282))
import time
a = time.time()
fastSum(8_192_892_819_891_112_282_728_282)
a = time.time() - a
print(a)
