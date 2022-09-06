class Solution:
    def isPalindrome(self, x: int):
        if x<0:
            return False
        else:
            z = [int(y) for y in str(x)]
            a = z[::-1]
            if(len(a)==sum([1 for i,j in zip(a,z) if i==j])):
                return True

            else:
                return False