import random
import pygame
import os
pygame.init()
FENETRE_X = 500
FENETRE_Y = 500
screen = pygame.display.set_mode((FENETRE_X, FENETRE_Y))


def generate_bombe(grille):

    n = len(grille[0])*(len(grille)-2)

    while n > 0:
        for i in range(len(grille)):
            for j in range(len(grille[i])):
                a = random.randint(0, 5)
                if a == 5:
                    grille[i][j] = 1
                    n -= 1


    return grille
grille = generate_bombe([
    [0, 0, 0, 0], 
    [0, 0, 0, 0],
    [0, 0, 0, 0]
    ])


def load_grille(grille):
    pass

while True:
    load_grille(grille)
    pygame.display.flip()

    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                game = 1
            if event.type == pygame.QUIT:
                running = False