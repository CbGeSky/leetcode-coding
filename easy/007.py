class Solution:
    # solution #2 0902
    def reverse(self, x: int) -> int:
        signed = 0
        out = 0
        if x < 0:
            signed = 1
            x = abs(x)
        while( x !=0):
            out = out*10 + x % 10
            x = x // 10
        if signed:
            out = - out 
        if out > 2**31-1 or out < -2**31:
            return 0
        else:
            return out

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

'''
solution #1
class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)
        l = len(a)
        if a[0] == '-':
            os = '-' + a[l:0:-1].lstrip('0')
        elif x > 0:
            os =  '' + a[l::-1].lstrip('0')
        else:
            return 0
        output = int(os)
        if output > 2**31-1 or output < -2**31:
            return 0
        else:
            return output
'''