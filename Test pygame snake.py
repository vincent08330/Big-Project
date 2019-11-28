import pygame
from pygame.locals import *

pygame.init()
taille_fenetre = (600,400)
fenetre_rect = pygame.Rect((0,0), taille_fenetre)
screen_surface = pygame.display.set_mode(taille_fenetre)

bleu_nuit = (  5,   5, 30)
vert      = (  0, 255,  0)
rouge     = (255,   0)

timer = pygame.time.Clock()

snake = pygame.Surface((25, 25))
snake.fill(rouge)

x, y = 25, 100
vx, vy = 0, 0

gravité = 0

mur = pygame.Surface((25, 25))
mur.fill(vert)

niveau = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

def dessiner_niveau(surface, niveau):

    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                surface.blit(mur, (i*25, j*25))


continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT :
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                vy = -20

    timer.tick(30)
    keys_pressed = pygame.key.get_pressed()
    vx = (keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]) * 5
    vy = (keys_pressed[K_DOWN] - keys_pressed[K_UP]) * 5
    vy = min(20, vy)
    x += vx
    y += vy
    y = min(300, y)

    screen_surface.fill(bleu_nuit)
    dessiner_niveau(screen_surface, niveau)
    screen_surface.blit(snake, (x, y))
    pygame.display.flip()

pygame.quit()
