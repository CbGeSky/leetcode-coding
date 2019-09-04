# 020 有效的括号
'''
题目的描述里说，
有效字符串需满足：
1、左括号必须用相同类型的右括号闭合。
2、左括号必须以正确的顺序闭合。
so，何为 正确的顺序 ？
'''
class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(','{','[']
        right = [')','}',']']
        value = {'(':1,'{':2,'[':3,')':1,'}':2,']':3}
        stack = []
        l = len(s)
        if l == 0:
            return True
        if s[0] in right or l ==1:
            return False
        stack.append(s[0])
        i = 1
        while(i<l):
            if ( s[i] in right ):
                if len(stack)!=0 and value[s[i]] == value[stack[-1]]:
                    i += 1
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
                i += 1
        if len(stack)==0:
            return True
        else:
            return False
                
            
        