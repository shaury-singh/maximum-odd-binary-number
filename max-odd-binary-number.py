class Solution:
    def noOfOnes(s:str) -> int:
        Ones = 0
        for i in s:
            if i == '1':
                Ones += 1
        return Ones
    def maximumOddBinaryNumber(self, s: str) -> str:
        NoOfOnes = Solution.noOfOnes(s)
        s = list(s)
        out = ""
        if NoOfOnes == 0:
            return 0
        if NoOfOnes == 1:
            for i in range(len(s)-1):
                s[i] = '0'
                out = out + s[i]
            s[len(s)-1] = '1'
            out = out + s[len(s)-1]
            return out
        else:
            NoOfOnes = NoOfOnes-1
            i = 0
            while i<NoOfOnes:
                s[i] = '1'
                i+=1
            for j in range(i,len(s)-1):
                s[j] = '0'
            s[len(s)-1] = '1'
            for m in range(len(s)):
                out = out + s[m]
            return out 
