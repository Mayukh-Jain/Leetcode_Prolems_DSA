class Solution:

    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        # last[j] stores the maximum index in word1 to start an exact match for word2[j..m-1]
        last = [-1] * (m + 1)
        last[m] = n

        # Precompute last array from right to left
        curr = n - 1
        for j in range(m - 1, -1, -1):
            while curr >= 0 and word1[curr] != word2[j]:
                curr -= 1
            last[j] = curr
            if curr >= 0:
                curr -= 1

        ans = []
        i = 0
        changed = False

        # Construct the lexicographically smallest sequence greedily
        for j in range(m):
            found = False
            while i < n:
                if word1[i] == word2[j]:
                    if changed:
                        if i < last[j + 1]:
                            ans.append(i)
                            i += 1
                            found = True
                            break
                    else:
                        # Character matches; no mismatch used yet
                        ans.append(i)
                        i += 1
                        found = True
                        break
                else:
                    if not changed and i < last[j + 1]:
                        # Use the 1 allowed mismatch at index i
                        ans.append(i)
                        changed = True
                        i += 1
                        found = True
                        break

                i += 1

            if not found:
                return []

        return ans