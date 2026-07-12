class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s=sorted(set(arr))
        rank_map = {num: i + 1 for i, num in enumerate(s)}
        return [rank_map[num] for num in arr]
        