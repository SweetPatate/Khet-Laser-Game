import pygame, sys

def Pharaoh(gameboard,couleur, choice):
    if couleur == 1:
        if gameboard == 0:
            Object_pharaon = pygame.image.load('sprites/pack' + str(choice) + '/pieces/pharaon 1.png')
        elif gameboard == 1:
            Object_pharaon = pygame.image.load('sprites/pack' + str(choice) + '/pieces/pharaon 2.png')
        elif gameboard == 2:
            Object_pharaon = pygame.image.load('sprites/pack' + str(choice) + '/pieces/pharaon 3.png')
        elif gameboard == 3:
            Object_pharaon = pygame.image.load('sprites/pack' + str(choice) + '/pieces/pharaon 4.png')
    else:
        if gameboard == 0:
            Object_pharaon = pygame.image.load('sprites/pack' + str(choice) + '/pieces/pharaonb 1.png')
        elif gameboard == 1:
            Object_pharaon = pygame.image.load('sprites/pack' + str(choice) + '/pieces/pharaonb 2.png')
        elif gameboard == 2:
            Object_pharaon = pygame.image.load('sprites/pack' + str(choice) + '/pieces/pharaonb 3.png')
        elif gameboard == 3:
            Object_pharaon = pygame.image.load('sprites/pack' + str(choice) + '/pieces/pharaonb 4.png')

    Object_pharaon = pygame.transform.scale(Object_pharaon, (65, 70))
    return Object_pharaon

def scarab(gameboard,couleur, choice):
    if couleur == 1:
        if gameboard == 0:
            Object_scarab = pygame.image.load('sprites/pack' + str(choice) + '/pieces/scaraber 1.png')
        elif gameboard == 1:
            Object_scarab = pygame.image.load('sprites/pack' + str(choice) + '/pieces/scaraber 2.png')
        elif gameboard == 2:
            Object_scarab = pygame.image.load('sprites/pack' + str(choice) + '/pieces/scaraber 3.png')
        elif gameboard == 3:
            Object_scarab = pygame.image.load('sprites/pack' + str(choice) + '/pieces/scaraber 4.png')
    else:
        if gameboard == 0:
            Object_scarab = pygame.image.load('sprites/pack' + str(choice) + '/pieces/scaraberb 1.png')
        elif gameboard == 1:
            Object_scarab = pygame.image.load('sprites/pack' + str(choice) + '/pieces/scaraberb 2.png')
        elif gameboard == 2:
            Object_scarab = pygame.image.load('sprites/pack' + str(choice) + '/pieces/scaraberb 3.png')
        elif gameboard == 3:
            Object_scarab = pygame.image.load('sprites/pack' + str(choice) + '/pieces/scaraberb 4.png')
    Object_scarab = pygame.transform.scale(Object_scarab, (65, 70))
    return Object_scarab

def anubis(gameboard,couleur, choice):
    if couleur == 1:
        if gameboard == 0:
            Object_anubis = pygame.image.load('sprites/pack' + str(choice) + '/pieces/anubis 1.png')
        elif gameboard == 1:
            Object_anubis = pygame.image.load('sprites/pack' + str(choice) + '/pieces/anubis 2.png')
        elif gameboard == 2:
            Object_anubis = pygame.image.load('sprites/pack' + str(choice) + '/pieces/anubis 3.png')
        elif gameboard == 3:
            Object_anubis = pygame.image.load('sprites/pack' + str(choice) + '/pieces/anubis 4.png')
    else:
        if gameboard == 0:
            Object_anubis = pygame.image.load('sprites/pack' + str(choice) + '/pieces/anubisb 1.png')
        elif gameboard == 1:
            Object_anubis = pygame.image.load('sprites/pack' + str(choice) + '/pieces/anubisb 2.png')
        elif gameboard == 2:
            Object_anubis = pygame.image.load('sprites/pack' + str(choice) + '/pieces/anubisb 3.png')
        elif gameboard == 3:
            Object_anubis = pygame.image.load('sprites/pack' + str(choice) + '/pieces/anubisb 4.png')
    Object_anubis = pygame.transform.scale(Object_anubis, (65, 70))
    return Object_anubis

def pyramid(gameboard,couleur, choice):
    if couleur == 1:
        if gameboard == 0:
            Object_pyramid = pygame.image.load('sprites/pack' + str(choice) + '/pieces/mirroir 1.png')
        elif gameboard == 1:
            Object_pyramid = pygame.image.load('sprites/pack' + str(choice) + '/pieces/mirroir 2.png')
        elif gameboard == 2:
            Object_pyramid = pygame.image.load('sprites/pack' + str(choice) + '/pieces/mirroir 3.png')
        elif gameboard == 3:
            Object_pyramid = pygame.image.load('sprites/pack' + str(choice) + '/pieces/mirroir 4.png')
    else:
        if gameboard == 0:
            Object_pyramid = pygame.image.load('sprites/pack' + str(choice) + '/pieces/mirroirb 1.png')
        elif gameboard == 1:
            Object_pyramid = pygame.image.load('sprites/pack' + str(choice) + '/pieces/mirroirb 2.png')
        elif gameboard == 2:
            Object_pyramid = pygame.image.load('sprites/pack' + str(choice) + '/pieces/mirroirb 3.png')
        elif gameboard == 3:
            Object_pyramid = pygame.image.load('sprites/pack' + str(choice) + '/pieces/mirroirb 4.png')
    Object_pyramid = pygame.transform.scale(Object_pyramid, (65, 70))
    return Object_pyramid

def sphinh(gameboard,couleur, choice):
    if couleur == 1:
        if gameboard == 0:
            Object_spinh = pygame.image.load('sprites/pack' + str(choice) + '/pieces/laser 1.png')
        elif gameboard == 1:
            Object_spinh = pygame.image.load('sprites/pack' + str(choice) + '/pieces/laser 2.png')
        elif gameboard == 2:
            Object_spinh = pygame.image.load('sprites/pack' + str(choice) + '/pieces/laser 3.png')
        elif gameboard == 3:
            Object_spinh = pygame.image.load('sprites/pack' + str(choice) + '/pieces/laser 4.png')
    else:
        if gameboard == 0:
            Object_spinh = pygame.image.load('sprites/pack' + str(choice) + '/pieces/laserb 1.png')
        elif gameboard == 1:
            Object_spinh = pygame.image.load('sprites/pack' + str(choice) + '/pieces/laserb 2.png')
        elif gameboard == 2:
            Object_spinh = pygame.image.load('sprites/pack' + str(choice) + '/pieces/laserb 3.png')
        elif gameboard == 3:
            Object_spinh = pygame.image.load('sprites/pack' + str(choice) + '/pieces/laserb 4.png')
    Object_spinh = pygame.transform.scale(Object_spinh, (65, 70))
    return Object_spinh