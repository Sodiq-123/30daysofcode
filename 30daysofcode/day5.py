def unique(L):
    return f'Sample List: {L}\nUnique List: {list(set(L))}'


print(unique([1,2,3,3,3,3,4,5]))
print(unique([1,2,3,3,3,3,4,5,3,3,3,3,4,5,6,6,11,22,33,44]))
print(unique([1,2,3,3,3,3,4,5,5,3,3,3,3,4,5,6,6,11]))