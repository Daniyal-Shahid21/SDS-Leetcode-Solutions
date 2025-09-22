#https://leetcode.com/problems/percentage-of-letter-in-string/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        letters = defaultdict(int)
        for i in s:
            letters[i] += 1
        return math.floor((letters[letter])/(sum(letters.values()))*100)
    
"""
Notes/Realizations
 - This one was pretty straightforward and easy.
"""