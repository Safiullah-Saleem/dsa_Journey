class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #return len(s.strip().split()[-1])
        extra_space = len(s.strip().split()[-1])
        return extra_space