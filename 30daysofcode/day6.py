def is_prime(num):
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
    sum_primes = [i for i in range(num) if is_prime(i)]
    return sum(sum_primes)

print(primeSum(10))
print(primeSum(20))
print(primeSum(100))
print(primeSum(1000000))