# 013 罗马数字转整数
'''
1、首先是7个字符和数值的对应，可以用字典
2、正常规则，左大右小每个字符对应数值直接相加
3、特例规则，条件，左小右大，合为一个数字，大减小
'''
# 一遍过 2019-09-03
class Solution:
    def romanToInt(self, s: str) -> int:
        map_table ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        value = 0
        i = 0
        l = len(s)
        while(i < l-1):
            rule = map_table[s[i]]<map_table[s[i+1]]
            if rule:
                value += (map_table[s[i+1]] - map_table[s[i]])
                i+=2
            else:
                value += map_table[s[i]]
                i+=1
        if i == l-1:
            value += map_table[s[i]]
        return value