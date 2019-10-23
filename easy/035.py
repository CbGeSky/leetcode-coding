class Solution:
    '''
    可以说冒出来的第二个想法就是二分查找了
    date:2019-10-23
    '''
    # def searchInsert(self, nums: List[int], target: int) -> int:
    def searchInsert(self, nums, target: int) -> int:
        try :
            left,right=0,len(nums)
            middle = (left+right) // 2
            while((right-left)>1):                
                if nums[middle] > target:
                    right = middle
                elif nums[middle] < target:
                    left = middle
                else:
                    return middle
                middle = (left+right) // 2
            # 这个地方边界条件还是要另外判断，能不能统一？
            if nums[left]>= target:
                return left
            else:
                return left+1
        except Exception as EnvironmentError:
            pass

if __name__ == "__main__":
    test = Solution()

    nums=[1,3,5,6]
    target = 3

    print(test.searchInsert(nums,target))
    print("finished!")