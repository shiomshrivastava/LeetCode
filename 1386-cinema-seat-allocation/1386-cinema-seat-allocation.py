from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        reserved = defaultdict(set)
        
        # Store reserved seats row-wise
        for row, seat in reservedSeats:
            reserved[row].add(seat)
        
        # Every completely empty row can fit 2 families
        answer = (n - len(reserved)) * 2
        
        for row in reserved:
            seats = reserved[row]
            
            left = all(seat not in seats for seat in [2, 3, 4, 5])
            middle = all(seat not in seats for seat in [4, 5, 6, 7])
            right = all(seat not in seats for seat in [6, 7, 8, 9])
            
            if left and right:
                # 2 groups: [2,3,4,5] and [6,7,8,9]
                answer += 2
            
            elif left or middle or right:
                # Only one possible group
                answer += 1
        
        return answer
        