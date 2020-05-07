def is_prime(num):
    '''
    A function that takes in a parameter and checks if it is a prime number

    Returns: True if num is prime and False if num is not prime.
    '''
    if num > 1:
        if num == 2:
            return True
        if num % 2 != 0:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        else: 
            return False
    return False

def primeSum(num):
    '''
    A function that takes in a parameter num and gets the prime numbers using the is_prime function from
    1 to the number.
    Returns: The sum of the prime numbers in that range 
    '''
    sum_primes = [i for i in range(num) if is_prime(i)]
    return sum(sum_primes)

print(primeSum(10)) #17
print(primeSum(20)) #77
print(primeSum(100)) #1060
print(primeSum(1000000)) #37550402023