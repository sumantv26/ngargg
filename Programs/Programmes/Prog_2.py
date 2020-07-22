#!============================================== Python Program 2 ============================================!#
#============================================== Simple Functions Module ============================================#


def fact(x):
	if x >=1 :
		y=1
		for i in range(1,x+1):
			y*=i
		return y
	
	elif x==0:
		return 1
	else:
		return "Not defined"
def mod(x):
	if x>=0:
		return x
	else:
		return x*-1
def sgn(x):
	if x==0:
		return 0
	else:
		return x//mod(x)
