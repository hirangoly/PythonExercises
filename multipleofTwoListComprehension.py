#list comprehension
#List/Dict comprehensions are syntax constructions to ease the creation of a list/dict based on existing iterable. 
#list comprehensions are generally faster than normal loops

#find out multiples of 2 from numbers 1-10 and store in a list
a = []
for x in range(10):
	a.append(x*2)
print a

#using list comprehension
b=[x*2 for x in range(10)]
print b
