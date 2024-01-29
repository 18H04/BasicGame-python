# game.py
import pygame
import time
import random
from snake import our_snake, Your_score

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
high_score = 0

# Show achievement
def show_achievements_screen(dis, dis_width, dis_height):
    achievements_screen = True

    while achievements_screen:
        dis.fill(BLACK)
        font = pygame.font.SysFont(None, 30)
        text = font.render("High Score: " + str(high_score), True, (255, 255, 255))
        dis.blit(text, (dis_width / 2 - 100, dis_height / 2 - 50))
        
        pygame.draw.rect(dis, (255, 255, 255), [dis_width / 2 - 70, dis_height / 2 + 50, 140, 40])
        button_font = pygame.font.SysFont(None, 30)
        button_text = button_font.render("Close", True, (0, 0, 0))
        button_rect = button_text.get_rect(center=(dis_width / 2, dis_height / 2 + 70))
        dis.blit(button_text, button_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                close_button_rect = pygame.Rect(dis_width / 2 - 70, dis_height / 2 + 50, 140, 40)
                if close_button_rect.collidepoint(mouseX, mouseY):
                    dis.fill(BLACK)
                    achievements_screen = False

# Show message
def message(dis, msg, color, dis_width, dis_height):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, color)
    
    text_rect = mesg.get_rect(center=(dis_width / 2, dis_height / 2 - 20))
    dis.blit(mesg, text_rect)
    pygame.display.update()

# Play button
def display_play_button(dis_width, dis_height, dis):
    pygame.draw.rect(dis, GREEN, [dis_width / 2 - 70, dis_height / 2 + 20, 140, 40])
    button_font = pygame.font.SysFont(None, 30)
    button_text = button_font.render("Play", True, BLACK)
    button_rect = button_text.get_rect(center=(dis_width / 2, dis_height / 2 + 40))
    dis.blit(button_text, button_rect)

    pygame.display.update()

# Achievement button
def display_achievements_button(dis_width, dis_height, dis):
    pygame.draw.rect(dis, (255, 165, 0), [dis_width / 2 - 70, dis_height / 2 + 120, 140, 40])
    button_font = pygame.font.SysFont(None, 30)
    button_text = button_font.render("Achievements", True, (0, 0, 0))
    button_rect = button_text.get_rect(center=(dis_width / 2, dis_height / 2 + 140))
    dis.blit(button_text, button_rect)
    
    pygame.display.update()
    
# Continue button 
def display_continues_button(dis_width, dis_height, dis):
    pygame.draw.rect(dis, GREEN, [dis_width / 2 - 70, dis_height / 2 + 20, 140, 40])
    button_font = pygame.font.SysFont(None, 30)
    button_text = button_font.render("Continues", True, BLACK)
    button_rect = button_text.get_rect(center=(dis_width / 2, dis_height / 2 + 40))
    dis.blit(button_text, button_rect)

    pygame.display.update()

# Quit button
def display_quit_button(dis_width, dis_height, dis):
    pygame.draw.rect(dis, RED, [dis_width / 2 - 70, dis_height / 2 + 70, 140, 40])
    button_font = pygame.font.SysFont(None, 30)
    button_text = button_font.render("Quit", True, BLACK)
    button_rect = button_text.get_rect(center=(dis_width / 2, dis_height / 2 + 90))
    dis.blit(button_text, button_rect)

# Replay button
def display_replay_button(dis_width, dis_height, dis):
    pygame.draw.rect(dis, YELLOW, [dis_width / 2 - 70, dis_height / 2 + 20, 140, 40])
    button_font = pygame.font.SysFont(None, 30)
    button_text = button_font.render("Replay", True, BLACK)
    button_rect = button_text.get_rect(center=(dis_width / 2, dis_height / 2 + 40))
    dis.blit(button_text, button_rect)
    

# Logic game
def gameLoop(dis_width, dis_height, dis, pygame, clock, snake_block, initial_snake_speed):
    play_button_clicked = False
    achievements_button_clicked = False
    quit_button_clicked = False
    replay_button_clicked = False
    paused = False
    snake_speed = initial_snake_speed
    return_to_main = False
    
    while not play_button_clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                play_button_rect = pygame.Rect(dis_width / 2 - 70, dis_height / 2 + 20, 140, 40)
                achievements_button_rect = pygame.Rect(dis_width / 2 - 70, dis_height / 2 + 120, 140, 40)
                
                if play_button_rect.collidepoint(mouseX, mouseY):
                    play_button_clicked = True
                elif achievements_button_rect.collidepoint(mouseX, mouseY):
                    show_achievements_screen(dis, dis_width, dis_height) 

        message(dis, "Snake Game", WHITE, dis_width, dis_height)
        display_play_button(dis_width, dis_height, dis)
        display_achievements_button(dis_width, dis_height, dis)
        pygame.display.update()

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over and not replay_button_clicked or not quit_button_clicked:
        while game_close == True:
            if return_to_main:
                break
            Your_score(dis, length_of_snake - 1)
            message(dis, "Game Over", (213, 50, 80), dis_width, dis_height)
            display_replay_button(dis_width, dis_height, dis)
            display_quit_button(dis_width, dis_height, dis)
            pygame.display.update()
            
            if length_of_snake - 1 > high_score:
                high_score = length_of_snake - 1

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    replay_button_rect = pygame.Rect(dis_width / 2 - 70, dis_height / 2 + 20, 140, 40)
                    quit_button_rect = pygame.Rect(dis_width / 2 - 70, dis_height / 2 + 70, 140, 40)

                    if replay_button_rect.collidepoint(mouseX, mouseY):
                        replay_button_clicked = True
                        game_close = False
                        x1 = dis_width / 2
                        y1 = dis_height / 2
                        x1_change = 0
                        y1_change = 0
                        snake_list = []
                        length_of_snake = 1
                        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

                    if quit_button_rect.collidepoint(mouseX, mouseY):
                        quit_button_clicked = True
                        game_over = True
                        return_to_main = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        
        while paused:
            message(dis, "Paused", WHITE, dis_width, dis_height)
            display_continues_button(dis_width, dis_height, dis)
            display_quit_button(dis_width, dis_height, dis)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    continue_button_rect = pygame.Rect(dis_width / 2 - 70, dis_height / 2 + 20, 140, 40)
                    quit_button_rect = pygame.Rect(dis_width / 2 - 70, dis_height / 2 + 70, 140, 40)

                    if continue_button_rect.collidepoint(mouseX, mouseY):
                        paused = False
                    elif quit_button_rect.collidepoint(mouseX, mouseY):
                        quit_button_clicked = True
                        return_to_main = True
                        game_close = False
                        paused = False

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill((0, 0, 0))
        pygame.draw.rect(dis, GREEN, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        if game_close:
            dis.fill((0, 0, 0))
            message(dis, "Game Over", (213, 50, 80), dis_width, dis_height)
            Your_score(dis, length_of_snake - 1)
            pygame.display.update()

        our_snake(dis, snake_block, snake_list)
        Your_score(dis, length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            
            if length_of_snake % 5 == 0:
                snake_speed += 1
            
        clock.tick(snake_speed)

    pygame.quit()
    quit()
