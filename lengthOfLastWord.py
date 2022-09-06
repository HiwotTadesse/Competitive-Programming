class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        striped = s.strip()
        splited = striped.split(' ')
        return len(splited[len(splited)-1])