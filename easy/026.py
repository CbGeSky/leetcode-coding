class Solution:
    '''
    26.删除排序数组中的重复项
    要求是O(1)的空间复杂度，原地修改数组
    想法是第一步遍历找重复值标记出来，同时确定了长度，注意这里的顺序是倒着来的
    第二步用的是ix记录标记位置，也就是需要覆盖的位置
    后面看题解，这两步可能可以用双指针合到一起，

    有个问题，每次0，1两种特殊情况都要单独考虑，能不能至少融合一种呢？
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)>1:
            length = len(nums)
            flag = nums[0]-1
            for i in range(len(nums)-1):
                if nums[i]==nums[i+1]:
                    nums[i]=flag
                    length -= 1
            ix = 0
            for i in range(len(nums)):
                
                if ix<length and nums[i] > flag:
                    # swap
                    nums[ix],nums[i]=nums[i],nums[ix]
                    ix +=1
            return length

        if len(nums):
            return 1
        else:
            return False