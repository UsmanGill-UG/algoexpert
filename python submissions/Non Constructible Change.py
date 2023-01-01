def nonConstructibleChange(coins):
    change = 0
    coins.sort()
    for curr_coin in coins:
        if change + 1 < curr_coin:
            return change+1
        change += curr_coin
    return change + 1


'''

Complexity :  nlogn + n =  O(nlogn)

Explanation:
     e.g  [1,1,2]
     change + 1 must be smaller than the next coin in the array 
     if it is not then obviously we can not make change + 1
     
'''