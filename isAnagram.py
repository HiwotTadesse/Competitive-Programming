class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alltrue = []
        for i in range(0,len(s)):
            alltrue.append(s[i] in t and s.count(s[i]) == t.count(s[i]))
        return True if len(s) == len(t) and all(alltrue) else False
