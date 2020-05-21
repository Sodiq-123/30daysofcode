def var_sort(*args): 
    assert all([type(x)==tuple for x  in args]) and all([type(x[1])==type(x[2])==int and x[1]>0 and x[2]>0 for x in args]) and all([type(x[0])==str for x in args])
    return sorted([tuple(x) for x in args],key=lambda x: (x[0], x[1], x[2]))

print(var_sort(('Tom',19,80),('John',20,90),('Jony',17,91),('Jony',17,93)))

def error(func, name, a, s):
    try:
        return func(name, a, s)
    except AssertionError:
        return 1
print(error(var_sort, 'Tom', -1, 12))==1 # 3 points
print(error(var_sort, 6, -2, 11)) ==1 #3points