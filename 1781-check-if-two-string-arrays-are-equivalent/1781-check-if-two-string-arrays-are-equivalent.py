class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        ans1 = ""
        ans2 = ""
        for i in word1: #o(n)
            ans1 +=i
        for j in word2: #O(m)
            ans2 +=j
        if ans1 == ans2: #o(k)
            return True
        else:
            return False
        
        # return "".join(word1) == "".join(word2)