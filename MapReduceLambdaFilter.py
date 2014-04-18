#Map, Lambda, Filter, Reduce

#normal method
items = [1, 2, 3, 4, 5]
squared = []
for x in items:
	squared.append(x**2)
print squared

# Map example map(aFunction, aSequence) - equivalent to for loop
# faster than normal loop
items = [1, 2, 3, 4, 5]
def sqr(x):
	return x ** 2
#range(1,5) means 1-4
print list(map(sqr, range(1,6))) 	

#Map lambda
items = [1, 2, 3, 4, 5]
print list(map((lambda x: x **2), items))
#or
print map((lambda x: x **2), items)

#If function is None, the identity function is assumed; if there are multiple arguments, map() returns a list consisting of tuples 
m=[1,2,3]
n=[2,5,6]
new_tuple = map(None, m , n)
print new_tuple

#filter(aFunction, aSequence) - extracts each element in the sequence for which the function returns true
# return all -negative elements from -5 to 5 
#range(-5,5)
#x<0
print filter((lambda x: x<0),range(-5,5))
#or
print list(filter((lambda x: x<0),range(-5,5)))

#reduce(aFunction, aSequence) - This function reduces a list to a single value by combining elements via a supplied function.
#multiply of all the elements
import operator
items = [1,2,3]
print reduce(operator.mul,items)
#or
print reduce((lambda x,y:x*y),items)

import operator
import functools
items = ['hello','how','are','you']
print ' '.join(items)
#or
print reduce((lambda x,y:x + ' ' +y),items)
#or
print functools.reduce( (lambda x,y:x+y), items)





