list = []
def IntInBinaryUsingList(num,i):
	if num < 2:
		num1 = num%2
		list.insert(i,num1)
		print list		
		i = i +1
	if num  >= 2:
		num1 = num%2
		list.insert(i,num1)
		i = i -1
		return IntInBinaryUsingList(num/2,i)
		
def binary(n):
   if n < 2:
     return [n]
   else:
     return binary(n / 2) + [n % 2]
	 
def binaryTest(n):
   if n < 2:
     return [n]
   else:
     return binary(n)
		
def main():	
	#method1 - using list
	IntInBinaryUsingList(12,-1)
	#method2 - using binary function
	print binary(12)
	#method2.1 - binary function
	print binaryTest(12)
	
if __name__ == '__main__':
	main()
