class Solution:
    def trap(self, height: List[int]) -> int:

        left_max = [0] * len(height)
        right_max = [0] * len(height)
        
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i - 1])
            
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i + 1])

        volume = 0
        for i, (lm, rm) in enumerate(zip(left_max, right_max)):
            level = min(lm, rm) - height[i]
            if level > 0:
                volume += level
        
        return volume

        




                
            


