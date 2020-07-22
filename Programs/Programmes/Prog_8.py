import numpy as np 
from matplotlib import pyplot as plt
import time

# x = np.arange(1,11) 
# y = 2 * x + 5 
# plt.title("Matplotlib demo") 
# plt.xlabel("x axis caption") 
# plt.ylabel("y axis caption") 
# plt.plot(x,y,"r") 
# plt.ion()
x_c=[]
y_c=[]
for a in range(0,100):
	y_c.append(a*0.75)
	if a%2==0:
		x_c.append(0)
	else:
		x_c.append(10)

plt.plot([5,10,0],[10,10,0],  color='lightcoral', linewidth=10, linestyle="-")
plt.plot(x_c,y_c, color="dodgerblue" , linewidth=0.11)
plt.show()


# for num in range(len(x_c)-1):
# 	x,y=list(x_c[num]),list(y_c,[num])
# 	x,y= [x_c[num],x_c[num+1]],[y_c[num],y_c[num+1]]
# 	plt.plot(x,y,"r")
# 	plt.draw()
# 	if num%20==0:
# 		plt.pause(0.000000001)
# 	plt.clf
# plt.plot(x_c,y_c)
# plt.draw()
# plt.pause(1)
# plt.clf()

# plt.ion()
# for i in range(50):
#     y = np.random.random([10,1])
#     plt.plot(y)
#     plt.draw()
#     plt.pause(0.0001)
#     plt.clf()