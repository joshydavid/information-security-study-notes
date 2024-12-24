class Solution:
    def caesarCipherDecrypt(self, cipher, k):
        """
        - can the cipher be empty?
        - can k be 0
        - is the cipher in upper case or lower case?
        """

        if k == 0:
            return cipher

        if not cipher:
            return cipher

        plaintext = []
        k = k % 26

        for ch in cipher:
            if ch.isalpha():
                if ch.isupper():
                    newChar = chr((ord(ch) - ord("A") - k) % 26 + ord("A"))
                else:
                    newChar = chr((ord(ch) - ord("a") - k) % 26 + ord("a"))

                plaintext.append(newChar)
            else:
                plaintext.append(ch)

        return "".join(plaintext)


if __name__ == "__main__":
    solution = Solution()

    cipher = "okffng-Qwvb"
    plaintext = "middle-Outz"
    k = 2
    result = solution.caesarCipherDecrypt(cipher, k)
    assert result == plaintext
    print(result)
    print("Test Case 1 Passed!")
    print()

    cipher = "cdefghijklmnopqrstuvwxyzab"
    plaintext = "abcdefghijklmnopqrstuvwxyz"
    result = solution.caesarCipherDecrypt(cipher, k)
    assert result == plaintext
    print(result)
    print("Test Case 2 Passed!")
    print()

    cipher = "Fubswrjudskb lv dq lqwhuhvwlqj vxemhfw"
    plaintext = "Cryptography is an interesting subject"
    result_v3 = solution.caesarCipherDecrypt(cipher, 3)
    assert result_v3 == plaintext
    print(result_v3)
    print("Test Case 3 Passed!")
    print()

    sentence = ""
    result = solution.caesarCipherDecrypt(sentence, k)
    expected = ""
    assert result == expected
    print("Empty String")
    print("Test Case 4 Passed!")
    print()

    cipher = "Ifmmp"
    sentence = "Hello"
    k = 1
    result = solution.caesarCipherDecrypt(cipher, k)
    expected = sentence
    assert result == expected
    print(result)
    print("Test Case 5 Passed!")
    print()

    cipher = "Hello"
    k = 0
    result = solution.caesarCipherDecrypt(cipher, k)
    expected = "Hello"
    assert result == expected
    print(result)
    print("Test Case 6 Passed!")
    print()
