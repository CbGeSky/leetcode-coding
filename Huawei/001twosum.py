class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {nums[i]:i for i in range(len(nums))}