import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        closest = []
        origin = [0, 0]
        for i in range(len(points)):
            distance = math.sqrt((points[i][0] - origin[0]) ** 2 + (points[i][1] - origin[1]) ** 2)
            closest.append({i:distance})
        sorted_values = sorted(closest, key=lambda d: list(d.values()))
        
        result = []
        for i in range(k):
            result.append(points[list(sorted_values[i].keys())[0]])
        return result