def fastSum(n):
    '''
    A function that takes in a parameter n
    Returns the sum of n to the nth term
    '''
    return n*(n+1)//2

print(fastSum(1_000)) #500500
print(fastSum(1_000_000_000)) #500000000500000000
print(fastSum(50_505_050)) #1275380063003775
print(fastSum(999_999_999_999_999)) #499999999999999500000000000000
print(fastSum(8_192_892_819_891_112_282_728_282)) #33561746379111670802984283972667972742780862699903
import time
a = time.time()
fastSum(8_192_892_819_891_112_282_728_282)
a = time.time() - a
print(a) #2.86102294921875e-06
