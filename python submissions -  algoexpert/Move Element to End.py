def moveElementToEnd(array, toMove):
    lp = 0
    rp = len(array)-1
    while lp < rp:
        while array[rp] == toMove and lp < rp:
            rp -= 1
        if array[lp] == toMove:
            array[lp], array[rp] = array[rp], array[lp]
        lp += 1
    return array
            

array = [1, 2, 4, 5, 6]
toMove=3
print(moveElementToEnd(array, toMove))