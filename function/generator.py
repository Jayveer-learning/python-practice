def generator(data) -> int:
    for i in data: 
        yield i

dataList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
generatorData = generator(dataList)
print(next(generatorData))

# accessing generator value using for loop
print("accessing data using for loop instace of next()")

for data in generatorData:
    print(data)

print(next(generatorData))


