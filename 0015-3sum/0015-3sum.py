class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        pos, neg, zero = [], [], []

        for n in nums:
            if n > 0:
                pos.append(n)
            elif n < 0:
                neg.append(n)
            else:
                zero.append(n)

        pos_set = set(pos)
        neg_set = set(neg)
        
        if zero:
            for p in pos_set:
                if -p in neg_set:
                    res.add((0, p, -p))

        if len(zero) > 2:
            res.add((0, 0, 0))

        
        for i, p1 in enumerate(pos):
            for j in range(i + 1, len(pos)):
                complement = -(p1 + pos[j])
                if complement in neg_set:
                    res.add(tuple(sorted([p1, pos[j], complement])))
        
        for i, n1 in enumerate(neg):
            for j in range(i + 1, len(neg)):
                complement = -(n1 + neg[j])
                if complement in pos_set:
                    res.add(tuple(sorted([n1, neg[j], complement])))


        return res


        

