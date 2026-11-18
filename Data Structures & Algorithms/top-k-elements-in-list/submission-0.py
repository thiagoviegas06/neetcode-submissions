class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        top_k = sorted(num_freq, key=num_freq.get, reverse=True)[:k]
        return top_k