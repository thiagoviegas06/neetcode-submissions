class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointerA = 0
        pointerB = len(s) - 1

        while pointerA < pointerB:
            if not s[pointerA].isalnum():
                pointerA += 1
                continue

            if not s[pointerB].isalnum():
                pointerB -= 1
                continue

            if s[pointerA].lower() != s[pointerB].lower():
                return False

            pointerA += 1
            pointerB -= 1

        return True
        