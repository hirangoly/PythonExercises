from sys import argv 

def lcm(x,y):
		tmp=x
		while (tmp%y)!=0:
			tmp+=x
		return tmp

def lcmm(*args):
    return reduce(lcm,args)

args=map(int,argv[1:])
print lcmm(*args)
