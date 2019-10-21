class Solution:
    # 最后一个测试用例，超时了，过不去
    def strStr(self, haystack: str, needle: str) -> int:
        sh = 0
        sn = 0
        if len(needle)==0:
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                sh = i
                sn = 0
                while(sn < len(needle) and sh < len(haystack) ):
                    if haystack[sh] == needle[sn]:
                        sn += 1
                        sh += 1
                    else:
                        break
                if sn == len(needle):
                    return i
        return -1 

class Solution:
    # ac 10月13日
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        try:
            return haystack.index(needle)
        except ValueError :
            return -1
        return -1

class Solution:
    # ac 10月13日
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        len_t = len(needle)
        if len(haystack)>=len(needle):
            for i in range(len(haystack) - len_t+1):
                if haystack[i] == needle[0]:
                    ix,j=i,0
                    while(j<len_t and (haystack[ix]==needle[j])):
                        ix+=1
                        j+=1
                    if j==len_t:
                        return i
                    else:
                        continue
        return -1
