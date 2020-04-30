def is_perfect_square(number):
    for i in range(number//2):
        if i * i == number:
            return True
    return False

print(is_perfect_square(9))