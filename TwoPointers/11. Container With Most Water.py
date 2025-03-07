class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Two pointers
        left, right = 0, len(height)-1

        # Max width between leftmost stick and rightmost stick
        max_width = len(height) - 1

        # area
        area = 0

       # Scan each possible width and compute maximal area
        for width in range(max_width, 0, -1):

            if height[left] < height[right]:
                # If the height of lefthand side is shorter
                area = max(area, width * height[left])

                # Update left index to righthand side
                left += 1

            else:
                # If the height of righthand side is shorter
                area = max(area, width * height[right])

                # Update right index to lefthand side
                right -= 1

        return area


""" 
Time Complexity : O(n)
For Example: list = [1,8,6,2,5,4,8,3,7]
Pass 1 : left = 0, right = 8, width = 8, height[left] = 1, area = 8
Pass 2 : left = 1, right = 8, width = 7, height[right] = 7, update area = 7*7=49
Pass 3 : left = 1, right = 7, width = 6, height[right] = 3, 6*3 < 49, area remain = 49
Pass 4 : left = 1, right = 6, width = 5, height[right] = 8, 5*8 < 49, area remain = 49 
Pass 5 : left = 1, right = 5, width = 4, height[right] = 4, 4*4 < 49, area remain = 49 
Pass 6 : left = 1, right = 4, width = 3, height[right] = 5, 3*5 < 49, area remain = 49 
Pass 7 : left = 1, right = 3, width = 2, height[right] = 2, 2*2 < 49, area remain = 49 
Pass 8 : left = 1, right = 2, width = 1, height[right] = 6, 1*6 < 49, area remain = 49
"""
