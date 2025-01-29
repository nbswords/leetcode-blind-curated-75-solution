class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two Pointers solution
        start, end = 0, len(s) - 1
        while start < end:
            if not s[start].isalnum():
                # isalnum() : is true if the character is an alphanumeric
                # Meaning alphabets or numbers only.
                # No punctuation, no special characters
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        return True
