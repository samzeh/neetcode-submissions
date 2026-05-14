class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = {}
        myDict2 = {}
        for i in s:
            if i not in myDict:
                myDict[i] = 1
            else:
                myDict[i] += 1
        
        for j in t:
            if j not in myDict2:
                myDict2[j] = 1
            else :
                myDict2[j] += 1
        
        return myDict == myDict2

        