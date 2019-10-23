class Solution:
    '''
    date:2019-10-23
    递归就没必要强行上了，就是递推，一个个字符的count第n个串得到第n+1个
    那么主体问题就分成了两部分，一个是字符串统计连续相同字符个数count，然后递推
    '''
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for i in range(n-1):
            count,new,char = 0,[],ans[0]
            for j in range(len(ans)):
                if (ans[j]==char):
                    count +=1
                    continue
                new.append(str(count))
                new.append(char)
                char,count =ans[j],1
            new.append(str(count))
            new.append(char)
            ans_new = ''
            for c in new:
                ans_new += c
            ans = ans_new
        return ans

def test_func(ans):
    '''
    主体的字符串统计连续相同字符个数统计
    count函数，这次的边界问题解决得还可以
    可能两个append可以统一成一个，加上else结构清晰一点
    另外最后得那个for 循环也许有别的写法
    '''
    count,new,char = 0,[],ans[0]
    for j in range(len(ans)):
        if (ans[j]==char):
            count +=1
            continue
        new.append(str(count))
        new.append(char)
        char,count =ans[j],1
    new.append(str(count))
    new.append(char)
    ans_new = ''
    for c in new:
        ans_new += c
    return ans_new

if __name__ == "__main__":
    test = Solution()
    n = 1
    # ans = '1'
    # print(test_func(ans))
    # print("finished!")
    print(test.countAndSay(n)) 
    print("finished!")   
