
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target :
                    return [i,j]
        return []
    
class Solution_2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        n = len(nums)

        for i in range(n):
            diff = target - nums[i]
            if diff in map:
                return [map[diff],i]
            map[nums[i]] = i
        return []
    
nums = [2,7,11,15]
target = 26

sol1 = Solution()
sol2 = Solution_2()
print(sol1.twoSum(nums, target))
print(sol2.twoSum(nums, target))