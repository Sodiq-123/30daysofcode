def create_arr(rowNum,colNum):
    assert type(rowNum)==int and type(colNum)==int and rowNum > 0 and colNum > 0, 'Invalid Input'
    multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

    for row in range(rowNum):
        for col in range(colNum):
            multilist[row][col]= row*col
    return multilist

def error(func, num, n):
    try:
        return func(num, n)
    except AssertionError:
        return 1
error(create_arr, 'a', -1)==1 # 3 points
error(create_arr, -1, -2) ==1 #3points