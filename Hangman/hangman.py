import pygame
from pygame.locals import *
import random
import time
import sys

beige=(245,245,220)
black=(0,0,0)
white=(255,255,255)
maroon=(128,0,0)
gap=20
letters=[]
startx=round((800-(3*gap)*13)/2)
starty=400
A=65
for i in range(26):
    x=startx+gap*2+((gap*3)*(i%13))
    y=starty+((i//13)*(3*gap))
    letters.append([x,y,chr(A+i),True])

clock=pygame.time.Clock()

with open("easy.txt","r") as file:
    etext=file.read().upper()
    easy=list(map(str, etext.split()))
with open("medium.txt","r") as file:
    mtext=file.read().upper()
    med=list(map(str, mtext.split()))
with open("hard.txt","r") as file:
    htext=file.read().upper()
    hard=list(map(str, htext.split()))

pygame.init()
pygame.font.init()

font=pygame.font.SysFont("comicsans",25)
title=pygame.font.SysFont("comicsans",60)
head=pygame.font.SysFont("comicsans",40)
message=pygame.font.SysFont("comicsans",80)
images=[pygame.image.load("hangman0.png"),pygame.image.load("hangman1.png"),pygame.image.load("hangman2.png"),pygame.image.load("hangman3.png"),pygame.image.load("hangman4.png"),pygame.image.load("hangman5.png"),pygame.image.load("hangman6.png")]

screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("Hangman")
icon=pygame.image.load("hangman.png")
pygame.display.set_icon(icon)
screen.fill(beige)

def draw():
    clock.tick(60)
    screen.fill(beige)
    screen.blit(images[status],(50,50))
    display_word=""
    for j in word:
        if j in guessed:
            display_word+=j+" "
        else:
            display_word+="_ "
    text1=title.render(display_word,1,black)
    screen.blit(text1,(350,200))
    for j in letters:
        x,y,l,b=j
        text=font.render(l,1,black)
        if b:
            pygame.draw.circle(screen,black,(x,y),gap,3)
            screen.blit(text,(x-text.get_width()/2,y-text.get_height()/2))

    pygame.display.update()

def start():
    screen.fill(beige)
    text=title.render("HANGMAN",1,black)
    screen.blit(text,(400-text.get_width()/2,20))
    text2=font.render("EASY(Press 1)",1,black)
    screen.blit(text2,(400-text2.get_width()/2,150))
    text2=font.render("MEDIUM(Press 2)",1,black)
    screen.blit(text2,(400-text2.get_width()/2,250))
    text2=font.render("HARD(Press 3)",1,black)
    screen.blit(text2,(400-text2.get_width()/2,350))
    pygame.display.update()

run=True
status=0
c=0
if c==0:
    word="DEFAULT"
guessed=[]
first=True
while first:
    start()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.QUIT()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_1]:
        c=1
        first=False
    if keys[pygame.K_2]:
        c=2
        first=False
    if keys[pygame.K_3]:
        c=3
        first=False
if c==1:
    word=random.choice(easy)
if c==2:
    word=random.choice(med)
if c==3:
    word=random.choice(hard)
while run:
    if c!=0:
        draw()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                mx,my=pygame.mouse.get_pos()
                for j in letters:
                    x,y,l,b=j
                    if b:
                        dis=((x-mx)**2+(y-my)**2)**0.5
                        if dis<gap:
                            j[3]=False
                            if l in word:
                                guessed.append(l)
                            else:
                                status+=1
        win=True
        for j in word:
            if j not in guessed:
                win=False
                break
        if win:
            screen.fill("beige")
            text2=message.render("YOU WON",1,black)
            screen.blit(text2,(400-text2.get_width()/2,200-text2.get_height()/2))
            pygame.display.update()
            pygame.time.delay(5000)
            break
        if status == 6:
            screen.fill("beige")
            text=font.render(word,1,black)
            screen.blit(text,(400-text.get_width()/2,20))
            text2=message.render("GAME OVER",1,black)
            screen.blit(text2,(400-text2.get_width()/2,200-text2.get_height()/2))
            pygame.display.update()
            pygame.time.delay(5000)
            break

pygame.quit()