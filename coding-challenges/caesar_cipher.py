class Solution:
    def caesarCipher(self, sentence, k):
        """
        - can the sentence be empty?
        - does the sentence only contain valid characters?
        - can k be 0?
        - is the sentence in upper case or lower case?
        """

        if k == 0:
            return sentence

        if not sentence:
            return sentence

        cipher = []
        k = k % 26

        for ch in sentence:
            if ch.isalpha():
                if ch.isupper():
                    newChar = chr((ord(ch) - ord("A") + k) % 26 + ord("A"))
                else:
                    newChar = chr((ord(ch) - ord("a") + k) % 26 + ord("a"))

                cipher.append(newChar)
            else:
                cipher.append(ch)

        return "".join(cipher)


if __name__ == "__main__":
    solution = Solution()

    text = "middle-Outz"
    k = 2
    result = solution.caesarCipher(text, k)
    assert result == "okffng-Qwvb"
    print(result)
    print("Test Case 1 Passed!")
    print()

    text = "abcdefghijklmnopqrstuvwxyz"
    result = solution.caesarCipher(text, k)
    assert result == "cdefghijklmnopqrstuvwxyzab"
    print(result)
    print("Test Case 2 Passed!")
    print()

    text = "Cryptography is an interesting subject"
    k = 3
    result = solution.caesarCipher(text, k)
    assert result == "Fubswrjudskb lv dq lqwhuhvwlqj vxemhfw"
    print(result)
    print("Test Case 3 Passed!")
    print()

    text = ""
    result = solution.caesarCipher(text, k)
    expected = ""
    assert result == expected
    print("Empty String")
    print("Test Case 4 Passed!")
    print()

    text = "Hello"
    k = 1
    result = solution.caesarCipher(text, k)
    expected = "Ifmmp"
    assert result == expected
    print(result)
    print("Test Case 5 Passed!")
    print()

    text = "Hello"
    k = 0
    result = solution.caesarCipher(text, k)
    expected = "Hello"
    assert result == expected
    print(result)
    print("Test Case 6 Passed!")
    print()
