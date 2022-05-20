def duplicateSums(a, b, c):
    if a != b and a != c and b != c:
        return a + b + c
    elif a == b == c:
        return 0
    else:
        return b

print(duplicateSums(1,2,3))     #should return 6
print(duplicateSums(2,3,2))     #should return 3
print(duplicateSums(1,1,1))     #should return 0
