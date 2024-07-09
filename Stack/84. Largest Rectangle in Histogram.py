# from typing import List

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         sorted_heights = sorted(heights)
#         unique_heights = list(dict.fromkeys(sorted_heights))
#         outer_positions = []
#         inner_positions = []
#         allowed_width = len(heights)
#         out = unique_heights[0] * allowed_width
#         for level_index in range(len(unique_heights)-1):
#             for j in range(len(heights)):
#                 if heights[j] == unique_heights[level_index]:
#                     outer_positions.append(j)
#                 if heights[j] == unique_heights[level_index+1]:
#                     inner_positions.append(j)
#             interval_lengths = self.interval_lengths(outer_lst=outer_positions,inner_lst=inner_positions)
#             for length in interval_lengths:
#                 allowed_width = length + 1
#                 out = max(out, unique_heights[level_index] * allowed_width)
#             positions = []
#         return out
    
    
#     def interval_lengths(self, outer_lst, inner_lst):
#         # Result list to store the lengths of intervals
#         result = []
        
#         # Iterate through each interval in outer_lst
#         for i in range(len(outer_lst) - 1):
#             start = outer_lst[i]
#             end = outer_lst[i + 1]
            
#             # Count the number of elements in inner_lst that fall within the current interval
#             count = 0
#             for num in inner_lst:
#                 if start < num <= end:
#                     count += 1
            
#             # Append the count to the result list
#             result.append(count)
        
#         return result               
        
        
        
# solution = Solution()
# print(solution.largestRectangleArea([2,1,5,6,2,3]))

    
# [1,4,9,12]
# [2,3,6,10]


# def calculate_intervals(arr):
#     # Get unique heights in ascending order
#     unique_heights = sorted(set(arr))
    
#     # Initialize the result dictionary
#     result = {}

#     # Start with the smallest height
#     prev_height = unique_heights[0]
#     prev_indices = [-1] + [i for i, x in enumerate(arr) if x == prev_height] + [len(arr)]

#     # Iterate through each unique height starting from the second smallest
#     for height in unique_heights[1:]:
#         current_indices = [i for i, x in enumerate(arr) if x == height]
#         intervals = []

#         # Calculate intervals between previous and current height indices
#         for i in range(len(prev_indices) - 1):
#             start = prev_indices[i]
#             end = prev_indices[i + 1]

#             # Count occurrences of current height between start and end
#             count = 0
#             for idx in current_indices:
#                 if start < idx < end:
#                     count += 1
#             intervals.append(count)

#         # Store the intervals for the current height
#         result[height] = intervals
        
#         # Update prev_indices for the next iteration
#         prev_indices = current_indices

#     return result

# # Example usage
# array = [3, 4, 1, 2, 1, 5, 6, 2, 3]
# print(calculate_intervals(array))

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         maxArea = 0
#         stack = []  # pair: (index, height)

#         for i, h in enumerate(heights):
#             start = i
#             while stack and stack[-1][1] > h:
#                 index, height = stack.pop()
#                 maxArea = max(maxArea, height * (i - index))
#                 start = index
#             stack.append((start, h))

#         for i, h in stack:
#             maxArea = max(maxArea, h * (len(heights) - i))
#         return maxArea


def merge_sort_to_return_allowed_width(outer_positions, inner_positions):
    allowed_width = []
    counter = 0
    index = 0
    while inner_positions or outer_positions:
        if not outer_positions:
            allowed_width.append(1)
            break
        elif outer_positions[0] > inner_positions[0]:
            inner_positions.pop(0)
            if counter == 0:
                allowed_width.append(1)
            else:
                allowed_width[index] += 1
            counter += 1
        else:
            outer_positions.pop(0)
            counter = 0
            index += 1
        print(outer_positions, inner_positions)
    return allowed_width


print(merge_sort_to_return_allowed_width([0,4],[5]))