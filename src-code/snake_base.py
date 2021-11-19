import pygame
import time
import random
import numpy as np

class Snake_base():
    def __init__(self):
        pygame.init()
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 102)
        self.black = (0, 0, 0)
        self.red = (213, 50, 80)
        self.green = (0, 255, 0)
        self.blue = (50, 153, 213)
        self.grey = (128, 128, 128)
        self.dark_g = (50, 50, 50)

        # Dimensions
        self.dis_width = 600
        self.dis_height = 400


        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))

        # Caption
        pygame.display.set_caption('~ Snake ~')

        # Time 
        self.clock = pygame.time.Clock()
        
        # Speed & Length
        self.snake_block = 10
        self.snake_speed = 13

        # Font
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)
         
        # Score & Message
    def Your_score(self, score):
        self.value = score_font.render("Score: " + str(score), True, dark_g)
        dis.blit(value, [0, 0])

    def our_snake(self, snake_block, snake_array): # The issue
        for x in snake_array:
            print(x)
            pygame.draw.rect(self.dis, self.black, [x[0], x[1], self.snake_block, self.snake_block])

    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [dis_width / 6, dis_height / 3])
     

    def gameLoop(self):
        start_game = time.time()
        game_over = False
        game_close = False
     
        x1 = self.dis_width / 2
        y1 = self.dis_height / 2
     
        x1_change = 0
        y1_change = 0
     
        snake_array = np.array([])
        Length_of_snake = 1
     
        foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0
     
        while not game_over:
     
            while game_close == True:
                self.dis.fill(self.grey)
                self.message("You Lost! Press C-Play Again or Q-Quit", self.dark_g)
                self.Your_score(Length_of_snake - 1)
                pygame.display.update()
     
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            self.gameLoop()
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = - self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = - self.snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = self.snake_block
                        x1_change = 0
     
            if x1 >= self.dis_width or x1 < 0 or y1 >= self.dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            self.dis.fill(self.grey)
            pygame.draw.rect(self.dis, self.red, [foodx, foody, self.snake_block, self.snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_array = np.append(snake_array, snake_Head) # Array Appends value 
            print(snake_array)
            if len(snake_array) > Length_of_snake:
                snake_array = np.delete(snake_array, 0)
                print(snake_array) # prints 300.0, 200.0
     
            for x in snake_array[:-1]:
                if np.any(x == snake_Head) == True:
                    game_close = True

            end_game = time.time()
            print(str(end_game - start_game))

            self.our_snake(self.snake_block, snake_array)
            self.Your_score(Length_of_snake - 1)
     
            pygame.display.update()
     
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0
                Length_of_snake += 1
     
            self.clock.tick(self.snake_speed)

        pygame.quit()
        quit()
             
             
G = Snake_base()
G.gameLoop()
