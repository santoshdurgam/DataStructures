klist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lambda basic
a=5
f = lambda x: x+1

print(f(a))

# lambda on a list + filter
evenlist = filter(lambda x: (x%2==0), klist)
print(evenlist)

oddlist = filter(lambda x: (x%2!=0), klist)
print oddlist

# lambda on a list + map
doublelist = map(lambda x: x*2, klist)
print doublelist