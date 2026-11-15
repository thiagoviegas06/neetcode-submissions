class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_in_s = {}
        chars_in_t = {}

        size_s = len(s)
        if size_s != len(t):
            return False

        for i in range(size_s):
            char_s = s[i]
            char_t = t[i]

            if char_s not in chars_in_s:
                chars_in_s[char_s] = 1

            else:
                chars_in_s[char_s] += 1

            if char_t not in chars_in_t:
                chars_in_t[char_t] = 1
            else: 
                chars_in_t[char_t] += 1

        for key, val in chars_in_s.items():
            if chars_in_t.get(key) != val:
                return False
        return True
        

        