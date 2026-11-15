class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars_in_s = {}
        chars_in_t = {}

        for i in range(len(s)):
            chars_in_s[s[i]] = chars_in_s.get(s[i], 0) + 1
            chars_in_t[t[i]] = chars_in_t.get(t[i], 0) + 1

        return chars_in_s == chars_in_t