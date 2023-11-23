import pygame
from data import *
pygame.init()

# створення персонажу гри
class Sprite(pygame. Rect):
    def __init__(self, x,y,width,height,color= (120,100,150), image= None, speed= 5 ):
        super().__init__(x,y,width,height)
        self.COLOR = color
        self.IMAGE_LIST = image
        self.IMAGE = self.IMAGE_LIST[0]
        self.IMAGE_COUNT = 0
        self.IMAGE_NOW = self.IMAGE
        self.SPEED = speed

    def move_image(self):
        self.IMAGE_COUNT     +=1
        if self.IMAGE_COUNT == len(self.IMAGE_LIST) * 10 - 1:
            self.IMAGE_COUNT = 0
        if self.IMAGE_COUNT % 10 == 0:
            self.IMAGE = self.IMAGE_LIST[self.IMAGE_COUNT // 10]

class Hero(Sprite):
    def __init__ (self,  x,y,width,height,color= (120,120,120), image= None, speed= 5 ):
        super().__init__(x,y,width,height, color, image, speed)
        self.MOVE = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}
        self.DIRECTION = False
        self.HP = 3

    def move(self, window): #Рух гравця
        if self.MOVE["UP"] and self.y >0:
            self.y -= self.SPEED
            if self.collidelist(wall_list) != -1:
                self.y += self.SPEED
        elif self.MOVE["DOWN"] and self.y < setting_win["HEIGHT"] - self.height:
            self.y += self.SPEED
            if self.collidelist(wall_list) != -1:
                self.y -= self.SPEED
        if self.MOVE["LEFT"] and self.x >0:
            self.x -= self.SPEED
            if self.collidelist(wall_list) != -1:
                self.x += self.SPEED
            self.DIRECTION = False
        elif self.MOVE["RIGHT"] and self.x < setting_win["WIDTH"] - self.width:
            self.x += self.SPEED
            if self.collidelist(wall_list) != -1:
                self.x -= self.SPEED
            self.DIRECTION = True



        if self.MOVE["UP"] or self.MOVE ["DOWN"] or self.MOVE["LEFT"] or self.MOVE ["RIGHT"]:
            self.move_image()
        else:
            self.IMAGE = self.IMAGE_LIST[1]
        if self.DIRECTION:
            self.IMAGE_NOW = pygame.transform.flip(self.IMAGE, True, False)
        else:
            self.IMAGE_NOW = self.IMAGE
        window.blit(self.IMAGE_NOW, (self.x, self.y))

class Bot(Sprite): #Створення бота
    def __init__ (self,  x,y,width,height,color= (120,120,120), image= None, speed= 5, orientation= None ):
        super().__init__(x,y,width,height, color, image, speed)
        self.ORIENTATION= orientation

    def move(self, window, hero):
        if self.ORIENTATION.lower() == "horizontal": #Напрямок руху бота
            self.x += self.SPEED
            if self.collidelist(wall_list) != -1 or self.x <=0 or self.x + self.width >= setting_win["WIDTH"]:
                self.SPEED *= -1
        if self.ORIENTATION.lower() == "vertical": #Напрямок руху бота
            self.x += self.SPEED
            if self.collidelist(wall_list) != -1 or self.y <=0 or self.y + self.height >= setting_win["HEIGHT"]:
                self.SPEED *= -1
        if hero.colliderect(self):
            hero.HP -= 1
            hero.x, hero.y = 30,30     


        self.move_image()
        window.blit(self.IMAGE, (self.x, self.y))        
def create_wall(key):
    #Створеня стін лабіринту
    x,y = 0,0
    index_x, index_y = 0,0
    width = 20

    for string in maps[key]:
        for elem in string:
            if elem == "1":
                for index in range(index_y, len(maps[key])):
                    if maps[key][index][index_x] == "2":
                        wall_list.append(pygame.Rect(x,y, width, (index - index_y) * width + width))
                        break
            if elem == "3":
                for index in range(index_x, len(maps[key][index_y])):
                    if maps[key][index_y][index] == "2":
                        wall_list.append(pygame.Rect(x,y, (index - index_x) * width + width, width))
                        break
            x += width
            index_x += 1
        x = 0
        index_x = 0
        y += width
        index_y +=1


create_wall("MAP1")