class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums):
            ans,sums=nums[0],0
            for i in nums:
                if sums > 0:
                    sums += i                    
                else:
                    sums = i 
            ans = max(ans,sums)
            return ans
        return False


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices):
            min_in,profit = prices[0],0
            for i in prices:
                if i < min_in:
                    min_in = i
                else:
                    profit = max(profit,i-min_in)
            return profit
        return False

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(-1)
        head = l
        while(l1 and l2):
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next
        if l1:
            l.next = l1
        else:
            l.next = l2
        return head.next