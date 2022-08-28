import math
class Solution:
    def reverse(self, x: int) -> int:
    
        num_string = str(x)
        y = num_string[len(num_string)::-1]
        if x < 0:
            y = num_string[len(num_string):0:-1]
            y = int(y)*-1
        return int(y) if int(y) in range(-2**31, 2**31-1) else  0
