class Solution:
    # solution #2 0902
    
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

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            x = int(line);
            
            ret = Solution().reverse(x)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

