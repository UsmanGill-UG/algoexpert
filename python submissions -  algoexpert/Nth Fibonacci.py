# O(2^n) and space : O(n)
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return getNthFib(n-1) + getNthFib(n-2)


# Memoization
# O(n) time, no duplicate calculations
# O(n) space
def getNthFib(n, memoize={1:0,2:1}):
    if n in memoize:
        return memoize[n]
    memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2,memoize)
    return memoize[n]

# Iterative solution