# map()

myList = [1, 2, 3, 4, 5, 6]
lambdaMap = lambda x : x * 2
myMap = list(map(lambdaMap, myList))
print(myMap) # -> [2, 4, 6, 8, 10, 12]

# filter()

lambdaFilter = lambda x : x % 2 == 0
myFilter = list(filter(lambdaFilter, myList))
print(myFilter) # -> [2, 4, 6]


# reduce()

from functools import reduce

lambdaReduce = lambda x, y : x + y
myReduce = reduce(lambdaReduce, myList)
print(myReduce) # -> 21


