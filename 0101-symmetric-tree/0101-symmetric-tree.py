class Solution:
    def isSymmetric(self, root):
        
        def mirror(left, right):
            # Both nodes are empty
            if left is None and right is None:
                return True

            # One node is empty
            if left is None or right is None:
                return False

            # Values must be same
            if left.val != right.val:
                return False

            # Check opposite sides
            return mirror(left.left, right.right) and \
                   mirror(left.right, right.left)

        return mirror(root.left, root.right)