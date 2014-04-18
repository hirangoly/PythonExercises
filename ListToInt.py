#convert list to string -> then string to int
#Step1: turn [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8]
#Step2: turn [1,2,3,4,5,6,7,8] into 12345678

#Step1: turn [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8]
items = [[1,2,3],[4,5],[6,7,8]] 
list = []
for x in items:
	for c in x:
		list.append(c)
print list
#print reduce(list.__add__, [[1, 2, 3], [4, 5], [6, 7, 8]], [])

#Step2: turn [1,2,3,4,5,6,7,8] into 12345678
items1 = [1,2,3,4,5,6,7,8]
items = [2,5,4,7,3,8,9]
print ''.join(map(str,items))
#or
print reduce((lambda x,y: 10*x+y),items)
