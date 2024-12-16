class Solution:
    def getEncryptedString(self, s, k):
        """
        - can the input be null?
        - is the input a valid string?
        - can k be 0?
        - are the characters in lower or uppercase?
        """

        if k == 0:
            return s

        if not s:
            return s

        cipher = []
        n = len(s)

        for i in range(n):
            newIndex = (
                i + k
            ) % n  # wraps around the string, prevents array out of bound
            newValue = s[newIndex]
            cipher.append(newValue)

        return "".join(cipher)


if __name__ == "__main__":
    solution = Solution()

    s = "dart"
    k = 3
    result = solution.getEncryptedString(s, k)
    assert result == "tdar"
    print(result)
    print("Test Case Passed!")
    print()
