import pygame
import time
import random
from random import randrange
from tkinter import *




class Move():
    def __init__(self, Xmove, Ymove):
        # object attributes
        self.Xmove = Xmove
        self.Ymove = Ymove

class Food:
    # constructor (yapıcı metod)
    def __init__(self, name, point):
        # object attributes
        self.name = name
        self.point = point


food1=Food(name='normal food', point= 1)
food2=Food(name='good food', point= 6)
food3=Food(name='bad food', point= -6)

Left=Move(Xmove=-10,Ymove=0)
Right=Move(Xmove=10,Ymove=0)
Up=Move(Xmove=0,Ymove=-10)
Down=Move(Xmove=0,Ymove=10)








def game_time():
    pygame.init()

    width = 600
    height = 400

    dis = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Game Of Snakes')

    clock = pygame.time.Clock()
    snake_speed = speed_of_snake

    score_of_gaming=0
    finising_game = False
    closing_game = False

    x_locate = 100
    y_locate = 100

    x_change = 0
    y_change = 0

    snake = []
    Length_of_snake = 1
    dis.fill((238, 238, 0))


    meal_x = round(random.randrange(0, width - 10) / 10.0) * 10.0
    meal_y = round(random.randrange(0, height - 10) / 10.0) * 10.0
    special_food_x = round(random.randrange(0, width - 10) / 10.0) * 10.0
    special_food_y = round(random.randrange(0, height - 10) / 10.0) * 10.0
    bad_food_x = round(random.randrange(0, width - 10) / 10.0) * 10.0
    bad_food_y = round(random.randrange(0, height - 10) / 10.0) * 10.0
    start_n=0
    while not finising_game:

        font = pygame.font.SysFont("cambria", 25)
        while closing_game == True:
            dis.fill((4,29,104))
            dis.blit(pygame.font.SysFont("cambria", 35).render("Your Score:"+str(score_of_gaming*10), True, (213, 50, 80)), [width / 5, height / 8])
            dis.blit(pygame.font.SysFont("cambria", 35).render("YOU LOST!! ", True, (213, 50, 80)), [width / 4, height / 4])
            dis.blit(pygame.font.SysFont("cambria", 30).render("If you want play again press: A or   press Q ",
                                                                   True, (208,215,237)), [width / 30, height/2 ])

            pygame.display.update()

            for press in pygame.event.get():
                if press.type == pygame.KEYDOWN:
                    if press.key == pygame.K_q:
                        finising_game = True
                        closing_game = False
                    if press.key == pygame.K_a:
                        choise_of_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finising_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = Left.Xmove
                    y_change = Left.Ymove
                elif event.key == pygame.K_RIGHT:
                    x_change = Right.Xmove
                    y_change = Right.Ymove
                elif event.key == pygame.K_UP:
                    y_change = Up.Ymove
                    x_change = Up.Xmove
                elif event.key == pygame.K_DOWN:
                    y_change = Down.Ymove
                    x_change = Down.Xmove
                elif event.key == pygame.K_SPACE:
                    y_change = 0
                    x_change = 0

        if x_locate >= width or x_locate < 0 or y_locate >= height or y_locate < 0:
            closing_game = True
        x_locate = x_locate+x_change
        y_locate = y_locate+y_change
        dis.fill((255, 255, 255))

        # Good Food
        if score_of_gaming%5==0 and score_of_gaming != 0 :

            pygame.draw.rect(dis, (255,62,150), [special_food_x, special_food_y, 13, 13])

        #Bad Food
        if score_of_gaming%6==0 and score_of_gaming != 0 :

            pygame.draw.rect(dis, (0,0,0), [bad_food_x, bad_food_y, 13, 13])




        if x_locate == special_food_x and y_locate == special_food_y:
            #Length_of_snake =Length_of_snake+food2.point
            score_of_gaming=score_of_gaming+food2.point
            print(score_of_gaming)

            Length_of_snake =Length_of_snake+ 1

        if x_locate == bad_food_x and y_locate == bad_food_y:
           #Length_of_snake =Length_of_snake+food3.point
            score_of_gaming=Length_of_snake+food3.point
            print(score_of_gaming)
            Length_of_snake =Length_of_snake - 1

        pygame.draw.ellipse(dis, (255,99,71), [meal_x, meal_y, 10, 10])


        snake_Head = []
        snake_Head.append(x_locate)
        snake_Head.append(y_locate)
        snake.append(snake_Head)

        if len(snake) > Length_of_snake:
            del snake[0]



        for sn in snake:
            pygame.draw.rect(dis, calor_of_snake, [sn[0], sn[1], 10, 10])

        pygame.display.update()

        if x_locate == meal_x and y_locate == meal_y:
            meal_x = round(random.randrange(0, width - 10) / 10.0) * 10.0
            meal_y = round(random.randrange(0, height - 10) / 10.0) * 10.0
            score_of_gaming=score_of_gaming+ food1.point
            Length_of_snake =Length_of_snake+ 1
            print(score_of_gaming)

        clock.tick(snake_speed)

    pygame.quit()
    quit()







def set_color(a):
    global calor_of_snake
    calor_of_snake = a

def set_level(b):
    global speed_of_snake
    speed_of_snake = b


def choise_of_game():
    ruleofgames = Tk()
    ruleofgames.geometry("1200x600")

    Label(ruleofgames, text="Welcome to  Game Of Snakes " + "\n"
      +"Please Choose Your Snake"+"\n"
      ,font=('Helvetica', 15)).pack(pady= 5)



    Button(ruleofgames, text="Mudsnake", font=('Helvetica', 16), command=lambda: set_color((205, 55, 0))).pack(pady=1)
    Button(ruleofgames, text="Hognose", font=('Helvetica', 16), command=lambda: set_color((40,40,40))).pack(pady=1)
    Button(ruleofgames, text="Anakondo", font=('Helvetica', 16), command=lambda: set_color((84,255,159))).pack(pady=1)

    Label(ruleofgames, text="Please Choose Level" + "\n" ,font=('Helvetica', 15)).pack(pady= 1)
    Button(ruleofgames, text="Easy", font=('Helvetica', 16), command=lambda: set_level(10)).pack(pady=1)
    Button(ruleofgames, text="Medium", font=('Helvetica', 16), command=lambda: set_level(30)).pack(pady=1)
    Button(ruleofgames, text="Hard", font=('Helvetica', 16), command=lambda: set_level(50)).pack(pady=1)
    Button(ruleofgames, text= "Start Game", font=('Helvetica', 20),
    command=ruleofgames.destroy).pack(pady=80)
    ruleofgames.mainloop()
    game_time()


ruleofgames = Tk()

ruleofgames.geometry("1200x500")

Label(ruleofgames, text="WELCOME TO THE GAME OF SNAKES"+"\n"
      +"Rule of games"+"\n"
      +"There are 3 different snake options. You can choose the difficulty level for the game."+"\n"
      +"easy medium hard"+"\n"
      +"It is quite difficult to control the snake in hard mode."+"\n"
      +"You get 1 point for every meal you eat."+"\n"
      +"From time to time, special foods will appear in front of you. Some foods are good for you, while others are harmful to you.",
font=('Helvetica', 15)).pack(pady= 5)



Button(ruleofgames, text= "OKAY", font=('Helvetica', 16),
command=ruleofgames.destroy).pack(pady=1)

ruleofgames.mainloop()
choise_of_game()
