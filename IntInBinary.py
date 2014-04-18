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
	IntInBinaryUsingList(12,-1)
	print binary(12)
	print binaryTest(12)
	
if __name__ == '__main__':
	main()
