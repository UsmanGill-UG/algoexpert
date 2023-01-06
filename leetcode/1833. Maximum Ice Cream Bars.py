def maxIceCream(costs, coins):
     costs = sorted(costs)
     i = 0
     while coins >= costs[i]:
         coins -= costs[i]
         i += 1
         if i >= len(costs):
             break
     return i
 
 
costs = [1,6,3,1,2,5]
maxIceCream(costs, 20)