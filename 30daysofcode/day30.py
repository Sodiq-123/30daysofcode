'''
    Define a python class ArrayOperation that has two methods twosum and threesum
    Both methods should take in an array of numbers(i.e either a tuple or a list)
    The first method twosum should take in two parameters 
    which is the array and the target and find a pair of elements 
    (indices of the two numbers) as a tuple from the given array whose
    sum equals to the target number.
    The second method threesum should take in one parameter as an array 
    and find the three elements as a pair in a list of list 
    from the given array that sum to zero in the array.
    NOTE: 
    1) In method threesum, the array can take in both positive and negative numbers
    and they must be integers only.
    2) In method threesum, it can be more then one pair that sums up to zero. therefore the output 
    should be list of lists as the case may be.
    3) Your function should return an empty array if the array does not reach the condition
   '''

class ArrayOperation:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i
        return tuple(lookup)

    def threeSum(self, nums, k=0):
        return list(map(list, set([tuple(sorted([x,y,z])) 
                    for (i,x) in enumerate(nums) 
                    for (j,y) in enumerate(nums) 
                    for (l,z) in enumerate(nums) 
                    if i > j > l and x+y+z == k])))

# 1 point for submission
a = ArrayOperation()
print(a.twoSum((20,10,40,50,60,70), 50)==(1, 2)) #2 points
print(a.twoSum([10,20,10,40,50,60,70], 50)==(2, 3)) #2 points
print(a.threeSum((10,20,10,40,50,60,70))==[]) #2 points
b = ArrayOperation()
print(b.threeSum([-25, -10, -7, -3, 2, 4, 8, 10])==[[-7, -3, 10], [-10, 2, 8]]) #3 points
print(b.threeSum([-25, -10, -7, -3, 2, 4, 8, 10, 6, -9, 4, -10, 7, 65, -55])==[[-9, 2, 7], [-10, 4, 6], [-10, 2, 8], [-7, -3, 10], [-55, -10, 65]]) #5 points

