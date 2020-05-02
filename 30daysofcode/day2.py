def missing_numbers(num_list):
    '''
    A function that takes in a parameter num_list and checks for the missing numbers in the list
    according to preference.

    Returns: a sorted list of the missing values of num_list
    '''
    missing_values = [x for x in range(min(num_list), max(num_list) + 1) if x not in num_list]
    return missing_values

print(missing_numbers([1,2,3,4,6,7,10])) #[5, 8, 9]
print(missing_numbers([10,11,12,14,17])) #[13, 15, 16]