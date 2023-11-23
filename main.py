
from data import *
from maze_funcion import *

#Створення вікна гри
window = pygame.display.set_mode((setting_win["WIDTH"], setting_win ["HEIGHT"]))
pygame.display.set_caption("Лабіринт")

#Головний цикл гри
def run ():
    key_check = True
    door_check = False
    hero = Hero(30,30,70,100, image = hero_list)  
    bot1 = Bot(300,500, 70,100, image= bot1_list, orientation= "horizontal")
    
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,100)

    game = True
    while game:
        window.fill((191,230,221))



        #x,y = 20,20
        #for i in range(50):
        #    pygame.draw.line (window, (255, 255, 255), (0, y), (1000, y))
        #    pygame.draw.line (window, (255, 255, 255), (x, 0), (x, 700))
        #    x +=20
        #    y +=20sdф
        for wall in wall_list:
            pygame.draw.rect(window, (255,255,255), wall)

        if hero.HP <= 0:
            hero.HP = 0
            hero.SPEED = 0
            window.blit(font.render("Ти програв", True, (0,0,50)), (setting_win["WIDTH"] // 2 - font.size("Ти програв") [0] // 2, setting_win["HEIGHT"] // 2))
        hero.move(window)
        bot1.move(window,hero)

        if key_check == True:
            window.blit(key_image, (620,200))
            if hero.colliderect(key_image.get_rect(topleft = (620,200))):
                key_check = False
            
        else:
            window.blit(door_image,(850, 40))
            if hero.colliderect(door_image.get_rect(topleft = (850,40))):
                door_check = True






        if door_check== True:
            hero.SPEED = 0
            window.blit(font.render("Ти переміг", True, (0,0,50)), (setting_win["WIDTH"] // 2 - font.size("Ти переміг") [0] // 2, setting_win["HEIGHT"] // 2))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game  = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    hero.MOVE["DOWN"] = True
                if event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = True
                if event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = False
                if event.key == pygame.K_s:
                    hero.MOVE["DOWN"] = False
                if event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = False
                if event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = False
        clock.tick(60)
        pygame.display.flip()


run()
