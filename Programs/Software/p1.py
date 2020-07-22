import time
import pygame as p
from pygame import mixer
p.init()



ss=[1200,800]
x=ss[0]//2
y=3*ss[1]//4
screen=p.display.set_mode(ss)
background=p.transform.scale(p.image.load("back.jpg"),ss)



space=p.transform.scale(p.image.load("spacecraft/s1.png"),[100,120])
pmove='right'
p1=p.image.load("planet/p1.png")
p2=p.image.load("planet/p2.png")
planet=p1
px=600
pspeed=5
collision=False

b_launch={}
b_x={}
b_y={}
b_index=['b1','b2','b3','b4','b5']
bullet=p.transform.scale(p.image.load("bullet.png"),[15,45])
for i in b_index:
	b_launch[i]=False
	b_x[i]=x+40
	b_y[i]=40
b_selected=0
index=1
print(b_x)


exp_dict={}
for i in range(1,40):
	exp="explosion/exp"+str(i)+".png"
	exp_dict[str(i)]=p.transform.scale(p.image.load(exp),[140,140])


mixer.music.load("background.wav")
mixer.music.play(-1)



while True:
	# if not b_launch[b_index[b_selected]] and not collision:
	# 	b_x[b_index[b_selected]]=x+40
	for i in b_index:
		if not b_launch[i] and not collision:
			b_x[i]=x+40
	screen.blit(background,[0,0])
	for bullets in b_index:
		screen.blit(bullet,[b_x[bullets],y+b_y[bullets]])

	screen.blit(space,[x,y])
	screen.blit(planet,[int(px),10])
	screen.blit(exp_dict[str(index)],[int(px),10])

	
	keys=p.key.get_pressed()
	events = p.event.get()
	for event in events:
		if event.type == p.KEYDOWN:
			if event.key == p.K_LEFT :
				x -= 10
			if event.key == p.K_RIGHT :
				x += 10
			if event.key == p.K_SPACE :
				exit()
			if event.key == p.K_UP :
				b_launch[b_index[b_selected]]=True
				b_selected+=1
				if b_selected==5:
					b_selected=4
	for b in b_index:
		if b_launch[b]:
			b_y[b]-=4
	if not collision:
		if pmove=="right":
			px+=pspeed
			if px >= 970:
				pmove="left"
		elif pmove=="left":
			px-=pspeed
			if px <=85:
				pmove="right"

	for b in b_index:
		if ((b_x[b] >= int(px)) and (b_x[b]<= int(px)+120)) and ((y+b_y[b]>=10) and (y+b_y[b] <=140)):
			collision=True

	if collision:
		time.sleep(0.02)
		index+=1
		if index==40:
			index=1
			planet=p2
			collision=False
	
	if planet==p2:
		pspeed+=1
		if pspeed >= 30:
			pspeed=2
			p.transform.rotate(p2,10)

	time.sleep(0.0001)
	p.display.update()