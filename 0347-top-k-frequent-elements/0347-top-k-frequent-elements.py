class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1]))

        keys = list(sorted_freq.keys())

        return keys[-k:]