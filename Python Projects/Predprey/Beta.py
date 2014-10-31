#Author=AcisAce

import pygame
import math
import random

## Welcome to the predprey simulation program


(width,height)=(800,400)  #Window properties
screen=pygame.display.set_mode((width,height)) #Display Settings
screen.fill((255,255,255))

sizePred=20  #Sizes in pixels
sizePrey=15
velPred=0.01
velPrey=0.01



colorRand=[(255,0,128),(0,255,200),(0,128,255)] #Three random colors
#------------------------------------------------------------------------------------Predator Initialization
class Predator(object):
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
    def drawPred(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),sizePred,4)
    def move(self):
        angle=random.uniform(0,2*math.pi)
        self.x=int(self.x+velPred*math.cos(angle))
        self.y=int(self.y+velPred*math.sin(angle))
        
        

predatorCount=1 #Set Number of predators

listPredators=[]

for i in range(predatorCount):
    xRand=random.randint(sizePred,width-sizePred)
    yRand=random.randint(sizePred,height-sizePred)
    colRand=random.choice(colorRand)
    listPredators.append(Predator(xRand,yRand,colRand))


#-------------------------------------------------------------------------------------Prey Initialization
class Prey(object):
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
    def drawPrey(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),sizePrey,2)

preyCount=30 #Set number of prey organisms

listPrey=[]

for i in range(preyCount):
    xRand=random.randint(sizePrey,width-sizePrey)
    yRand=random.randint(sizePrey,height-sizePrey)
    colP=(0,0,0)
    listPrey.append(Prey(xRand,yRand,colP))
    

for predator in listPredators:
        predator.drawPred()

for prey in listPrey:
        prey.drawPrey()




running=True
while running: #Main Game Loop
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
    screen.fill((255,255,255))
    for predator in listPredators:
        predator.move()
        predator.drawPred()
    for prey in listPrey:
        prey.drawPrey()
    
    pygame.display.flip()
        
       
    
    


    
    
