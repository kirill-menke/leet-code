from collections import Counter
from heapq import heappush, heappop

class Pair:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, pair):
        return self.count < pair.count or (self.count == pair.count and self.word > pair.word)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = Counter(words)
        heap = []

        for word, count in word_count.items():
            heappush(heap, Pair(count, word))
            if len(heap) > k:
                heappop(heap)
        
        return reversed([heappop(heap).word for _ in range(k)])
