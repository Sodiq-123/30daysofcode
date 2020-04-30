def is_even(num):
    if num % 2 == 0:
        return True
    return False

def even_odd(list_num):
    even = [i for i in list_num if is_even(i)]
    return(f'number of even numbers is {len(even)}\nnumber of odd numbers is {len(list_num) - len(even)}')

print(even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18]))
print(even_odd(range(10, 35)))