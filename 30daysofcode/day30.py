'''
    Define a python class ArrayOperation that has two methods twosum and threesum
    Both methods should take in an array of numbers
    The first method twosum should take in the two parameters 
    which is the array and the target and find a pair of elements 
    (indices of the two numbers) from the given array whose
    sum equals to the target number.
    The second method threesum should take in the parameter array 
    and find the three elements as a pair from a given array that 
    sum to zero from the array.
    NOTE: 
    1) In method threesum, the array can take in both positive and negative numbers
    and they must be integers only.
    2) In method two, it can be more then one pair that sums up to zero.
   '''

class ArrayOperation:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        pass

    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i )
            lookup[num] = i
        return lookup

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

a = ArrayOperation((10,20,10,40,50,60,70), 50)
print(a.twoSum())

