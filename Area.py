class Area:
    
    def bruteForceMaxArea(self, height: List[int]) -> int:
        length_of_height = len(height)
        for i in range(0, length_of_height):
            for j in range(i+1, length_of_height):
                area = min(height[i], height[j]) * (j-i)
                if area > max_area:
                    max_area = area
        return max_area
    
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        return max_area
    
