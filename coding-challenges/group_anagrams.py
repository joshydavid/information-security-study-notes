class Solution:
    def groupAnagrams(self, results):
        """
        - https://leetcode.com/problems/group-anagrams/
        - can the input be empty?
        - does the input only contain lowercase characters?
        """

        if not results:
            return results

        anagrams_mapping = {}

        for result in results:
            key = [0] * 26

            for ch in result:
                # a -> 0
                # b -> 1
                # c -> 2
                key[ord(ch) - ord("a")] += 1

            tupleKey = tuple(key)

            if tupleKey not in anagrams_mapping:
                anagrams_mapping[tupleKey] = [result]
            else:
                anagrams_mapping[tupleKey].append(result)

        return list(anagrams_mapping.values())


if __name__ == "__main__":
    solution = Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    result = solution.groupAnagrams(strs)
    assert result == output
    print(output)
    print("Test Case 1 Passed!")
    print()

    strs = [""]
    output = [[""]]
    result = solution.groupAnagrams(strs)
    assert result == output
    print(output)
    print("Test Case 2 Passed!")
    print()

    strs = ["a"]
    output = [["a"]]
    result = solution.groupAnagrams(strs)
    assert result == output
    print(output)
    print("Test Case 3 Passed!")
    print()
