class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [0] * (amount + 1)

        for i in range(1, len(mem)):
            min_coins = float("inf")
            for coin in coins:
                diff = i - coin
                if diff >= 0 and mem[diff] != -1:
                    min_coins = min(mem[diff], min_coins)
            
            mem[i] = min_coins + 1 if min_coins != float("inf") else -1
        
        return mem[-1]
            
            



