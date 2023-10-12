from collections import Counter
from heapq import heappop, heappush, heapreplace

class Pair:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __gt__(self, pair):
        return self.count > pair.count or (self.count == pair.count and self.word < pair.word)


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = list(Counter(words).items())
        heap = [Pair(count, s) for s, count in word_count[:k]]
        heapify(heap)
        
        for i in range(k, len(word_count)):
            if heap[0] < Pair(word_count[i][1], word_count[i][0]):
                heapreplace(heap, Pair(word_count[i][1], word_count[i][0]))
        

        return reversed([heappop(heap).word for _ in range(k)])


            
        
