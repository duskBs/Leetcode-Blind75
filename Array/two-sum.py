class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, item in enumerate(nums):
            if((target - item) in dict):
                return [i, dict[target-item]]
            dict[item] = i
        if((target - item) in dict):
                return [i, dict[target-item]]
