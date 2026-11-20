class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastidx = defaultdict(int)

        for i, c in enumerate(s):
            lastidx[c] = i
        
        size, end = 0, 0
        res = []

        for i, c in enumerate(s):
            end = max(end, lastidx[c])
            size += 1

            if i == end:
                res.append(size)
                size = 0
        
        return res