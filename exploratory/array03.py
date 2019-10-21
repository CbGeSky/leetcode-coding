class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # l = len(digits)
        num = 0 
        for i in digits:
        # 这里list是可以直接迭代的，写多了range容易搞错
            num = num*10+int(i)
            # 这个10进制的相互转换都写错了
        num += 1
        ans = []
        while(num!=0):
            ans.append(num % 10)
            num = num // 10
        return reversed(ans)
