class Solution:
    # solution #1 0902
    def isPalindrome(self, x: int) -> bool: 
        import math
        if x < 0:
            return False
        if x == 0:
            # 这个会导致math.log报错
            return True
        n = math.floor(math.log(x,10))
        head = x // (10**n)
        tail = x % 10
        while( head==tail ):
            x = (x - head*10**n) // 10
            n = n-2
            head = x // (10**n)
            tail = x % 10 
            if head==tail:
                if x <10:
                    return True
                else:
                    continue
            else:
                break
        return False

    # solution #2 0903
    def isPalindrome(self, x: int) -> bool: 
        import math
        if x < 0 or (x%10 ==0 and x !=0):
        # 这个地方的特殊判断一直没搞出来
        # 而且其实只有X0这几个特例会出问题
        # 别的两位数都没问题
            return False
        out = 0
        out = out*10 + x % 10
        x = x // 10
        while( x > out ):
            out = out*10 + x % 10
            x = x // 10
        if x==out or (out // 10)==x:
            return True
        else:
            return False
        

