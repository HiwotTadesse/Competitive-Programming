import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^a-zA-Z0-9]+'
        x = re.sub(pattern, '', s).lower()
        if x == x[::-1]:
            return True
        else:
            return False