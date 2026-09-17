class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            d[c] = 1 + d.get(c, 0)
        
        for c in t:
            d[c] = d.get(c, 0) - 1

            if d[c] < 0:
                return False
        
        return sum(d.values()) == 0