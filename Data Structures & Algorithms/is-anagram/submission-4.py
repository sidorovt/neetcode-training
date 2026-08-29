class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) == len(t):
            for ch in s:
                if ch not in hashmap:
                    hashmap[ch] = 0
                hashmap[ch] += 1
            
            for ch in t:
                if ch not in hashmap or hashmap[ch] != t.count(ch):
                    return False
            
            return True
        
        return False
