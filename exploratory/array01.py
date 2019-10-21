# 中心索引
# easy 724
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums):
            total = sum(nums)
            current = 0
            last = 0 #这个last的加入是的下面的循环可以从0开始
            for i in range(len(nums)):
                check = (total - nums[i]) / 2
                current += last
                last = nums[i]
                if current == check:
                    return i                    
            # if sum(nums[0:len(nums)-1])==0:
            #    return len(nums)-1
            return -1
        return -1


# sum函数会超时，循环里面一个sum都不能有
# 所以，想到了能不能把和存下来，每次只做一次加法运算
# 边界条件每次都好烦，两个方面
### 1数组长度的边界条件
### 2循环起始的边界条件