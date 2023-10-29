
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k

        while left != right:
            mid = (left + right) // 2

            if abs(arr[mid] - x) > abs(arr[mid + k] - x):
                left = mid + 1
            elif arr[mid] == arr[mid + k] and x > arr[mid]:
                left = mid + 1
            else:
                right = mid
            
        return arr[left: left + k]

        
