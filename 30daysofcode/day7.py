def averageMultiple(num):
    '''
    A function that takes in a parameter num and checks all the values from 
    0 till the number if it's a multiple of 3 or 5
    Returns: the average of the numbers generated 
    '''
    x = [i for i in range(1, num) if i % 3 == 0 or i % 5 == 0]
    return sum(x)/len(x)

print(averageMultiple(10)) #5.75
print(averageMultiple(20))