
# Iterative Approach
# Average
# Time    O(LogN)
# Space    O(1)
# Worst
# Time    O(N)
# Space    O(1)
def findClosestValueInBst(tree, target):
    closest = float("inf")
    while tree is not None:
        if abs(target - closest) > abs(target - tree.value):
            closest = tree.value
        if target < tree.value:
            tree = tree.left
        elif target > tree.value:
            tree = tree.right
        else:
            break
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
