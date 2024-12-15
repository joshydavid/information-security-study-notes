class TextToEmoji:
    """
    - Can the input be null?
    - Are the input in lowercase or uppercase?
    - Are there special characters in the inputs?
    """

    def swapTextToEmoji(self, sentence):
        # can the sentence be empty?
        # is input in lowercase or uppercase?

        if not sentence:
            EMPTY_MESSAGE = "Sorry, no inputs found."
            return EMPTY_MESSAGE

        emojiMapping = {
            "a": "😊",
            "b": "😂",
            "c": "😍",
            "d": "🤣",
            "e": "😊",
            "f": "🙌",
            "g": "😎",
            "h": "🤩",
            "i": "😄",
            "j": "🥰",
            "k": "🤗",
            "l": "🤪",
            "m": "😜",
            "n": "🥳",
            "o": "🥺",
            "p": "😝",
            "q": "🤠",
            "r": "😌",
            "s": "😅",
            "t": "😆",
            "u": "😇",
            "v": "🤩",
            "w": "😺",
            "x": "😈",
            "y": "🤪",
            "z": "😃",
        }

        result = [emojiMapping.get(ch.lower(), "") for ch in sentence]

        return "".join(result)


if __name__ == "__main__":
    textToEmoji = TextToEmoji()

    # Test Case 1
    print("Test Case 1")
    empty_text = ""
    cipher = textToEmoji.swapTextToEmoji(empty_text)
    print(f"Original -", empty_text)
    print(f"Cipher -", cipher)
    assert cipher == "Sorry, no inputs found."
    print("Test Case 1 Passed!")
    print()

    # Test Case 2
    print("Test Case 2")
    valid_text = "Apple"
    cipher = textToEmoji.swapTextToEmoji(valid_text)
    print(f"Original -", valid_text)
    print(f"Cipher -", cipher)
    assert cipher == "😊😝😝🤪😊"
    print("Test Case 2 Passed!")
    print()
