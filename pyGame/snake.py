import pygame

#Draw snake
def our_snake(dis, snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, (0, 0, 255), [x[0], x[1], snake_block, snake_block])

#Show scores
def Your_score(dis, score):
    font_style = pygame.font.SysFont(None, 50)
    value = font_style.render("Your Score: " + str(score), True, (255, 255, 255))
    dis.blit(value, [0, 0])
