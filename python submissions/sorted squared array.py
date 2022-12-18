# def sortedSquaredArray1(array): #nlogn
#     # Write your code here.
#     res = []
#     for i in array:
#         res.append(i**2)  # will not work for minus numbers
#     res = sorted(res)
#     return res

# Optimal Solution by 2 Pointers # O(n)

def sortedSquaredArray(array):
    # Write your code here.
    res = [0 for i in array]
    l_ptr = 0
    r_ptr = len(array)-1
    i = len(array)-1
    while l_ptr <= r_ptr:
        l_sqr = array[l_ptr]**2
        r_sqr = array[r_ptr]**2
        if r_sqr > l_sqr:
            res[i] = r_sqr
            r_ptr -= 1
        else:
            res[i] = l_sqr
            l_ptr += 1
        i -= 1
    return res


array = [1, 2, 3, 5, 6, 8, 9]
res = sortedSquaredArray(array)
print(res)
