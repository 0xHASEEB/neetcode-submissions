class Solution:
    def isPalindrome(self, s: str) -> bool:
        f, b = 0, len(s)-1
        while f <= b:
            if s[f].isalnum():
                if s[b].isalnum():
                    if s[f].lower() != s[b].lower():
                        return False
                    else:
                        f += 1
                        b -= 1
                else:
                    b -= 1
            else:
                f += 1
        return True
