#https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        stack = []
        target = image[sr][sc]
        image[sr][sc] = color
        stack.append((sr,sc))
        while len(stack) > 0:
            sr, sc = stack[-1]
            if (sr + 1 < len(image)) and image[sr+1][sc] == target: #RIGHT
                image[sr+1][sc] = color
                stack.append((sr+1, sc))
            elif (sr - 1 >= 0) and image[sr-1][sc] == target: #LEFT
                image[sr-1][sc] = color
                stack.append((sr-1, sc))
            elif (sc + 1 < len(image[0])) and image[sr][sc+1] == target: #UP
                image[sr][sc+1] = color
                stack.append((sr, sc+1))
            elif (sc - 1 >= 0) and image[sr][sc-1] == target: #DOWN
                image[sr][sc-1] = color
                stack.append((sr, sc-1))
            else:
                stack.pop()
        return image

"""
Notes/Realizations

 - Iterative approach where I start at the base cell, scan it's color, and then move Right, Left, Up, and Down in that order upon each iteration.
	- I save a tuple of the sr/sc to a stack and continue until all cells are popped off, this way ensures color change upon each branch and a runtime of O(n) or O(m*n) in our scenario
"""
