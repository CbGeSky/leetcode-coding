# 014 最长公共前缀
'''
1、注意"前缀"，意味着必然从头开始
2、利用python具有str cmp的机制进行sorted
3、找到最短的一个，和sorted后的头尾对比得到结果
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minL = 10000
        minS = ''
        prefix = ''
        if len(strs)==0 or ('' in strs):
            return prefix
        sort_strs = sorted(strs)
        for s in sort_strs:
            if len(s) < minL:
                minL = len(s)
                minS = s
        headS = sort_strs[0]
        tailS = sort_strs[-1]
        c = 0
        while(c<minL and (headS[c] == tailS[c])):
        # 这里有个小细节，利用了and判断的机制(先左后右)
        # 先判断长度再取值判断
        # 不会报index out of range的问题
        # 这个是单个字符的时候卡了一下
            if headS[c]==minS[c]:
                prefix += headS[c]
                c += 1
            else:
                break
        return prefix