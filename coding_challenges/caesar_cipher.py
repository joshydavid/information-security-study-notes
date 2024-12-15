class Solution:
    def caesarCipher(self, sentence, k):
        """
        - can the sentence be empty?
        - does the sentence only contain valid characters?
        - can k be more than 0?
        - is the sentence in upper case or lower case?
        """

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
    result = solution.caesarCipherEncrypt(text, k)
    assert result == "okffng-Qwvb"
    print(result)
    print("Test Case Passed!")
    print()

    text_v2 = "abcdefghijklmnopqrstuvwxyz"
    result_v2 = solution.caesarCipherEncrypt(text_v2, k)
    assert result_v2 == "cdefghijklmnopqrstuvwxyzab"
    print(result_v2)
    print("Test Case Passed!")
    print()

    k_v3 = 3
    text_v3 = "Cryptography is an interesting subject"
    result_v3 = solution.caesarCipherEncrypt(text_v3, k_v3)
    assert result_v3 == "Fubswrjudskb lv dq lqwhuhvwlqj vxemhfw"
    print(result_v3)
    print("Test Case Passed!")
    print()

    sentence = ""
    result = solution.caesarCipherEncrypt(sentence, k)
    expected = ""
    assert result == expected
    print("Empty String")
    print("Test Case Passed!")
    print()

    sentence = "Hello"
    k = 1
    result = solution.caesarCipher(sentence, k)
    expected = "Ifmmp"
    assert result == expected
    print(result)
    print("Test Case Passed!")
    print()
