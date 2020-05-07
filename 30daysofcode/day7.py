def averageMultiple(num):
    '''
    
    '''
    x = [i for i in range(1, num) if i % 3 == 0 or i % 5 == 0]
    return sum(x)/len(x)

print(averageMultiple(10))