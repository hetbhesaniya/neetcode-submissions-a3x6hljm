class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        arr = list(count.items())
        arr.sort(key=lambda x: x[1], reverse=True)

        res = []
        for num, freq in arr[:k]:
            res.append(num)

        return res