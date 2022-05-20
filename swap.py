list1 = [1,2,3,4,5]        #should print [5,2,3,4,1]
list2 = [5,2,3,4,1]        #should print [1,2,3,4,5]
list3 = [7,4,7,2,3,6,3]    #should print [3,4,7,2,3,6,7]
list1[0] = 5
list1[4] = 1
print(list1)
list2[0] = 1
list2[4] = 5
print(list2)
list3[0] = 3
list3[6] = 7
print(list3)
