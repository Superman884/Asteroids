import pygame
from random import randrange
run=True
win=pygame.display.set_mode((500,500))
xchange=1
ychange=1
stuff=[1,-89]
angle=1
c=0
d=10
delay=0
spawnx=0
class car:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.xmom=0
		self.ymom=0
class bullet:
	def __init__(self,x,y,vel,mom):
		self.x=x
		self.y=y
		self.vel=vel
		self.mom=mom
bullets=[]
car1=car(250,100)
img2=pygame.image.load("MAN2.png")
img1=[pygame.image.load("MAN1.png"),pygame.image.load("MAN1_0.png"),pygame.image.load("MAN1_1.png")]
bullet_img=pygame.image.load('bullet.png')
img=img2
while run:
	if c%100==0:
		d+=1
	img_show=pygame.transform.rotate(img,-angle)
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False
	win.blit(img_show,(car1.x,car1.y))
	img=img2
	keys=pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		car1.xmom+=stuff[0]/33000
		car1.ymom+=stuff[1]/33000
		img=img1[d%3]
	if c%1==0:
		for i in bullets:
			i.x+=i.mom/130
			if i.x>=500:
				i.x=-20
			elif i.x<=-20:
				i.x=500
			i.y+=i.vel/130
			if i.y>=500:
				i.y=-20
			elif i.y<=-20:
				i.y=500
			win.blit(bullet_img,(i.x,i.y))
	if c%7==0:
		if keys[pygame.K_RIGHT]:
			angle+=1
			if angle>=360:
				angle-=360
			stuff[0]+=xchange
			stuff[1]+=ychange
			if angle==90 or angle==270:
				xchange*=-1
			if angle==0 or angle==180:
				ychange*=-1
		if keys[pygame.K_LEFT]:
			angle-=1
			if angle<0:
				angle=360+angle
			stuff[0]-=xchange
			stuff[1]-=ychange
			if angle==90 or angle==270:
				xchange*=-1
			if angle==0 or angle==180:
				ychange*=-1
	if delay==0:
		if len(bullets)<300 and keys[pygame.K_SPACE]:
			bullets.append(bullet(car1.x+20+stuff[0]/3,car1.y+20+stuff[1]/3,stuff[1],stuff[0]))
			delay=300
	else:
		delay-=1
	c+=1
	car1.x+=car1.xmom/2
	car1.y+=car1.ymom/2
	car1.xmom/=1.005
	car1.ymom/=1.005
	if car1.x<-30:
		car1.x=520
	if car1.x>520:
		car1.x=-30
	if car1.y<-30:
		car1.y=530
	if car1.y>530:
		car1.y=-30
	pygame.display.update()
	win.fill((0,0,0))