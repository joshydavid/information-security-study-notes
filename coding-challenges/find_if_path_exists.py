from collections import defaultdict


class Solution:
    def validPath(self, edges, source, destination):
        """
        - https://leetcode.com/problems/find-if-path-exists-in-graph/
        - are the edges bi-directional?
        - is the length of edges always 2
        """

        if source == destination:
            return True

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        visited.add(source)

        def dfs(node):
            if node == destination:
                return True

            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    visited.add(neighbour)

                    if dfs(neighbour):
                        return True

            return False

        return dfs(0)


if __name__ == "__main__":
    solution = Solution()

    edges = [[0, 1], [1, 2], [2, 0]]
    source = 0
    destination = 2
    result = solution.validPath(edges, source, destination)
    assert result == True
    print(result)
    print("Test Case 1 Passed!")
    print()

    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source = 0
    destination = 5
    result = solution.validPath(edges, source, destination)
    assert result == False
    print(result)
    print("Test Case 2 Passed!")
