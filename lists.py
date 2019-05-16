# original list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))

print "remove duplicates"
from collections import OrderedDict
res = list(OrderedDict.fromkeys(test_list))
print ("The new list is : " + str(res))


print "Number of values greater than k in list"
k=4
res = filter(lambda x:x>k, test_list)
print ("the Number of items greater than K in the list :" + str(len(res)))

print "find substr in string"
test_str ="GeeksforGeeks"

res = test_str.find("eek")
res2 = test_str.index("eek")
import operator
res3 = operator.contains(test_str, "eek")
print res
print res2
print res3


print "intresection of 2 lists"
# initializing lists
test_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]
# printing both lists
print ("The original list 1 : " + str(test_list1))
print ("The original list 2 : " + str(test_list2))

