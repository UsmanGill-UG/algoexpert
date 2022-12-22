def nonConstructibleChange(coins):
    change = 0
    coins.sort()
    for curr_coin in coins:
        if change + 1 < curr_coin:
            return change+1
        change += curr_coin
    return change + 1



