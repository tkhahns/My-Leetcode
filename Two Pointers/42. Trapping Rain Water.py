class Solution:
    def trap(self, height: List[int]) -> int:
        out = 0
        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                out += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                out += maxRight - height[right]
            
        return out