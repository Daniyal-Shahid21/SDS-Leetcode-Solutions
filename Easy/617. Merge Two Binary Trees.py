#https://leetcode.com/problems/merge-two-binary-trees/description/

class Solution:
    def traverse(self, curr1: Optional[TreeNode], curr2: Optional[TreeNode]) -> Optional[TreeNode]:
        if curr1 is None:
            return curr2
        if curr2 is None:
            return curr1

        curr1.val += curr2.val

        if curr1.left is None and curr2.left is not None:
            curr1.left = curr2.left
        else:
            curr1.left = self.traverse(curr1.left, curr2.left)

        if curr1.right is None and curr2.right is not None:
            curr1.right = curr2.right
        else:
            curr1.right = self.traverse(curr1.right, curr2.right)

        return curr1

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            self.traverse(root1, root2)
            return root1
        return root1 or root2
    
"""
Notes/Realizations
 - If left bin tree doesn't exist, return right, vice versa applicable
 - This means current node exists for both, add values:
    If left side of Tree1 is none, and left side of Tree2 is not None,
        Add the rest of the left side of Tree2 to Tree1
            Do the same for right sides
    
    If a left side exists for both, repeat the program for left for both trees, restarting the loop at the next node, and assigning subsequent value to that level of the tree
"""