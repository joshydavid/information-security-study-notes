class Solution:
    def isPalindrome(self, s):
        """
        https://leetcode.com/problems/valid-palindrome/
        - can the input be empty?
        - convert all uppercase to lowercase
        - remove all non-alphanumeric characters
        """

        sanitized = [ch.lower() for ch in s if ch.isalnum()]

        left, right = 0, len(sanitized) - 1
        while left < right:
            if sanitized[left] != sanitized[right]:
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    solution = Solution()

    s = "A man, a plan, a canal: Panama"
    result = solution.isPalindrome(s)
    assert result == True
    print(result)
    print("Test Case 1 Passed!")
    print()

    s = "race a car"
    result = solution.isPalindrome(s)
    assert result == False
    print(result)
    print("Test Case 2 Passed!")
    print()

    s = " "
    result = solution.isPalindrome(s)
    assert result == True
    print(result)
    print("Test Case 3 Passed!")
    print()
