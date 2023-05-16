# First Solution:
# O(n) time | O(1) space
def isMonotonic(array):
    prev = None
    increasing = False
    decreasing = False
    for num in array:
        if prev is not None:
            if num < prev:
                if increasing:
                    return False
                decreasing = True
            elif num > prev:
                if decreasing:
                    return False
                increasing = True
        prev = num
    return True

# Cleaner Solution:
# O(n) time | O(1) space
def isMonotonic(array):
    prev = None
    increasing = True
    decreasing = True
    for num in array:
        if prev is not None:
            if num < prev:
                increasing = False
            elif num > prev:
                decreasing = False
        prev = num
    return increasing or decreasing


array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(isMonotonic(array))
