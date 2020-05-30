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

    def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

# 1 point for submission
# a = ArrayOperation()
# print(a.twoSum((10,20,10,40,50,60,70), 50)==((2, 3))) #2 points
# print(a.twoSum([10,20,10,40,50,60,70], 50)==(2, 3)) #2 points
# print(a.threeSum((10,20,10,40,50,60,70))==[]) #2 points
# b = ArrayOperation()
# print(b.threeSum([-25, -10, -7, -3, 2, 4, 8, 10])==[[-10, 2, 8], [-7, -3, 10]]) #3 points
# print(b.threeSum([-25, -10, -7, -3, 2, 4, 8, 10, 6, -9, 4, -10, 7, 65, -55])==[[-55, -10, 65], [-10, 2, 8], [-10, 4, 6], [-9, 2, 7], [-7, -3, 10]]) #5 points