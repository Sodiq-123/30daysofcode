def is_perfect_square(number):
    '''
    A function that takes in a parameter number and checks if it is a prime number.

    Returns:True if perfect square and False not. 
    '''
    for i in range(number//2):
        if i * i == number:
            return True
    return False
def is_even(num):
    '''
    A function that checks if a given number is even.

    Returns True if the number is even and False if otherwise.
    '''
    if num % 2 == 0:
        return True
    return False

def isfib(number):
    return is_perfect_square(int(5*number*number + 4)) or is_perfect_square(int(5*number*number - 4))

def fibSum(number):
    if number == 0: return 0
    if number < 1: return "Invalid, number can't be negative"
    if not isinstance(number, int): return "Invalid input, number must be positive integer"
    return sum(list(i for i in range(number+1) if isfib(i) and is_even(i)))

print(fibSum(10))