import pygame, sys
import random
import socket
from pygame.locals import *
from Affichage import *
from Piéces import *
from variableinit import *
from ai import *

fpsClock = pygame.time.Clock()
pygame.init()
Surface = pygame.display.set_mode((1280, 720))
menu(Surface, select, choice, etat_son)
pygame.display.set_caption('Khet Laser Game 2.0')
game = True

def music(musique, etat_son):
    if etat_son == 1:
        if musique == 1:
            pygame.mixer.music.load('sound/pack_sound' + str(choice) + '/fond_sonore1.wav')
            pygame.mixer.music.play(loops = -1)
        elif musique == 2:
            pygame.mixer.music.load('sound/pack_sound' + str(choice) + '/fond_sonore2.wav')
            pygame.mixer.music.play(loops = -1)
    else:
        pygame.mixer.music.pause()

music(musique, etat_son)

while game:
    for event in pygame.event.get():
        if event.type == QUIT:
            game = False
        deplacement = pygame.mixer.Sound('sound/pack_sound' + str(choice) + '/deplacement.wav')
        destruction = pygame.mixer.Sound('sound/pack_sound' + str(choice) + '/destruction.wav')
        laser = pygame.mixer.Sound('sound/pack_sound' + str(choice) + '/laser.wav')

        if c_menu == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 1 <x < 30 and 5 < y < 35:
                    if etat_son == 1:
                        etat_son = 0
                        music(musique, etat_son)
                    else:
                        etat_son = 1
                        music(musique, etat_son)
                if 50 <= x <= 75 and 5 <= y <= 35:
                    c_menu_info = True
                    info(Surface, select_info, choice)

                if 95 < x < 135 and 5 <= y <= 35:
                    c_rules = True
                    rules(Surface, select)


        if c_rules == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                select_book = 0
                x, y = event.pos
                for i in range(4):
                    if 120 < x < 350 and 60 + i * 155 < y < 60 + (i + 1) * 155:
                        select_book = i
                        rules(Surface, select_book)
                if 80 <= x <= 120 and 5 <= y <= 30:
                    c_rules = True
                    c_menu = False
                    rules(Surface, select_book)
                if (x > 120 and y < 60) or (x < 120 and y > 30) or x > 1172 or y > 680:
                    menu(Surface, select, choice, etat_son)
                    c_rules = False
                    c_menu = True


        if c_solo == True or c_multi == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if x >= 1189 and x <= 1262 and y >= 11 and y <= 38:
                    if c_solo == True:
                        c_solo = False
                        pause = 1
                    else:
                        c_multi = False
                        pause = 2
                    c_menu_pause = True
                    c_menu = False
                    menupause(Surface, choice)
                    break


        if c_menu_info == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                for i in range(0, 8):
                    if 140 < x < 350 and 50 + i * 77 < y < 50 + (i + 1) * 77:  # Clique sur les onglets du menu
                        select_info = i
                        info(Surface, select_info, choice)
                if 50 <= x <= 75 and 5 <= y <= 30:
                    info(Surface, select_info, choice)
                    c_menu_info = True
                    c_menu = False
                if (x > 85 and y < 50) or (x < 100 and y > 30) or x > 1172 or y > 680:
                    menu(Surface, select, choice, etat_son)
                    c_menu_info = False
                    c_menu = True


        if c_verif_editeur == True:
            verif_editeur(Surface, choice)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if x < 100 or y < 50 or x > 1172 or x > 680:
                    c_verif_editeur =  False
                    c_editeur = True
                    editeuraffiche(Surface, gameBoard, piece, couleur, select, choice, etat_sauvegarde, test)


        elif c_menu_pause == True:
            if c_sauvegarde == False:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if x <= 332 or x >= 946 or y <= 64 or y >= 626:
                        c_menu_pause = False
                        if pause == 1:
                            c_solo = True
                            c_menu_pause = False
                            solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                        else:
                            c_multi = True
                            c_menu_pause = False
                            multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                    for i in range(4):
                        if x >= 503 and x <= 778 and y >= 101 + i * 125 and y <= 184 + i * 125:
                            if i == 0:
                                if pause == 1:
                                    c_solo = True
                                    c_menu_pause = False
                                    solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                                else:
                                    c_multi = True
                                    c_menu_pause = False
                                    multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                            elif i == 1:
                                read_save = open("map/map" + str(choice_map) + ".txt", "r")
                                gameBoard = eval(read_save.readline())
                                read_save.close()
                                action = 1
                                c_menu_pause == False
                                if pause == 1:
                                    solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                                else:
                                    multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                            elif i == 2:
                                c_sauvegarde = True
                                sauvegarder(Surface, choice, pause)

                            elif i == 3:
                                if c_multi_local == True:
                                    connexion_avec_client.close()
                                    connexion_principale.close()
                                c_menu_pause = False
                                c_menu = True
                                menu(Surface, select, choice,etat_son)
            else:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if x >= 505 and x <= 777 and y >= 517 and y <= 597:
                        c_sauvegarde = False
                        menupause(Surface,choice)
                    for i in range(4):
                        if x >= 505 and x <= 777 and y >= 101 + i * 125 and y <= 184 + i * 100:
                            save_board = open("save/solo/save" + str(i + 1) + ".txt", "w")
                            save_board.write(repr(gameBoard))
                            save_board.close()
                            sauvegarder(Surface,choice,pause)
                        if x >= 505 and x <= 777 and y >= 101 + i * 125 and y <= 184 + i * 100 and pause == 2:
                            save_board = open("save/multi/save" + str(i + 1) + ".txt", "w")
                            save_board.write(repr(gameBoard))
                            save_board.close()
                            sauvegarder(Surface,choice,pause)


        elif c_menu == True:
            if event.type == MOUSEMOTION:
                x, y = event.pos
                if 500 < x < 780 and 110 < y < 195:
                    select = 0
                    etat_menu = 1
                elif 500 < x < 780 and 210 < y < 295:
                    select = 1
                    etat_menu = 2
                elif 500 < x < 780 and 310 < y < 395:
                    select = 2
                elif 500 < x < 780 and 410 < y < 495:
                    select = 3
                elif 500 < x < 780 and 510 < y < 595:
                    select = 4
                else:
                    select = -1
                menu(Surface, select, choice, etat_son)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if select == 0:
                    c_menu_solo = True
                    c_menu = False
                    menuSolo(Surface, choice, choice_map, difficulty, T_joueur)
                elif select == 1:
                    c_menu = False
                    c_menu_multi = 1
                    menuMulti(Surface, choice, choice_map, difficulty, T_joueur)
                elif select == 2:
                    c_menu = False
                    c_editeur = True
                    test = [0 for i in range(12)]
                    editeuraffiche(Surface, gameBoard, piece, couleur, select, choice, etat_sauvegarde, test)
                    pygame.time.delay(200)
                elif select == 3:
                    c_menu = False
                    c_themes = True
                    themes(Surface, choice)
                elif select == 4:
                    game = False


        elif c_themes == True:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if 10 < x < 60 and 10 < y < 60:
                        c_themes = False
                        c_menu = True
                        select = -1
                        menu(Surface, select, choice, etat_son)
                    if 70 < x < 610:
                        if 30 < y < 350:
                            choice = 1
                            themes(Surface, choice)
                            music(musique, etat_son)
                    elif 670 < x < 1140:
                        if 30 < y < 350:
                            choice = 2
                            themes(Surface, choice)
                            music(musique, etat_son)


        elif c_editeur == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 1060 < x < 1100 and 650 < y < 685:
                    c_verif_editeur = True

                phara1, phara2, mir1,mir2, scar1, scar2, las1, las2, anub1, anub2, verif1, verif2 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

                for i in range(10):
                    for j in range(8):
                        if x >= gameBoard_coordonnée[i][j][0] and x <= gameBoard_coordonnée[i][j][0] + 65 and y >= gameBoard_coordonnée[i][j][1] and y <= gameBoard_coordonnée[i][j][1] + 65:
                            if gameBoard[i][j][1] == 0:
                                gameBoard[i][j][1] = piece + 1
                                gameBoard[i][j][0] = couleur
                            else:
                                gameBoard[i][j][1] = 0
                                gameBoard[i][j][0] = 0
                                gameBoard[i][j][2] = 0
                            if etat_son == True:
                                deplacement.play()

                        if gameBoard[i][j][0] == 1 and gameBoard[i][j][1] == 1:  # Pharaon Rouge
                            phara1 += 1
                        if gameBoard[i][j][0] == 2 and gameBoard[i][j][1] == 1:  # Pharaon Blanc
                            phara2 += 1
                        if gameBoard[i][j][0] == 1 and gameBoard[i][j][1] == 2:  # Scarabé Rouge
                            scar1 += 1
                        if gameBoard[i][j][0] == 2 and gameBoard[i][j][1] == 2:  # Scarabé Blanc
                            scar2 += 1
                        if gameBoard[i][j][0] == 1 and gameBoard[i][j][1] == 4:  # Miroir Rouge
                            mir1 += 1
                        if gameBoard[i][j][0] == 2 and gameBoard[i][j][1] == 4:  # Miroir Blanc
                            mir2 += 1
                        if gameBoard[i][j][0] == 1 and gameBoard[i][j][1] == 5:  # Laser Rouge
                            las1 += 1
                        if gameBoard[i][j][0] == 2 and gameBoard[i][j][1] == 5:  # Laser Blanc
                            las2 += 1

                        if gameBoard[0][0][0] == 1 and gameBoard[0][0][1] == 5 and gameBoard[0][0][2] == 0 and las1 == 1:
                            verif1 = 1
                        else:
                            verif1 = 0

                        if gameBoard[9][7][0] == 2 and gameBoard[9][7][1] == 5 and gameBoard[9][7][2] == 2 and las2 == 1:
                            verif2 = 1
                        else:
                            verif2 = 0

                verif_pions = [phara1, phara2, mir1,mir2, scar1, scar2, las1, las2]

                if 825 < x < 1015 and 670 < y < 770:
                    if verif1 == verif2 == 1 and phara1 == phara2 == 1 and mir1 > 0 and mir2 > 0 and scar1 > 0 and scar2 > 0:
                        etat_sauvegarde = 1
                        print("Configuration valide.")
                    else:
                        etat_sauvegarde = 0
                        print("Configuration erronée. ")

                for i in range(3):
                    if x >= 10 and x <= 310 and y >= 150 + i * 150 and y <= 250 + i * 150:
                        select = i + 1 + 3

                for i in range(5):
                    if x >= 480 and x <= 480 + 65 and y >= i * 100 + 150 and y <= i * 100 + 220:
                        piece = i
                        couleur = 2
                    if x >= 400 and x <= 400 + 65 and y >= i * 100 + 150 and y <= i * 100 + 220:
                        piece = i
                        couleur = 1
                editeuraffiche(Surface, gameBoard, piece, couleur, select, choice, etat_sauvegarde, verif_pions)

                if select == 4:
                    gameBoard = [[[0 for k in range(3)] for j in range(8)] for i in range(10)]
                    gameBoard[0][0][0] = 1
                    gameBoard[0][0][1] = 5
                    gameBoard[0][0][2] = 0
                    gameBoard[9][7][0] = 2
                    gameBoard[9][7][1] = 5
                    gameBoard[9][7][2] = 2
                    editeuraffiche(Surface, gameBoard, piece, couleur, select, choice, etat_sauvegarde, verif_pions)
                    select = 0
                elif select == 5:
                    if etat_sauvegarde == 1:
                        print('Sauvegarde effectuée.')
                        Save_editeur = open('save/editeur.txt', 'w')
                        Save_editeur.write(repr(gameBoard))
                        Save_editeur.close()
                        editeuraffiche(Surface, gameBoard, piece, couleur, select, choice, etat_sauvegarde, verif_pions)
                        select = 0
                    else:
                        print('Pas de sauvegarde possible, les conditions ne sont pas respectées.')
                elif select == 6:
                    select = 0
                    c_editeur = False
                    c_menu = True
                    menu(Surface, select, choice, etat_son)

            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                x, y = event.pos
                for i in range(10):
                    for j in range(8):
                        if x >= gameBoard_coordonnée[i][j][0] and x <= gameBoard_coordonnée[i][j][0] + 65 and y >= gameBoard_coordonnée[i][j][1] and y <= gameBoard_coordonnée[i][j][1] + 65:
                            gameBoard[i][j][2] += 1
                            pygame.time.delay(200)
                            if gameBoard[i][j][2] == 4:
                                gameBoard[i][j][2] = 0
                            if etat_son == True:
                                deplacement.play()
                editeuraffiche(Surface, gameBoard, piece, couleur, select, choice, etat_sauvegarde, verif_pions)


        elif c_menu_solo == True:
            if c_chargement == False:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if 135 < y < 180:
                        if 315 <= x <= 405:
                            difficulty = 1

                    if 285 < y < 320:
                        if 320 < x < 425:
                            T_joueur = 1
                            etat_alea = 0
                        elif 520 < x < 675:
                            T_joueur = 2
                            etat_alea = 0
                        elif 765 < x < 900:
                            T_joueur = 3
                            etat_alea = 1

                    if 450 < y < 500:
                        if 350 < x < 400:
                            choice_map -= 1
                            if choice_map == 0:
                                choice_map = 1

                        elif 870 < x < 925:
                            choice_map += 1
                            if choice_map == 6:
                                choice_map = 5

                    if 640 < y < 700:
                        if 15 < x < 185:
                            c_menu_solo = False
                            c_menu = True

                        elif 550 < x < 725:
                            pass

                    menuSolo(Surface, choice, choice_map, difficulty, T_joueur)
                    for i in range(3):
                        if x >= 10 + i * 540 and x <= 190 + i * 540 and 675 <= y <= 700:
                            if i == 0:
                                c_menu_solo = False
                                c_menu = True
                                menu(Surface, select, choice, etat_son)
                            elif i == 1:
                                c_chargement = True
                                Chargersolo(Surface, choice)
                            elif i == 2:
                                c_menu_solo = False
                                c_solo = True

                                if choice_map == 5:
                                    choice_map = random.randrange(1, 5)
                                if choice_map == 4:
                                    read_save = open("save/editeur.txt", "r")
                                else:
                                    read_save = open("map/map" + str(choice_map) + ".txt", "r")
                                gameBoard = eval(read_save.readline())

                                read_save.close()
                                solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)
            else:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if x <= 332 or x >= 946 or y <= 64 or y >= 626:
                        c_chargement = False
                        menuSolo(Surface, choice, choice_map, difficulty, T_joueur)
                    if x >= 502 and x <= 779 and y >= 513 and y <= 599:
                        c_chargement = False
                        menuSolo(Surface, choice, choice_map, difficulty, T_joueur)
                    for i in range(3):
                        if x >= 504 and x <= 780 and y >= 113 + i * 100 and y <= 198 + i * 100:
                            read_save = open("save/solo/save" + str(i + 1) + ".txt", "r")
                            look_saveb = read_save.read()
                            if look_saveb != "":
                                gameBoard = eval(look_saveb)
                                solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                                c_menu_solo = False
                                c_solo = True
                            read_save.close()

                        if x >= 427 and x <= 484 and y >= 124 + i * 100 and y <= 180 + i * 100:
                            look_save = open("save/solo/save" + str(i + 1) + ".txt", "w")
                            look_save.write('')
                            look_save.close()
                            Chargersolo(Surface, choice)


        elif c_solo == True:
            if var1 == 1:
                musique = 2
                music(musique,etat_son)
                var1 = 2

            if etat_alea == 1:
                T_joueur = randint(1, 2)
                etat_alea = 0

            if T_joueur == 2:
                select_piéce, new_position, new_rotation = choose_piece(gameBoard, T_joueur, Surface, gameBoard_coordonnée, choice)
                piece_player = gameBoard[select_piéce[0]][select_piéce[1]][0]
                piece_type = gameBoard[select_piéce[0]][select_piéce[1]][1]
                piece_rotation = gameBoard[select_piéce[0]][select_piéce[1]][2]
                if piece_type != 0 and piece_player == T_joueur and select_piéce != [-1, -1]:
                    if gameBoard[new_position[0]][new_position[1]] == gameBoard[select_piéce[0]][select_piéce[1]]:
                        gameBoard[select_piéce[0]][select_piéce[1]][2] = new_rotation
                    else:
                        if gameBoard[new_position[0]][new_position[1]][1] == 0:
                            gameBoard[new_position[0]][new_position[1]] = gameBoard[select_piéce[0]][select_piéce[1]]
                            gameBoard[select_piéce[0]][select_piéce[1]] = [0, 0, 0]
                        else:
                            piece_copy = gameBoard[new_position[0]][new_position[1]]
                            gameBoard[new_position[0]][new_position[1]] = gameBoard[select_piéce[0]][select_piéce[1]]
                            gameBoard[select_piéce[0]][select_piéce[1]] = piece_copy
                action = 1
                pygame.time.delay(3000)
                if action == 1 and T_joueur == 2:
                    pygame.mixer.music.load("sound/laser.wav")
                    pygame.mixer.music.play()
                    select_piéce = [-1, -1]
                    solo(Surface, gameBoard, T_joueur,select, select_piéce, choice)
                    direction = A_laser(Surface, gameBoard,gameBoard_coordonnée, T_joueur, choice, need_rotat= False)
                    action = 0
                    if T_joueur == 1:
                        T_joueur = 2
                    else:
                        T_joueur = 1
                    if gameBoard[direction[0]][direction[1]][1] == 1 and direction != [-1, -1]:
                        gameBoard[direction[0]][direction[1]][0] = 0
                        gameBoard[direction[0]][direction[1]][1] = 0
                        gameBoard[direction[0]][direction[1]][2] = 0
                        win(Surface, T_joueur, choice)
                        c_multi = False
                    else:
                        solo(Surface, gameBoard, T_joueur,
                             select, select_piéce, choice)
                    if direction != [-1, -1]:
                        gameBoard[direction[0]][direction[1]][0] = 0
                        gameBoard[direction[0]][direction[1]][1] = 0
                        gameBoard[direction[0]][direction[1]][2] = 0
                        if etat_son == True:
                            pygame.mixer.music.load("sound/destruction.wav")
                            pygame.mixer.music.play()
                    action = 1


            if event.type == MOUSEBUTTONDOWN and event.button == 1 and T_joueur == 1:
                x, y = event.pos
                if action != 0:
                    for i in range(10):
                        for j in range(8):
                            if x >= gameBoard_coordonnée[i][j][0] and x <= gameBoard_coordonnée[i][j][0] + 65 and y >= gameBoard_coordonnée[i][j][1] and y <= gameBoard_coordonnée[i][j][1] + 65:
                                if T_joueur == gameBoard[i][j][0]:
                                    if gameBoard[select_piéce[0]][select_piéce[1]][1] == 2:
                                        if gameBoard[i][j][1] == 3 or gameBoard[i][j][1] == 4:
                                            pass
                                        else:
                                            select_piéce = [i, j]
                                            solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                                    else:
                                        select_piéce = [i, j]
                                        solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)

                    if gameBoard[select_piéce[0]][select_piéce[1]][1] != 5:
                        for i in range(3):
                            for j in range(3):
                                if select_piéce[0] - 1 + i < 0 or select_piéce[1] - 1 + j < 0 or select_piéce[0] - 1 + i > 9 or select_piéce[1] - 1 + j > 7 :
                                    pass
                                elif x >= gameBoard_coordonnée[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0] and x <= gameBoard_coordonnée[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0] + 65 and y >= gameBoard_coordonnée[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] and y <= gameBoard_coordonnée[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] + 65 and select_piéce != [-1, -1]:
                                    if i == 1 and j == 1:
                                        None
                                    if gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 1 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 2 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 3 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 4 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 5:
                                        None
                                    else:
                                        if select_piéce[0] - 1 + i >= 0 or select_piéce[1] - 1 + j >= 0:
                                            gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0] = gameBoard[select_piéce[0]][select_piéce[1]][0]
                                            gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] = gameBoard[select_piéce[0]][select_piéce[1]][1]
                                            gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][2] = gameBoard[select_piéce[0]][select_piéce[1]][2]
                                            gameBoard[select_piéce[0]][select_piéce[1]][0] = 0
                                            gameBoard[select_piéce[0]][select_piéce[1]][1] = 0
                                            gameBoard[select_piéce[0]][select_piéce[1]][2] = 0
                                            select_piéce = [-1, -1]
                                            action -= 1
                                            if etat_son == True:
                                                deplacement.play()
                                            solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                                    if gameBoard[select_piéce[0]][select_piéce[1]][1] == 2:
                                        if gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 1 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 2 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 5:
                                            None
                                        else:
                                            gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0],gameBoard[select_piéce[0]][select_piéce[1]][0] = gameBoard[select_piéce[0]][select_piéce[1]][0],gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0]
                                            gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1],gameBoard[select_piéce[0]][select_piéce[1]][1] = gameBoard[select_piéce[0]][select_piéce[1]][1],gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1]
                                            gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][2],gameBoard[select_piéce[0]][select_piéce[1]][2] = gameBoard[select_piéce[0]][select_piéce[1]][2],gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][2]
                                            select_piéce = [-1, -1]
                                            action -= 1
                                            if etat_son == True:
                                                deplacement.play()
                                            solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)



                    if select_piéce != [-1, -1]:
                        if x >= 65 + 600 and x <= 65 + 665 and y >= 8 * 65 + 125 and y <= 8 * 65 + 200:
                            if gameBoard[select_piéce[0]][select_piéce[1]][2] == 3:
                                gameBoard[select_piéce[0]][select_piéce[1]][2] = 0
                            else:
                                gameBoard[select_piéce[0]][select_piéce[1]][2] += 1
                            action -= 1
                            if etat_son == True:
                                deplacement.play()
                            select_piéce = [-1, -1]
                            solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                        elif x >= 8 * 65 + 600 and x <= 8 * 65 + 665 and y >= 8 * 65 + 125 and y <= 8 * 65 + 200:
                            if gameBoard[select_piéce[0]][select_piéce[1]][2] == 0:
                                gameBoard[select_piéce[0]][select_piéce[1]][2] = 3
                            else:
                                gameBoard[select_piéce[0]][select_piéce[1]][2] -= 1
                            action -= 1
                            if etat_son == True:
                                deplacement.play()
                            select_piéce = [-1, -1]
                            solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                if x >= 890 and x <= 1075 and y >= 665 and y <= 710 and action == 0 and T_joueur == 1:
                    if etat_son == 1:
                        laser.play()
                    select_piéce = [-1, -1]
                    solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                    direction = A_laser(Surface, gameBoard, gameBoard_coordonnée, T_joueur, choice, need_rotat= False)
                    pygame.time.delay(2000)
                    if T_joueur == 1:
                        T_joueur = 2
                    else:
                        T_joueur = 1
                    if gameBoard[direction[0]][direction[1]][1] == 1 and direction != [-1, -1]:
                        if T_joueur == 1:
                            T_joueur = 2
                        else:
                            T_joueur = 1
                        gameBoard[direction[0]][direction[1]][0] = 0
                        gameBoard[direction[0]][direction[1]][1] = 0
                        gameBoard[direction[0]][direction[1]][2] = 0
                        c_solo = False
                        c_win = True
                    else:
                        solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                    if direction != [-1, -1]:
                        gameBoard[direction[0]][direction[1]][0] = 0
                        gameBoard[direction[0]][direction[1]][1] = 0
                        gameBoard[direction[0]][direction[1]][2] = 0
                        if etat_son == True:
                            destruction.play()
                        if c_multi == True:
                            solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)

            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                select_piéce = [-1, -1]
                solo(Surface, gameBoard, T_joueur, select, select_piéce, choice)


        elif c_menu_multi == True:
            if c_chargement == False:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if 135 < y < 180:
                        if 315 <= x <= 475:
                            type = 1
                        elif 515 <= x <= 650:
                            type = 2
                        elif 715 < x < 860:
                            type = 3
                            menuMulti(Surface, choice, choice_map, type, T_joueur)
                            pygame.display.update()

                    if type != 3:
                        if 285 < y < 320:
                            if 320 < x < 445:
                                T_joueur = 1
                            elif 520 < x < 640:
                                T_joueur = 2
                            elif 765 < x < 900:
                                T_joueur = 3
                                etat_alea = 1

                        if 450 < y < 500:
                            if 350 < x < 400:
                                choice_map -= 1
                                if choice_map == 0:
                                    choice_map = 1

                            elif 870 < x < 925:
                                choice_map += 1
                                if choice_map == 6:
                                    choice_map = 5

                    if 640 < y < 700:
                        if 15 < x < 185:
                            c_menu_multi = False
                            c_menu = True


                    menuMulti(Surface, choice, choice_map, type, T_joueur)
                    for i in range(3):
                        if x >= 10 + i * 540 and x <= 190 + i * 540 and 675 <= y <= 700:
                            if i == 0:
                                c_menu_multi = False
                                c_menu = True
                                menu(Surface, select, choice, etat_son)
                            elif i == 1:
                                c_chargement = True
                                Chargermulti(Surface, choice)
                            elif i == 2:
                                c_menu_multi = False
                                c_multi = True

                                if choice_map == 5:
                                    choice_map = random.randrange(1, 5)
                                if choice_map == 4:
                                    read_save = open("save/editeur.txt", "r")
                                else:
                                    read_save = open("map/map" + str(choice_map) + ".txt", "r")
                                gameBoard = eval(read_save.readline())



                                if type == 1:
                                    c_multi = True
                                    multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                                elif type == 2:
                                    client = 0
                                    c_menu_hebergement = True
                                    etatserveur = 0
                                    menu_hebergement(Surface, choice, etatserveur, client)
                                elif type == 3:
                                    c_menu_rejoindre = True
                                    etatserveur = 0
                                    ip = ""
                                    menu_rejoindre(Surface, choice, etatserveur, ip)
            else:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if x <= 332 or x >= 946 or y <= 64 or y >= 626:
                        c_chargement = False
                        menuMulti(Surface, choice, choice_map, type, T_joueur)
                    if x >= 502 and x <= 779 and y >= 513 and y <= 599:
                        c_chargement = False
                        menuMulti(Surface, choice, choice_map, type, T_joueur)
                    for i in range(3):
                        if x >= 504 and x <= 780 and y >= 113 + i * 100 and y <= 198 + i * 100:
                            read_save = open("save/multi/save" + str(i + 1) + ".txt", "r")
                            look_saveb = read_save.read()
                            if look_saveb != "":
                                gameBoard = eval(look_saveb)
                                c_menu_multi = False
                                c_multi = True
                                multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                            read_save.close()

                        if x >= 427 and x <= 484 and y >= 124 + i * 100 and y <= 180 + i * 100:
                            look_save = open("save/multi/save" + str(i + 1) + ".txt", "w")
                            look_save.write('')
                            look_save.close()
                            Chargermulti(Surface, choice)


        elif c_menu_hebergement == True:
            hote = ''
            port = 12800
            msg_recu = b""
            msg_a_envoyer = b""
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                if y >= 647 and y <= 697:
                    if x >= 315 and x <= 481:
                        c_menu_rejoindre = False
                        c_menu_multi = True
                        menuMulti(Surface, choice, choice_map, type, T_joueur)
                    elif x >= 856 and x <= 1023 and client == 3 and etatserveur == 1:
                        connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        connexion_avec_serveur.connect((infos_connexion[0], port))
                        gameBoardprint = repr(gameBoard)
                        msg_a_envoyer = gameBoardprint
                        msg_a_envoyer = msg_a_envoyer.encode()
                        connexion_avec_serveur.send(msg_a_envoyer)
                        c_menu_hebergement = False
                        c_multi_local = True
                        multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                        action = 1
                        etat = 2
                        compt = 0

                if x >= 565 and x <= 734 and y >= 343 and y <= 390:
                    connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    connexion_principale.bind((hote, port))
                    connexion_principale.listen(5)
                    etatserveur = 1
                    client = 2
                    menu_hebergement(Surface, choice, etatserveur, client)
                    pygame.display.update()
                    connexion_avec_client, infos_connexion = connexion_principale.accept()
                    connexion_avec_client.settimeout(1)
                    msg_recu = connexion_avec_client.recv(1024)
                    if msg_recu == b"okclient":
                        client = 3
                        menu_hebergement(Surface, choice, etatserveur, client)


        elif c_menu_rejoindre == True:
            hote = ''
            port = 12800
            msg_recu = b""
            msg_a_envoyer = b""
            if event.type == KEYDOWN:
                if event.unicode.isdigit():
                    ip += event.unicode
                if event.key == K_PERIOD or event.key == K_KP_PERIOD:
                    ip += event.unicode
                if event.key == K_BACKSPACE:
                    ip = ip[:-1]
                menu_rejoindre(Surface, choice, etatserveur,ip)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                if y >= 647 and y <= 697:
                    if x >= 315 and x <= 481:
                        c_menu_rejoindre = False
                        c_menu_multi = True
                        menuMulti(Surface, choice, choice_map, type, T_joueur)
                if x >= 565 and x <= 734 and y >= 343 and y <= 390:
                    connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    connexion_principale.bind((hote, port))
                    connexion_principale.listen(5)
                    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    connexion_avec_serveur.connect((ip, port))
                    msg_a_envoyer = b"okclient"
                    connexion_avec_serveur.send(msg_a_envoyer)
                    etatserveur = 1
                    menu_rejoindre(Surface, choice, etatserveur, ip)
                    pygame.display.update()
                    connexion_avec_client, infos_connexion = connexion_principale.accept()
                    connexion_avec_client.settimeout(1)
                    msg_recu = connexion_avec_client.recv(1024)
                    gameBoard = eval(msg_recu)
                    c_menu_rejoindre = False
                    c_multi_local = True
                    multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                    compt = 0
                    etat = 1


        elif c_multi_local == True:
            if var1 == 1:
                musique = 2
                music(musique, etat_son)
                var1 = 2

            if etat == 1:
                while compt == 0:
                    if compt == 0:
                        try:
                            msg_recu = connexion_avec_client.recv(1024)
                        except socket.timeout:
                            continue
                        else:
                            gameBoard = eval(msg_recu)
                            if etat_son == True:
                                deplacement.play()
                            multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                            pygame.display.update()
                            compt += 1


                while compt == 1:
                    if compt == 1:
                        try:
                            msg_recu = connexion_avec_client.recv(1024)
                        except socket.timeout:
                            continue
                        else:
                            if etat_son == 1:
                                laser.play()
                            select_piéce = [-1, -1]
                            multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                            direction = A_laser(Surface, gameBoard, gameBoard_coordonnée, T_joueur, choice, need_rotat= False)
                            action = 1
                            if gameBoard[direction[0]][direction[1]][1] == 1 and direction != [-1, -1]:
                                connexion_avec_client.close()
                                connexion_principale.close()
                                gameBoard[direction[0]][direction[1]][0] = 0
                                gameBoard[direction[0]][direction[1]][1] = 0
                                gameBoard[direction[0]][direction[1]][2] = 0
                                if T_joueur == 1:
                                    T_joueur = 2
                                else:
                                    T_joueur = 1
                                c_multi_local = False
                                c_win = True
                            else:
                                multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                            if direction != [-1, -1]:
                                gameBoard[direction[0]][direction[1]][0] = 0
                                gameBoard[direction[0]][direction[1]][1] = 0
                                gameBoard[direction[0]][direction[1]][2] = 0
                                if etat_son == True:
                                    destruction.play()
                                if c_multi_local == True:
                                    multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                            etat = 2
                            compt = 0

            else:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if action != 0:
                        for i in range(10):
                            for j in range(8):
                                if x >= gameBoard_coordonnée[i][j][0] and x <= gameBoard_coordonnée[i][j][0] + 65 and y >= gameBoard_coordonnée[i][j][1] and y <= gameBoard_coordonnée[i][j][1] + 65:
                                    if T_joueur == gameBoard[i][j][0]:
                                        if gameBoard[select_piéce[0]][select_piéce[1]][1] == 2:
                                            if gameBoard[i][j][1] == 3 or gameBoard[i][j][1] == 4:
                                                pass
                                            else:
                                                select_piéce = [i, j]
                                                multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                                        else:
                                            select_piéce = [i, j]
                                            multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)

                        if gameBoard[select_piéce[0]][select_piéce[1]][1] != 5:
                            for i in range(3):
                                for j in range(3):
                                    if select_piéce[0] - 1 + i < 0 or select_piéce[1] - 1 + j < 0 or select_piéce[0] - 1 + i > 9 or select_piéce[1] - 1 + j > 7:
                                        pass
                                    elif x >= gameBoard_coordonnée[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0] and x <= gameBoard_coordonnée[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0] + 65 and y >= gameBoard_coordonnée[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] and y <= gameBoard_coordonnée[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] + 65 and select_piéce != [-1, -1]:
                                        if i == 1 and j == 1:
                                            None
                                        if gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 1 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 2 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 3 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 4 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 5:
                                            None
                                        else:
                                            if select_piéce[0] - 1 + i >= 0 or select_piéce[1] - 1 + j >= 0:
                                                gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0] = gameBoard[select_piéce[0]][select_piéce[1]][0]
                                                gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] = gameBoard[select_piéce[0]][select_piéce[1]][1]
                                                gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][2] = gameBoard[select_piéce[0]][select_piéce[1]][2]
                                                gameBoard[select_piéce[0]][select_piéce[1]][0] = 0
                                                gameBoard[select_piéce[0]][select_piéce[1]][1] = 0
                                                gameBoard[select_piéce[0]][select_piéce[1]][2] = 0
                                                select_piéce = [-1, -1]
                                                action -= 1
                                                if etat_son == True:
                                                    deplacement.play()
                                                msg_a_envoyer = repr(gameBoard)
                                                msg_a_envoyer = msg_a_envoyer.encode()
                                                connexion_avec_serveur.send(msg_a_envoyer)
                                                multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)

                                        if gameBoard[select_piéce[0]][select_piéce[1]][1] == 2:
                                            if gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 1 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 2 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 5:
                                                None
                                            else:
                                                gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0], gameBoard[select_piéce[0]][select_piéce[1]][0] = gameBoard[select_piéce[0]][select_piéce[1]][0],gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0]
                                                gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1], gameBoard[select_piéce[0]][select_piéce[1]][1] = gameBoard[select_piéce[0]][select_piéce[1]][1], gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1]
                                                gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][2], gameBoard[select_piéce[0]][select_piéce[1]][2] = gameBoard[select_piéce[0]][select_piéce[1]][2],gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][2]
                                                select_piéce = [-1, -1]
                                                action -= 1
                                                if etat_son == True:
                                                    deplacement.play()
                                                msg_a_envoyer = repr(gameBoard)
                                                msg_a_envoyer = msg_a_envoyer.encode()
                                                connexion_avec_serveur.send(msg_a_envoyer)
                                                multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)

                        if select_piéce != [-1, -1]:
                            if x >= 65 + 600 and x <= 65 + 665 and y >= 8 * 65 + 125 and y <= 8 * 65 + 200:
                                if gameBoard[select_piéce[0]][select_piéce[1]][2] == 3:
                                    gameBoard[select_piéce[0]][select_piéce[1]][2] = 0
                                else:
                                    gameBoard[select_piéce[0]][select_piéce[1]][2] += 1
                                action -= 1
                                if etat_son == True:
                                    deplacement.play()
                                select_piéce = [-1, -1]
                                msg_a_envoyer = repr(gameBoard)
                                msg_a_envoyer = msg_a_envoyer.encode()
                                connexion_avec_serveur.send(msg_a_envoyer)
                                multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                            elif x >= 8 * 65 + 600 and x <= 8 * 65 + 665 and y >= 8 * 65 + 125 and y <= 8 * 65 + 200:
                                if gameBoard[select_piéce[0]][select_piéce[1]][2] == 0:
                                    gameBoard[select_piéce[0]][select_piéce[1]][2] = 3
                                else:
                                    gameBoard[select_piéce[0]][select_piéce[1]][2] -= 1
                                action -= 1
                                if etat_son == True:
                                    deplacement.play()
                                select_piéce = [-1, -1]
                                msg_a_envoyer = repr(gameBoard)
                                msg_a_envoyer = msg_a_envoyer.encode()
                                connexion_avec_serveur.send(msg_a_envoyer)
                                multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                    if x >= 890 and x <= 1075 and y >= 665 and y <= 710 and action == 0:
                        msg_a_envoyer = "laser"
                        msg_a_envoyer = msg_a_envoyer.encode()
                        connexion_avec_serveur.send(msg_a_envoyer)
                        if etat_son == 1:
                            laser.play()
                        select_piéce = [-1, -1]
                        multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                        direction = A_laser(Surface, gameBoard, gameBoard_coordonnée, T_joueur, choice, need_rotat= False)
                        action = 1
                        if T_joueur == 1:
                            T_joueur = 2
                        else:
                            T_joueur = 1
                        if gameBoard[direction[0]][direction[1]][1] == 1 and direction != [-1, -1]:
                            connexion_avec_client.close()
                            connexion_principale.close()
                            gameBoard[direction[0]][direction[1]][0] = 0
                            gameBoard[direction[0]][direction[1]][1] = 0
                            gameBoard[direction[0]][direction[1]][2] = 0
                            c_multi_local = False
                            win(Surface, T_joueur, choice)
                            c_win = True
                        else:
                            multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                        if direction != [-1, -1]:
                            gameBoard[direction[0]][direction[1]][0] = 0
                            gameBoard[direction[0]][direction[1]][1] = 0
                            gameBoard[direction[0]][direction[1]][2] = 0
                            if etat_son == True:
                                destruction.play()
                            if c_multi_local == True:
                                multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                        etat = 1
                        compt = 0

                if event.type == MOUSEBUTTONDOWN and event.button == 3:
                    select_piéce = [-1, -1]
                    multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)


        elif c_multi == True:
            if var1 == 1:
                musique = 2
                music(musique,etat_son)
                var1 = 2

            if etat_alea == 1:
                T_joueur = randint(1, 2)
                etat_alea = 0


            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if action != 0:
                    for i in range(10):
                        for j in range(8):
                            if x >= gameBoard_coordonnée[i][j][0] and x <= gameBoard_coordonnée[i][j][0] + 65 and y >= gameBoard_coordonnée[i][j][1] and y <= gameBoard_coordonnée[i][j][1] + 65:
                                if T_joueur == gameBoard[i][j][0]:
                                    if gameBoard[select_piéce[0]][select_piéce[1]][1] == 2:
                                        if gameBoard[i][j][1] == 3 or gameBoard[i][j][1] == 4:
                                            pass
                                        else:
                                            select_piéce = [i, j]
                                            multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                                    else:
                                        select_piéce = [i, j]
                                        multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)

                    if gameBoard[select_piéce[0]][select_piéce[1]][1] != 5:
                        for i in range(3):
                            for j in range(3):
                                if select_piéce[0] - 1 + i < 0 or select_piéce[1] - 1 + j < 0 or select_piéce[0] - 1 + i > 9 or select_piéce[1] - 1 + j > 7 :
                                    pass
                                elif x >= gameBoard_coordonnée[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0] and x <= gameBoard_coordonnée[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0] + 65 and y >= gameBoard_coordonnée[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] and y <= gameBoard_coordonnée[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] + 65 and select_piéce != [-1, -1]:
                                    if i == 1 and j == 1:
                                        None
                                    if gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 1 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 2 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 3 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 4 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 5:
                                        None
                                    else:
                                        if select_piéce[0] - 1 + i >= 0 or select_piéce[1] - 1 + j >= 0:
                                            gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0] = gameBoard[select_piéce[0]][select_piéce[1]][0]
                                            gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] = gameBoard[select_piéce[0]][select_piéce[1]][1]
                                            gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][2] = gameBoard[select_piéce[0]][select_piéce[1]][2]
                                            gameBoard[select_piéce[0]][select_piéce[1]][0] = 0
                                            gameBoard[select_piéce[0]][select_piéce[1]][1] = 0
                                            gameBoard[select_piéce[0]][select_piéce[1]][2] = 0
                                            select_piéce = [-1, -1]
                                            action -= 1
                                            if etat_son == True:
                                                deplacement.play()
                                            multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                                    if gameBoard[select_piéce[0]][select_piéce[1]][1] == 2:
                                        if gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 1 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 2 or gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1] == 5:
                                            None
                                        else:
                                            gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0],gameBoard[select_piéce[0]][select_piéce[1]][0] = gameBoard[select_piéce[0]][select_piéce[1]][0],gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][0]
                                            gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1],gameBoard[select_piéce[0]][select_piéce[1]][1] = gameBoard[select_piéce[0]][select_piéce[1]][1],gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][1]
                                            gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][2],gameBoard[select_piéce[0]][select_piéce[1]][2] = gameBoard[select_piéce[0]][select_piéce[1]][2],gameBoard[select_piéce[0] - 1 + i][select_piéce[1] - 1 + j][2]
                                            select_piéce = [-1, -1]
                                            action -= 1
                                            if etat_son == True:
                                                deplacement.play()
                                            multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)



                    if select_piéce != [-1, -1]:
                        if x >= 65 + 600 and x <= 65 + 665 and y >= 8 * 65 + 125 and y <= 8 * 65 + 200:
                            if gameBoard[select_piéce[0]][select_piéce[1]][2] == 3:
                                gameBoard[select_piéce[0]][select_piéce[1]][2] = 0
                            else:
                                gameBoard[select_piéce[0]][select_piéce[1]][2] += 1
                            action -= 1
                            if etat_son == True:
                                deplacement.play()
                            select_piéce = [-1, -1]
                            multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                        elif x >= 8 * 65 + 600 and x <= 8 * 65 + 665 and y >= 8 * 65 + 125 and y <= 8 * 65 + 200:
                            if gameBoard[select_piéce[0]][select_piéce[1]][2] == 0:
                                gameBoard[select_piéce[0]][select_piéce[1]][2] = 3
                            else:
                                gameBoard[select_piéce[0]][select_piéce[1]][2] -= 1
                            action -= 1
                            if etat_son == True:
                                deplacement.play()
                            select_piéce = [-1, -1]
                            multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                if x >= 890 and x <= 1075 and y >= 665 and y <= 710 and action == 0:
                    if etat_son == 1:
                        laser.play()
                    select_piéce = [-1, -1]
                    multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                    direction = A_laser(Surface, gameBoard, gameBoard_coordonnée, T_joueur, choice, need_rotat= False)
                    action = 1
                    if T_joueur == 1:
                        T_joueur = 2
                    else:
                        T_joueur = 1
                    if gameBoard[direction[0]][direction[1]][1] == 1 and direction != [-1, -1]:
                        if T_joueur == 1:
                            T_joueur = 2
                        else:
                            T_joueur = 1

                        gameBoard[direction[0]][direction[1]][0] = 0
                        gameBoard[direction[0]][direction[1]][1] = 0
                        gameBoard[direction[0]][direction[1]][2] = 0
                        c_multi = False
                        c_win = True
                    else:
                        multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
                    if direction != [-1, -1]:
                        gameBoard[direction[0]][direction[1]][0] = 0
                        gameBoard[direction[0]][direction[1]][1] = 0
                        gameBoard[direction[0]][direction[1]][2] = 0
                        if etat_son == True:
                            destruction.play()
                        if c_multi == True:
                            multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                select_piéce = [-1, -1]
                multi(Surface, gameBoard, T_joueur, select, select_piéce, choice)


        elif c_win == True :
            win(Surface, T_joueur, choice)
            if event.type == QUIT:
                game = 0
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                win(Surface, T_joueur, choice)
                x, y = event.pos
                if 50 < x < 130 and 650 < y < 685:
                    c_win = False
                    if etat_menu == 1:
                        c_menu_solo = True
                        menuSolo(Surface, choice, choice_map, difficulty, T_joueur)
                    if etat_menu == 2:
                        c_menu_multi = True
                        menuMulti(Surface, choice, choice_map, difficulty, T_joueur)
                elif 610 < x < 704 and 650 < y < 685:
                    c_win = False
                    c_menu = True
                    menu(Surface, 0, choice, etat_son)
                elif 1100 < x < 1210 and 650 <y < 685:
                    game = 0

    pygame.display.update()
    fpsClock.tick(fps)

pygame.quit()