import pygame
import random

# calculates focus of one given und one randomly chosen of 3 given points
# Then draws a pixel on the focuspoint in one of 3, colors depending on the chosen vertex
def bridge(firstx, firsty, secondx:list, secondy:list):
        randomvar = random.choice(range(3))
        point4x,point4y = (firstx+secondx[randomvar])/2, (firsty+secondy[randomvar])/2
        screen.set_at((int(point4x),int(point4y)),COLORS[randomvar])
        return point4x, point4y

# initialize pygame
pygame.init()

# define colors in RGB
WHITE = (255,255,255)
BLACK = (0,0,0)
COLORS = [(0,0,255),(0,255,0),(255,0,0)]

# create a white window with caption
pygame.display.set_caption("Sierpiński triangle")
screen = pygame.display.set_mode((1000, 1000))
screen.fill(WHITE)
pygame.display.flip()

# wait for mouse clicks and create 4 starting points
for i in range(4):
    wait = True
    while wait:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                wait = False
                if i == 0:
                    point1_x, point1_y = pygame.mouse.get_pos()
                    pygame.draw.circle(screen,BLACK,(point1_x, point1_y),5)
                if i == 1:
                    point2_x, point2_y = pygame.mouse.get_pos()
                    pygame.draw.circle(screen,BLACK,(point2_x, point2_y),5)
                if i == 2:
                    point3_x, point3_y = pygame.mouse.get_pos()
                    pygame.draw.circle(screen,BLACK,(point3_x, point3_y),5)
                if i == 3:
                    point_oth_x, point_oth_y = pygame.mouse.get_pos()
                    pygame.draw.circle(screen,BLACK,(point_oth_x, point_oth_y),5)
                pygame.display.flip()


# create first point between 4th and random point
point_new_x,point_new_y = bridge(point_oth_x,point_oth_y,(point1_x,point2_x,point3_x),(point1_y,point2_y,point3_y))

# repeat creating focuspoints
for i in range(3_000_000):
    point_new_x,point_new_y = bridge(point_new_x,point_new_y,(point1_x,point2_x,point3_x),(point1_y,point2_y,point3_y))
pygame.display.flip()


# wait for closing window
wait = True
while wait:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            wait = False

# quit
pygame.quit()