def is_perfect_square(number):
    '''
    A function that takes in a parameter number and checks if it is a prime number.

    Returns:True if perfect square and False not. 
    '''
    for i in range(number//2):
        if i * i == number:
            return True
    return False

def fibonacci(number):
    return is_perfect_square(int(5*number*number + 4)) or is_perfect_square(int(5*number*number - 4))

print(fibonacci(100))