#!============================================== Python Program 16 ======================================================!#
#=============================================== GCD And LCM Module ======================================================#

def gcd(x,y):
	hcf=1
	for num in range(1,min(x,y)+1):
		if (x%num==0) and (y%num==0):
			hcf=num
	return hcf

def lcm(x,y):
	number=1
	for num in range(int(x),int(x*y)+1):
		if (num%x==0) and (num%y==0):
			number=num
			break
		else:
			pass
	return number
