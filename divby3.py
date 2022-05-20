numList = [3,10,33,12,5,8,50,100]
print("Given this list of integers: ", numList)
result = list(filter(lambda x: (x % 3 ==0), numList))
print("These numbers are divisible by 3: ", result)
