class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low_c = 0
        high_c = len(matrix) - 1
        low_r = 0
        high_r = len(matrix[0]) - 1
        while low_c <= high_c:
            mid_c = low_c + (high_c - low_c) // 2
            if matrix[mid_c][0] == target:
                return True
            elif matrix[mid_c][0] < target:
                low_c = mid_c + 1
            else:
                high_c = mid_c - 1
        while low_r <= high_r:
            mid_r = low_r + (high_r - low_r) // 2
            if matrix[high_c][mid_r] == target:
                return True
            elif matrix[high_c][mid_r] < target:
                low_r = mid_r + 1
            else:
                high_r = mid_r - 1
        return False