class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
#         distance = []
#         l = []
#         for i in points:
#             if i[0] == x or i[1] == y:
#                 dx = abs(i[0] - x)
#                 dy = abs(i[1] - y)
#                 dist = dx + dy
                
#                 l.append(i)
#                 distance.append(dist)
        
                
#         print(min(distance))
            
# #         print(l)
        
#         if len(distance) != 0:
#             print(l.index(distance[0]))
#         else:
#             print(-1)
        distance, idx = float('inf'), -1
        
        for i, (a,b) in enumerate(points):
            if a == x or b == y:
                dist = abs(a - x) + abs(b - y)
                if dist < distance:
                    idx = i
                    distance = dist

        return idx
