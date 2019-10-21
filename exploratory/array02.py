class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        Max = 0
        maxI= 0
        SecMax = 0
        # if len(nums)>1:
        # 这边有个测试用例
        # input: [1]  output:0 这就看怎么理解了
        if len(nums):
            for i in range(len(nums)):
                if nums[i]>Max:
                    SecMax = Max
                    Max = nums[i]
                    maxI= i
                elif nums[i]> SecMax:
                    SecMax = nums[i]
            if Max >= 2*SecMax:
                return maxI
            return -1
        return -1 

# 这边有个测试用例
# input: [1]  output:0 这就看怎么理解了