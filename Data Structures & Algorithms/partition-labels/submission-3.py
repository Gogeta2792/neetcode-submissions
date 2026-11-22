class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = defaultdict(int)
        for i, c in enumerate(s):
            lastIdx[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, lastIdx[c])
            size += 1

            if i == end:
                res.append(size)
                size = 0
        
        return res