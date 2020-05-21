def create_arr(rowNum,colNum):
    assert type(rowNum)==int and type(colNum)==int and rowNum > 0 and colNum > 0, 'Invalid Input'
    multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

    for row in range(rowNum):
        for col in range(colNum):
            multilist[row][col]= row*col
    return multilist