import pygame, sys
from Piéces import *
from Laser import *
from pygame.locals import *


def menulogo(Surface, choice):
    font = pygame.font.Font(None, 30)
    Menu = font.render("Menu", 1, (255, 255, 255))
    Fmenu_Selection_Neutre = pygame.image.load('sprites/pack' + str(choice) + '/imgs/neutre.png')
    Fmenu_Selection_Neutre = pygame.transform.scale(Fmenu_Selection_Neutre, (350, 65))
    Surface.blit(Fmenu_Selection_Neutre,(1050, -10))
    Surface.blit(Menu,(1199, 16))


def menupause(Surface, choice):
    font = pygame.font.SysFont("Calibri", 40)
    T1 = font.render("Reprendre", 1, (255, 255, 255))
    T2 = font.render("Recommencer", 1, (255, 255, 255))
    T3 = font.render("Sauvegarder", 1, (255, 255, 255))
    T4 = font.render("Quitter", 1, (255, 255, 255))
    Fmenu_Selection_Neutre = pygame.image.load('sprites/pack' + str(choice) + '/imgs/neutre.png')
    Fpause = pygame.image.load('sprites/pack' + str(choice) + '/imgs/pause.png')
    Surface.blit(Fpause, (0, 0))
    for i in range(4):
        Surface.blit(Fmenu_Selection_Neutre, (0, 35 + i * 125))
    Surface.blit(T1, (555, 125 + 0 * 125))
    Surface.blit(T2, (525, 127 + 1 * 125))
    Surface.blit(T3, (535, 127 + 2 * 125))
    Surface.blit(T4, (580, 127 + 3 * 125))


def sauvegarder(Surface,choice,mode):
    font = pygame.font.SysFont("Calibri", 35)
    Fmenu_Selection_Neutre = pygame.image.load('sprites/pack' + str(choice) + '/imgs/neutre.png')
    Fpause = pygame.image.load('sprites/pack' + str(choice) + '/imgs/pause.png')
    retour = font.render("Retour", 1, (255, 255, 255))
    Surface.blit(Fpause, (0, 0))
    if mode == 1:
        for i in range(3):
            Surface.blit(Fmenu_Selection_Neutre, (0, 50 + i * 100))
            look_save = open("save/solo/save" + str(i + 1) + ".txt", "r")
            look_saveb = look_save.read()
            if look_saveb == "":
                slot = font.render("Slot " + str(i + 1) + " Sauvegarde", 1, (255, 255, 255))
                Surface.blit(slot, (516, 142 + i * 100))
            else:
                slot = font.render("Partie " + str(i + 1), 1, (255, 0, 0))
                Surface.blit(slot, (590, 142 + i * 100))
    else:
        for i in range(3):
            Surface.blit(Fmenu_Selection_Neutre, (0, 50 + i * 100))
            look_save = open("save/multi/save" + str(i + 1) + ".txt", "r")
            look_saveb = look_save.read()
            if look_saveb == "":
                slot = font.render("Slot " + str(i + 1) + " Sauvegarde", 1, (255, 255, 255))
                Surface.blit(slot, (516, 142 + i * 100))
            else:
                slot = font.render("Partie " + str(i + 1), 1, (255, 0, 0))
                Surface.blit(slot, (590, 142 + i * 100))

    Surface.blit(Fmenu_Selection_Neutre, (0, 450))
    Surface.blit(retour, (590, 545))


def menu(screen,select, choice, etat_son):
    scrrec = screen.get_rect()
    font = pygame.font.SysFont("Calibri", 35)
    Fmenu_original = pygame.image.load('sprites/pack' + str(choice) +'/imgs/bg_menu.jpg').convert()
    Fmenu_Selection_Neutre = pygame.image.load('sprites/pack' + str(choice) +'/imgs/neutre.png')
    Fmenu_Selection_select = pygame.image.load('sprites/pack' + str(choice) +'/imgs/select.png')
    Fmenu = Fmenu_original
    Fmenu = pygame.transform.scale(Fmenu, (scrrec.right, scrrec.bottom))
    Solo = font.render("Solo", 1, (255, 255, 255))
    Multijoueur = font.render("Multijoueur", 1, (255, 255, 255))
    Editeur = font.render("Editeur", 1, (255, 255, 255))
    Themes = font.render("Thèmes", 1, (255, 255, 255))
    Quitter = font.render("Quitter", 1, (255, 255, 255))
    screen.blit(Fmenu, (0, 0))
    for y in range(5):
        if select == y:
            screen.blit(Fmenu_Selection_select, (0, (y + 1) * 100 - 20))
        else:
            screen.blit(Fmenu_Selection_Neutre, (0, y * 100 + 45))
    screen.blit(Solo, (608, 142))
    screen.blit(Multijoueur, (560, 240))
    screen.blit(Editeur, (590, 340))
    screen.blit(Themes, (587, 440))
    screen.blit(Quitter, (585, 540))

    mute = pygame.image.load('sprites/commun/mute.png')
    son = pygame.image.load('sprites/commun/son.png')
    info = pygame.image.load('sprites/commun/info.png')
    book = pygame.image.load('sprites/commun/book.png')
    mute = pygame.transform.scale(mute, (25, 25))
    son = pygame.transform.scale(son, (25, 25))
    info = pygame.transform.scale(info, (45, 45))
    book = pygame.transform.scale(book, (30, 30))
    if etat_son == 1:
        screen.blit(son, (5, 5))
    else:
        screen.blit(mute, (5, 5))
    screen.blit(info, (40, -5))
    screen.blit(book, (100, 5))


def menuSolo(Surface, choice, choice_map,difficulty,choice_tour):
    scrrec = Surface.get_rect()
    font = pygame.font.SysFont("Calibri", 35)
    font2 = pygame.font.SysFont("Calibri", 45)
    Fmenu = pygame.image.load('sprites/pack' + str(choice) + '/imgs/bg_menuSolo.jpg').convert()
    carte = pygame.image.load('map/map'+str(choice_map)+'.png')
    neutre = pygame.image.load('sprites/pack' + str(choice) + '/imgs/neutre.png')
    previous = pygame.image.load('sprites/pack' + str(choice) + '/imgs/previous.png')
    next = pygame.image.load('sprites/pack' + str(choice) + '/imgs/next.png')
    vert = (0, 255, 0)
    blanc = (255, 255, 255)
    rouge = (255, 0, 0)
    gris = (150, 150, 150)
    l1, l2, l3, t1, t2, t3 = rouge, gris, gris, blanc, blanc, blanc

    level = font2.render('Difficulté', 1, blanc)
    order = font2.render('Premier tour', 1, blanc)

    if choice_tour == 1:
        t1 = rouge
    elif choice_tour == 2:
        t2 = rouge
    elif choice_tour == 3:
        t3 = rouge

    map1 = font.render("Classique", 1, vert)
    map2 = font.render("Dynastie", 1, vert)
    map3 = font.render("Imhotep", 1, vert)
    map4 = font.render("Editée", 1, vert)
    map5 = font.render("Aléatoire", 1, vert)

    level1 = font.render("Facile", 1, l1)
    level2 = font.render("Normal", 1, l2)
    level3 = font.render("Difficile", 1, l3)


    tour1 = font.render("Humain", 1, t1)
    tour2 = font.render("Ordinateur", 1, t2)
    tour3 = font.render("Aléatoire", 1, t3)


    Lancer = font.render("Lancer", 1, blanc)
    Charger = font.render("Charger", 1, blanc)
    Retour = font.render("Retour", 1, blanc)


    neutre = pygame.transform.scale(neutre,(800, 125))
    Fmenu = pygame.transform.scale(Fmenu, (scrrec.right, scrrec.bottom))
    Surface.blit(Fmenu, (0, 0))

    if choice_map == 1:
        Surface.blit(map1, (320, 355))
    elif choice_map == 2:
        Surface.blit(map2, (320, 355))
    elif choice_map == 3:
        Surface.blit(map3, (320, 355))
    elif choice_map == 4:
        Surface.blit(map4, (320, 355))
    elif choice_map == 5:
        Surface.blit(map5, (320, 355))

    Surface.blit(level, (320, 70))
    Surface.blit(level1, (320, 140))
    Surface.blit(level2, (520, 140))
    Surface.blit(level3, (720, 140))

    pygame.draw.line(Surface, gris, (515, 158), (630,158), 2)
    pygame.draw.line(Surface, gris, (715, 158), (830,158), 2)

    Surface.blit(order, (320,220))
    Surface.blit(tour1, (320, 290))
    Surface.blit(tour2, (520, 290))
    Surface.blit(tour3, (770, 290))

    Surface.blit(previous, (350, 450))
    Surface.blit(carte, (480, 350))
    Surface.blit(next, (875, 450))

    for i in range(3):
        Surface.blit(neutre, (i*540 - 300, 615))

    Surface.blit(Retour,(55,665))
    Surface.blit(Charger, (582, 665))
    Surface.blit(Lancer, (1135, 665))
    pygame.display.flip()


def menuMulti(Surface, choice, choice_map,difficulty,choice_tour):
    scrrec = Surface.get_rect()
    font = pygame.font.SysFont("Calibri", 35)
    font2 = pygame.font.SysFont("Calibri", 45)
    Fmenu = pygame.image.load('sprites/pack' + str(choice) + '/imgs/bg_menuSolo.jpg').convert()
    carte = pygame.image.load('map/map' + str(choice_map) + '.png')
    neutre = pygame.image.load('sprites/pack' + str(choice) + '/imgs/neutre.png')
    previous = pygame.image.load('sprites/pack' + str(choice) + '/imgs/previous.png')
    next = pygame.image.load('sprites/pack' + str(choice) + '/imgs/next.png')
    blanc = (255, 255, 255)
    rouge = (255, 0, 0)
    vert = (0, 255, 0)
    l1, l2, l3, t1, t2, t3 = blanc, blanc, blanc, blanc, blanc, blanc

    level = font2.render('Type', 1, blanc)
    order = font2.render('Premier tour', 1, blanc)

    if difficulty == 1:
        l1 = rouge
    elif difficulty == 2:
        l2 = rouge
    elif difficulty == 3:
        l3 = rouge

    if choice_tour == 1:
        t1 = rouge
    elif choice_tour == 2:
        t2 = rouge
    elif choice_tour == 3:
        t3 = rouge

    level1 = font.render("Ordinateur", 1, l1)
    level2 = font.render("Héberger", 1, l2)
    level3 = font.render("Rejoindre", 1, l3)

    map1 = font.render("Classique", 1, vert)
    map2 = font.render("Dynastie", 1, vert)
    map3 = font.render("Imhotep", 1, vert)
    map4 = font.render("Editée", 1, vert)
    map5 = font.render("Aléatoire", 1, vert)

    tour1 = font.render("Joueur 1", 1, t1)
    tour2 = font.render("Joueur 2", 1, t2)
    tour3 = font.render("Aléatoire", 1, t3)

    Lancer = font.render("Lancer", 1, blanc)
    Charger = font.render("Charger", 1, blanc)
    Retour = font.render("Retour", 1, blanc)

    neutre = pygame.transform.scale(neutre, (800, 125))
    Fmenu = pygame.transform.scale(Fmenu, (scrrec.right, scrrec.bottom))
    Surface.blit(Fmenu, (0, 0))

    Surface.blit(level, (320, 70))
    Surface.blit(level1, (320, 140))
    Surface.blit(level2, (520, 140))
    Surface.blit(level3, (720, 140))

    if difficulty != 3:
        Surface.blit(order, (320, 220))
        Surface.blit(tour1, (320, 290))
        Surface.blit(tour2, (520, 290))
        Surface.blit(tour3, (770, 290))

        Surface.blit(previous, (350, 450))
        Surface.blit(carte, (480, 350))
        Surface.blit(next, (875, 450))

        if choice_map == 1:
            Surface.blit(map1, (320, 355))
        elif choice_map == 2:
            Surface.blit(map2, (320, 355))
        elif choice_map == 3:
            Surface.blit(map3, (320, 355))
        elif choice_map == 4:
            Surface.blit(map4, (320, 355))
        elif choice_map == 5:
            Surface.blit(map5, (320, 355))

    for i in range(3):
        Surface.blit(neutre, (i*540 - 300, 615))

    Surface.blit(Retour,(55,665))
    Surface.blit(Charger, (582, 665))
    Surface.blit(Lancer, (1135, 665))
    pygame.display.flip()


def themes(Surface, choice):
    scrrec = Surface.get_rect()
    Fmenu = pygame.image.load('sprites/pack' + str(choice) + '/imgs/bg_menu.jpg').convert()
    back = pygame.image.load('sprites/pack' + str(choice) + '/imgs/quit.png')
    Fmenu = pygame.transform.scale(Fmenu, (scrrec.right, scrrec.bottom))
    Surface.blit(Fmenu, (0, 0))
    Surface.blit(back, (10, 10))
    pack1 = pygame.image.load('sprites/pack1/imgs/bg_menuSolo.jpg')
    pack2 = pygame.image.load('sprites/pack2/imgs/bg_jeu.jpg')
    pack3 = pygame.image.load('sprites/pack3/imgs/bg_jeu.jpg')
    pack4 = pygame.image.load('sprites/pack4/imgs/bg_jeu.jpg')
    pack1 = pygame.transform.scale(pack1, (520, 300))
    pack2 = pygame.transform.scale(pack2, (520, 300))
    pack3 = pygame.transform.scale(pack3, (520, 300))
    pack4 = pygame.transform.scale(pack4, (520, 300))
    pack = [pack1, pack2, pack3, pack4]
    cpt = 0
    blanc = (255, 255, 255)
    rouge = (255, 0, 0)
    for line in range(2):
        for col in range(2):
            if cpt == choice - 1:
                color = rouge
            else:
                color = blanc
            pygame.draw.rect(Surface, color, (70 + col * 600, 30 + line * 340, 540, 320))
            Surface.blit(pack[cpt], (80 + col * 600, 40 + line * 340))
            cpt += 1


def solo(Surface,gameBoard,T_joueur,select,select_piéce, choice):
    info = pygame.display.Info()
    scrrec = Surface.get_rect()
    Fmenu_original = pygame.image.load('sprites/pack' + str(choice) + '/imgs/bg_jeu.jpg').convert()
    playing = pygame.image.load('sprites/pack' + str(choice) + '/imgs/select_player.png')
    playing = pygame.transform.scale(playing, (40, 40))
    Fmenu = Fmenu_original
    Fmenu = pygame.transform.scale(Fmenu, (scrrec.right, scrrec.bottom))
    Surface.blit(Fmenu, (0, 0))
    font = pygame.font.Font(None, 45)

    Fire = font.render("Tirer", 1, (255, 255, 255))

    Case_neutre = pygame.image.load('sprites/pack' + str(choice) + '/imgs/case_neutre.png')
    Case_possible = pygame.image.load('sprites/pack' + str(choice) + '/imgs/case_possible.png')
    Case_baton = pygame.image.load('sprites/pack' + str(choice) + '/imgs/case_baton.png')
    Case_oeil = pygame.image.load('sprites/pack' + str(choice) + '/imgs/case_oeil.png')
    Case_neutre = pygame.transform.scale(Case_neutre, (65, 65))
    Case_possible = pygame.transform.scale(Case_possible, (65, 65))
    Case_baton = pygame.transform.scale(Case_baton, (65, 65))
    Case_oeil = pygame.transform.scale(Case_oeil, (65, 65))
    Rot_d = pygame.image.load('sprites/pack' + str(choice) + '/imgs/rot_d.png')
    Rot_g = pygame.image.load('sprites/pack' + str(choice) + '/imgs/rot_g.png')
    Rot_d = pygame.transform.scale(Rot_d, (65, 65))
    Rot_g = pygame.transform.scale(Rot_g, (65, 65))
    Parchemin = pygame.image.load('sprites/pack' + str(choice) + '/imgs/parchemin.png')
    Parchemin = pygame.transform.scale(Parchemin, (300, 100))

    for i in range(2):
        Surface.blit(Parchemin,(300,190+i*289))
    if choice == 1:
        J1 = font.render("Joueur 1", 1, (255, 0, 0))
        J2 = font.render("Ordinateur", 1, (255, 255, 255))
        if T_joueur == 1:
            Surface.blit(playing, (315, 219))
        else:
            Surface.blit(playing, (315, 509))
    else:
        J1 = font.render("Joueur 1", 1, (255, 0, 0))
        J2 = font.render("Ordinateur", 1, (193, 45, 190))
        if T_joueur == 1:
            Surface.blit(playing, (315, 219))
        else:
            Surface.blit(playing, (315, 509))

    Parchemin2 = pygame.transform.scale(Parchemin, (300, 85))
    Surface.blit(Parchemin2, (775, 635))
    Surface.blit(Fire, (890, 665))
    Surface.blit(J1, (380, 228))
    Surface.blit(J2, (380, 517))

    for x in range(10):
        for y in range(8):
            if x == 0:
                Surface.blit(Case_oeil, (x * 65 + 600, y * 65 + 125))
            elif x == 9:
                Surface.blit(Case_baton, (x * 65 + 600, y * 65 + 125))
            elif x == 1 and y == 0:
                Surface.blit(Case_baton, (x * 65 + 600, y * 65 + 125))
            elif x == 1 and y == 7:
                Surface.blit(Case_baton, (x * 65 + 600, y * 65 + 125))
            elif x == 8 and y == 0:
                Surface.blit(Case_oeil, (x * 65 + 600, y * 65 + 125))
            elif x == 8 and y == 7:
                Surface.blit(Case_oeil, (x * 65 + 600, y * 65 + 125))
            else:
                Surface.blit(Case_neutre, (x * 65 + 600, y * 65 + 125))

    if select_piéce[0] != -1:
        Surface.blit(Rot_d, (1 * 65 + 600, 8 * 65 + 125))
        Surface.blit(Rot_g, (8 * 65 + 600, 8 * 65 + 125))
        for x in range(3):
            for y in range(3):
                if select_piéce[0] - 1 + x < 0 or select_piéce[1] - 1 + y < 0 or select_piéce[0] - 1 + x > 9 or select_piéce[1] - 1 + y > 7 or gameBoard[select_piéce[0]][select_piéce[1]][1] == 5:
                    pass
                elif gameBoard[select_piéce[0] - 1 + x][select_piéce[1] - 1 + y][1] == 0:
                    Surface.blit(Case_possible,((select_piéce[0] - 1 + x) * 65 + 600, (select_piéce[1] - 1 + y) * 65 + 125))
                if gameBoard[select_piéce[0]][select_piéce[1]][1] == 2:
                    if gameBoard[select_piéce[0] - 1 + x][select_piéce[1] - 1 + y][1] == 3 or gameBoard[select_piéce[0] - 1 + x][select_piéce[1] - 1 + y][1] == 4:
                        Surface.blit(Case_possible,((select_piéce[0] - 1 + x) * 65 + 600, (select_piéce[1] - 1 + y) * 65 + 125))

    for x in range(10):
        for y in range(8):
            if gameBoard[x][y][1] == 1:
                Surface.blit(Pharaoh(gameBoard[x][y][2], gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))
            elif gameBoard[x][y][1] == 2:
                Surface.blit(scarab(gameBoard[x][y][2], gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))
            elif gameBoard[x][y][1] == 3:
                Surface.blit(anubis(gameBoard[x][y][2], gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))
            elif gameBoard[x][y][1] == 4:
                Surface.blit(pyramid(gameBoard[x][y][2], gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))
            elif gameBoard[x][y][1] == 5:
                Surface.blit(sphinh(gameBoard[x][y][2], gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))
    menulogo(Surface, choice)


def Chargersolo(Surface,choice):
    font = pygame.font.SysFont("Calibri", 36)
    Fmenu_Selection_Neutre = pygame.image.load('sprites/pack' + str(choice) + '/imgs/neutre.png')
    Supp = pygame.image.load('sprites/pack2/imgs/case_possible.png')
    Supp = pygame.transform.scale(Supp, (65, 65))
    Fpause = pygame.image.load('sprites/pack' + str(choice) + '/imgs/pause.png')
    retour = font.render("Retour", 1, (255, 255, 255))
    Surface.blit(Fpause, (0, 0))
    Surface.blit(Fmenu_Selection_Neutre, (0, 450))
    Surface.blit(retour,(590,545))
    for i in range(3):
        Surface.blit(Fmenu_Selection_Neutre,(0,50 + i * 100))
        look_save = open("save/solo/save" + str(i+1) + ".txt", "r")
        look_saveb = look_save.read()
        if look_saveb == "":
            slot = font.render("Slot " + str(i+1) + " Vide", 1, (255, 255, 255))
            Surface.blit(slot, (565, 142 + i * 100))
        else:
            slot = font.render("Partie " + str(i + 1), 1, (255, 0, 0))
            Surface.blit(slot, (584, 142 + i * 100))
            Surface.blit(Supp, (425, 125 + i * 100))


def menu_hebergement(Surface,choice,etatserveur,client):
    font = pygame.font.Font(None, 45)
    scrrec = Surface.get_rect()
    address_ip = font.render("Adresse IP", 1, (255, 255, 255))
    retour = font.render("Retour", 1, (255, 255, 255))
    statut = font.render("Statut :", 1, (255, 255, 255))
    if etatserveur == 0:
        statut2 = font.render("Serveur Inactif", 1, (255, 0, 0))
    else:
        statut2 = font.render("Serveur Actif", 1, (0, 255, 0))
    if client == 0:
        statut3 = font.render("Joueur non trouvé", 1, (255, 0, 0))
    elif client == 2:
        statut3 = font.render("En attente de joueur", 1, (255, 0, 0))
    else:
        statut3 = font.render("Joueur trouvé", 1, (0, 255, 0))
    if etatserveur == 1 and client == 3:
        demarrer = font.render("Démarrer", 1, (0, 255, 0))
    else:
        demarrer = font.render("Démarrer", 1, (255, 0, 0))

    enter = font.render("Entrer", 1, (255, 255, 255))
    Fond_image = pygame.image.load('sprites/pack' + str(choice) + '/imgs/bg_menuSolo.jpg').convert()
    neutre = pygame.image.load('sprites/pack' + str(choice) + '/imgs/neutre.png')
    Fond_saisie = pygame.image.load('sprites/commun/Saisie.png')
    Fond_saisie = pygame.transform.scale(Fond_saisie, (550, 65))
    Fond_convert = pygame.transform.scale(Fond_image, (scrrec.right, scrrec.bottom))
    Surface.blit(Fond_convert, (0, 0))
    neutre = pygame.transform.scale(neutre, (800, 125))
    for i in range(2):
        Surface.blit(neutre, (i * 540, 605))
    Surface.blit(neutre, (250, 300))
    Surface.blit(enter, (605, 352))
    Surface.blit(statut, (400, 450))
    Surface.blit(statut2, (525, 450))
    Surface.blit(statut3, (525, 500))
    Surface.blit(retour, (350, 660))
    Surface.blit(demarrer, (870, 660))


def menu_rejoindre(Surface,choice,etatserveur,ip):
    font = pygame.font.Font(None,45)
    scrrec = Surface.get_rect()
    address_ip = font.render("Adresse IP", 1, (255, 255, 255))
    retour = font.render("Retour", 1, (255, 255, 255))
    statut = font.render("Statut :", 1, (255, 255, 255))
    ip_affiche = font.render(ip,1,(0,0,0))
    if etatserveur == 0:
        statut2 = font.render("Aucun serveur trouvé ", 1, (255, 0, 0))
    else:
        statut2 = font.render("Serveur trouvé", 1, (0, 255, 0))

    enter = font.render("Entrer", 1, (255, 255, 255))
    Fond_image = pygame.image.load('sprites/pack' + str(choice) + '/imgs/bg_menuSolo.jpg').convert()
    neutre = pygame.image.load('sprites/pack' + str(choice) + '/imgs/neutre.png')
    Fond_saisie = pygame.image.load('sprites/commun/Saisie.png')
    Fond_saisie = pygame.transform.scale(Fond_saisie, (550,65))
    Fond_convert = pygame.transform.scale(Fond_image, (scrrec.right, scrrec.bottom))
    Surface.blit(Fond_convert, (0,0))
    Surface.blit(Fond_saisie, (375,250))
    neutre = pygame.transform.scale(neutre, (800, 125))
    Surface.blit(address_ip,(570,175))

    Surface.blit(neutre,(0 , 605))
    Surface.blit(ip_affiche, (425,270))
    Surface.blit(neutre, (250, 300))
    Surface.blit(enter, (610,350))
    Surface.blit(statut, (400,450))
    Surface.blit(statut2, (525,450))
    Surface.blit(retour,(350,660))


def Chargermulti(Surface,choice):
    font = pygame.font.SysFont("Calibri", 36)
    Fmenu_Selection_Neutre = pygame.image.load('sprites/pack' + str(choice) + '/imgs/neutre.png')
    Supp = pygame.image.load('sprites/pack2/imgs/case_possible.png')
    Supp = pygame.transform.scale(Supp, (65, 65))
    Fpause = pygame.image.load('sprites/pack' + str(choice) + '/imgs/pause.png')
    retour = font.render("Retour", 1, (255, 255, 255))
    Surface.blit(Fpause, (0, 0))
    Surface.blit(Fmenu_Selection_Neutre, (0, 450))
    Surface.blit(retour,(590,545))
    for i in range(3):
        Surface.blit(Fmenu_Selection_Neutre,(0,50 + i * 100))
        look_save = open("save/multi/save" + str(i+1) + ".txt", "r")
        look_saveb = look_save.read()
        if look_saveb == "":
            slot = font.render("Slot " + str(i+1) + " Vide", 1, (255, 255, 255))
            Surface.blit(slot, (565, 142 + i * 100))
        else:
            slot = font.render("Partie " + str(i + 1), 1, (255, 0, 0))
            Surface.blit(slot, (584, 142 + i * 100))
            Surface.blit(Supp, (425, 125 + i * 100))


def multi(Surface,gameBoard,T_joueur,select,select_piéce, choice):
    scrrec = Surface.get_rect()
    Fmenu_original = pygame.image.load('sprites/pack' + str(choice) + '/imgs/bg_jeu.jpg').convert()
    playing = pygame.image.load('sprites/pack' + str(choice) + '/imgs/select_player.png')
    playing = pygame.transform.scale(playing, (40, 40))
    Fmenu = Fmenu_original
    Fmenu = pygame.transform.scale(Fmenu, (scrrec.right, scrrec.bottom))
    Surface.blit(Fmenu, (0, 0))
    font = pygame.font.Font(None, 45)

    Fire = font.render("Tirer", 1, (255, 255, 255))
    Case_neutre = pygame.image.load('sprites/pack' + str(choice) + '/imgs/case_neutre.png')
    Case_possible = pygame.image.load('sprites/pack' + str(choice) + '/imgs/case_possible.png')
    Case_baton = pygame.image.load('sprites/pack' + str(choice) + '/imgs/case_baton.png')
    Case_oeil = pygame.image.load('sprites/pack' + str(choice) + '/imgs/case_oeil.png')
    Case_neutre = pygame.transform.scale(Case_neutre, (65, 65))
    Case_possible = pygame.transform.scale(Case_possible,(65, 65))
    Case_baton = pygame.transform.scale(Case_baton, (65, 65))
    Case_oeil = pygame.transform.scale(Case_oeil, (65, 65))
    Rot_d = pygame.image.load('sprites/pack' + str(choice) + '/imgs/rot_d.png')
    Rot_g = pygame.image.load('sprites/pack' + str(choice) + '/imgs/rot_g.png')
    Rot_d = pygame.transform.scale(Rot_d, (65, 65))
    Rot_g = pygame.transform.scale(Rot_g, (65, 65))
    Parchemin = pygame.image.load('sprites/pack' + str(choice) + '/imgs/parchemin.png')
    Parchemin = pygame.transform.scale(Parchemin, (300, 100))

    for i in range(2):
        Surface.blit(Parchemin,(300,190+i*289))
    if choice == 1:
        J1 = font.render("Joueur 1", 1, (255, 0, 0))
        J2 = font.render("Joueur 2", 1, (255, 255, 255))
        if T_joueur == 1:
            Surface.blit(playing, (315, 219))
        else:
            Surface.blit(playing, (315, 509))
    else:
        J1 = font.render("Joueur 1", 1, (255, 0, 0))
        J2 = font.render("Joueur 2", 1, (193, 45, 190))
        if T_joueur == 1:
            Surface.blit(playing, (315, 219))
        else:
            Surface.blit(playing, (315, 509))

    Parchemin2 = pygame.transform.scale(Parchemin, (300, 85))
    Surface.blit(Parchemin2, (775, 635))
    Surface.blit(Fire, (890, 665))
    Surface.blit(J1, (380, 228))
    Surface.blit(J2, (380, 517))

    for x in range(10):
        for y in range(8):
            if x == 0 :
                Surface.blit(Case_oeil, (x * 65 + 600, y * 65 + 125))
            elif x == 9 :
                Surface.blit(Case_baton, (x * 65 + 600, y * 65 + 125))
            elif x == 1 and y == 0:
                Surface.blit(Case_baton, (x * 65 + 600, y * 65 + 125))
            elif x == 1 and y == 7:
                Surface.blit(Case_baton, (x * 65 + 600, y * 65 + 125))
            elif x == 8 and y == 0:
                Surface.blit(Case_oeil, (x * 65 + 600, y * 65 + 125))
            elif x == 8 and y == 7:
                Surface.blit(Case_oeil, (x * 65 + 600, y * 65 + 125))
            else:
                Surface.blit(Case_neutre, (x * 65 + 600, y * 65 + 125))

    if select_piéce[0] != -1:
        Surface.blit(Rot_d,(1 * 65 + 600,8 * 65 + 125))
        Surface.blit(Rot_g, (8 * 65 + 600,8 * 65 + 125))
        for x in range(3):
            for y in range(3):
                if select_piéce[0] - 1 + x < 0 or select_piéce[1] - 1 + y < 0 or select_piéce[0] - 1 + x > 9 or select_piéce[1] - 1 + y > 7 or gameBoard[select_piéce[0]][select_piéce[1]][1] == 5:
                    pass
                elif gameBoard[select_piéce[0] - 1 + x][select_piéce[1] - 1 + y][1] == 0:
                    Surface.blit(Case_possible,((select_piéce[0] - 1 + x) * 65 + 600, (select_piéce[1] - 1 + y) * 65 + 125))
                elif gameBoard[select_piéce[0]][select_piéce[1]][1] == 2 and gameBoard[select_piéce[0] - 1 + x][select_piéce[1] - 1 + y][1] == 4:
                    Surface.blit(Case_possible,((select_piéce[0] - 1 + x) * 65 + 600, (select_piéce[1] - 1 + y) * 65 + 125))

    for x in range(10):
        for y in range(8):
            if gameBoard[x][y][1] == 1:
                Surface.blit(Pharaoh(gameBoard[x][y][2],gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))
            elif gameBoard[x][y][1] == 2:
                Surface.blit(scarab(gameBoard[x][y][2],gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))
            elif gameBoard[x][y][1] == 3:
                Surface.blit(anubis(gameBoard[x][y][2],gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))
            elif gameBoard[x][y][1] == 4:
                Surface.blit(pyramid(gameBoard[x][y][2],gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))
            elif gameBoard[x][y][1] == 5:
                Surface.blit(sphinh(gameBoard[x][y][2],gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))
    menulogo(Surface, choice)


def editeuraffiche(Surface,gameBoard,piece,couleur,select, choice, etat_sauvegarde, verif_editeur):
    font = pygame.font.Font(None,45)
    font2 = pygame.font.Font(None, 35)
    font3 = pygame.font.Font(None, 55)
    vert = (0, 255, 0)
    blanc = (255, 255, 255)
    rouge = (255, 0, 0)
    phara1 = verif_editeur[0]
    phara2 = verif_editeur[1]
    scar1 = verif_editeur[2]
    scar2 = verif_editeur[3]
    mir1 = verif_editeur[4]
    mir2 = verif_editeur[5]
    las1 = verif_editeur[6]
    las2 = verif_editeur[7]

    if etat_sauvegarde == 0:
        choix_couleur = rouge
    else:
        choix_couleur = vert
    reset = font.render("Réinitialiser",1,blanc)
    save = font.render("Sauvegarder", 1, choix_couleur)
    retour = font.render("Retour", 1, blanc)
    valider = font2.render("Valider", 1, blanc)

    scrrec = Surface.get_rect()
    Fmenu_original = pygame.image.load('sprites/pack' + str(choice) + '/imgs/bg_jeu.jpg').convert()
    Fmenu = Fmenu_original
    Fmenu = pygame.transform.scale(Fmenu, (scrrec.right, scrrec.bottom))
    Surface.blit(Fmenu, (0, 0))

    bouton_info = pygame.image.load('sprites/commun/info.png')
    bouton_info = pygame.transform.scale(bouton_info, (50, 50))
    Surface.blit(bouton_info, (1055, 655))


    Case_neutre = pygame.image.load('sprites/pack' + str(choice) + '/imgs/case_neutre.png')
    Case_baton = pygame.image.load('sprites/pack' + str(choice) + '/imgs/case_baton.png')
    Case_oeil = pygame.image.load('sprites/pack' + str(choice) + '/imgs/case_oeil.png')
    Parchemin = pygame.image.load('sprites/pack' + str(choice) + '/imgs/parchemin.png')
    Case_neutre = pygame.transform.scale(Case_neutre, (65, 65))
    Case_baton = pygame.transform.scale(Case_baton, (65, 65))
    Case_oeil = pygame.transform.scale(Case_oeil, (65, 65))
    Parchemin = pygame.transform.scale(Parchemin,(300,100))
    Parchemin2 = pygame.transform.scale(Parchemin, (200, 66))
    Verif = pygame.transform.scale(Parchemin, (150, 60))

    a = Pharaoh(0, 1, choice)
    b = Pharaoh(0, 2, choice)
    c = scarab(0, 1, choice)
    d = scarab(0, 2, choice)
    e = pyramid(0, 1, choice)
    f = pyramid(0, 2, choice)
    g = sphinh(0, 1, choice)
    h = sphinh(0, 2, choice)


    a = pygame.transform.scale(a, (40, 40))
    b = pygame.transform.scale(b, (40, 40))
    c = pygame.transform.scale(c, (40, 40))
    d = pygame.transform.scale(d, (40, 40))
    e = pygame.transform.scale(e, (40, 40))
    f = pygame.transform.scale(f, (40, 40))
    g = pygame.transform.scale(g, (40, 40))
    h = pygame.transform.scale(h, (40, 40))

    if phara1 == 1:
        p1 = font3.render(str(phara1), 1, vert)
    else:
        p1 = font3.render(str(phara1), 1, rouge)

    if phara2 == 1:
        p2 = font3.render(str(phara2), 1, vert)
    else:
        p2 = font3.render(str(phara2), 1, rouge)

    if scar1 > 0:
        s1 = font3.render(str(scar1), 1, vert)
    else:
        s1 = font3.render(str(scar1), 1, rouge)

    if scar2 > 0:
        s2 = font3.render(str(scar2), 1, vert)
    else:
        s2 = font3.render(str(scar2), 1, rouge)

    if mir1 > 0:
        m1 = font3.render(str(mir1), 1, vert)
    else:
        m1 = font3.render(str(mir1), 1, rouge)

    if mir2 > 0:
        m2 = font3.render(str(mir2), 1, vert)
    else:
        m2 = font3.render(str(mir2), 1, rouge)

    if las1 == 1:
        l1 = font3.render(str(las1), 1, vert)
    else:
        l1 = font3.render(str(las1), 1, rouge)

    if las2 == 1:
        l2 = font3.render(str(las2), 1, vert)
    else:
        l2 = font3.render(str(las2), 1, rouge)

    Surface.blit(Pharaoh(0,1, choice), (400, 150))
    Surface.blit(scarab(0,1, choice), (400, 250))
    Surface.blit(anubis(0,1, choice), (400, 350))
    Surface.blit(pyramid(0,1, choice), (400, 450))
    Surface.blit(sphinh(0,1, choice), (400, 550))
    Surface.blit(Pharaoh(0,2, choice), (480, 150))
    Surface.blit(scarab(0,2, choice), (480, 250))
    Surface.blit(anubis(0,2, choice), (480, 350))
    Surface.blit(pyramid(0,2, choice), (480, 450))
    Surface.blit(sphinh(0,2, choice), (480, 550))
    for i in range(3):
        Surface.blit(Parchemin,(10,150+i*150))
    for i in range(4):
        for j in range(2):
            Surface.blit(Verif, (600 + i * 167, 3 + j * 62))
    pygame.draw.rect(Surface, (255,215,0), [320+80*couleur, piece*100+150, 65, 70], 5)
    Surface.blit(reset, (72, 185))
    Surface.blit(save, (67, 335))
    Surface.blit(retour, (110, 485))
    Surface.blit(Parchemin2, (825, 647))
    Surface.blit(valider, (885, 670))

    Surface.blit(a, (610, 12))
    Surface.blit(b, (610, 75))
    Surface.blit(c, (775, 12))
    Surface.blit(d, (775, 75))
    Surface.blit(e, (940, 12))
    Surface.blit(f, (940, 75))
    Surface.blit(g, (1100, 12))
    Surface.blit(h, (1100, 75))

    Surface.blit(p1, (705, 17))
    Surface.blit(p2, (705, 78))
    Surface.blit(m1, (870, 17))
    Surface.blit(m2, (870, 78))
    Surface.blit(s1, (1035, 17))
    Surface.blit(s2, (1035, 78))
    Surface.blit(l1, (1200, 17))
    Surface.blit(l2, (1200, 78))

    for x in range(10):
        for y in range(8):
            if x == 0 :
                Surface.blit(Case_oeil, (x * 65 + 600, y * 65 + 125))
            elif x == 9 :
                Surface.blit(Case_baton, (x * 65 + 600, y * 65 + 125))
            elif x == 1 and y == 0:
                Surface.blit(Case_baton, (x * 65 + 600, y * 65 + 125))
            elif x == 1 and y == 7:
                Surface.blit(Case_baton, (x * 65 + 600, y * 65 + 125))
            elif x == 8 and y == 0:
                Surface.blit(Case_oeil, (x * 65 + 600, y * 65 + 125))
            elif x == 8 and y == 7:
                Surface.blit(Case_oeil, (x * 65 + 600, y * 65 + 125))
            else:
                Surface.blit(Case_neutre, (x * 65 + 600, y * 65 + 125))

    for x in range(10):
        for y in range(8):
            if gameBoard[x][y][1] == 1:
                Surface.blit(Pharaoh(gameBoard[x][y][2],gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))
            elif gameBoard[x][y][1] == 2:
                Surface.blit(scarab(gameBoard[x][y][2],gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))
            elif gameBoard[x][y][1] == 3:
                Surface.blit(anubis(gameBoard[x][y][2],gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))
            elif gameBoard[x][y][1] == 4:
                Surface.blit(pyramid(gameBoard[x][y][2],gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))
            elif gameBoard[x][y][1] == 5:
                Surface.blit(sphinh(gameBoard[x][y][2],gameBoard[x][y][0], choice), (x * 65 + 600, y * 65 + 125))


def info(Surface,select, choice):
    font = pygame.font.SysFont("Calibri", 28)
    info_cadre = pygame.image.load('sprites/commun/info_cadre.png')
    info_select = pygame.image.load('sprites/commun/info_select.png')
    info_select2 = pygame.image.load('sprites/commun/info_select2.png')
    info_select3 = pygame.image.load('sprites/commun/info_1.png')
    pharaon = pygame.image.load('sprites/pack' + str(choice) + '/pieces/pharaon 1.png')
    sphinx = pygame.image.load('sprites/pack' + str(choice) + '/pieces/laser 1.png')
    scarabe = pygame.image.load('sprites/pack' + str(choice) + '/pieces/scaraber 1.png')
    pyramide = pygame.image.load('sprites/pack' + str(choice) + '/pieces/mirroir 1.png')
    anubis = pygame.image.load('sprites/pack' + str(choice) + '/pieces/anubis 1.png')
    pharaon = pygame.transform.scale(pharaon, (200, 200))
    sphinx = pygame.transform.scale(sphinx, (200, 200))
    scarabe = pygame.transform.scale(scarabe, (200, 200))
    pyramide = pygame.transform.scale(pyramide, (200, 200))
    anubis = pygame.transform.scale(anubis, (200, 200))
    text0 = font.render("Présentation", 1, (0, 0, 0))
    text1 = font.render("Partie", 1, (0, 0, 0))
    text2 = font.render("Déplacement", 1, (0, 0, 0))
    text3 = font.render("Pharaon", 1, (0, 0, 0))
    text4 = font.render("Sphinx", 1, (0, 0, 0))
    text5 = font.render("Scarabé", 1, (0, 0, 0))
    text6 = font.render("Pyramide", 1, (0, 0, 0))
    text7 = font.render("Anubis", 1, (0, 0, 0))
    info_cadre = pygame.transform.scale(info_cadre, (1200, 700))
    info_select = pygame.transform.scale(info_select, (300, 110))
    info_select2 = pygame.transform.scale(info_select2, (300, 110))
    info_select3 = pygame.transform.scale(info_select3, (300, 300))    # Présentation du jeu
    Surface.blit(info_cadre,(50, 25))

    for i in range(8):
        if i == select:
            Surface.blit(info_select2, (80, 37 + i*77))            # Surface.blit(info_select, (80, 60 + i * 68))
        else:
            Surface.blit(info_select, (80, 37 + i * 77))
    Surface.blit(text0, (140, 86 + 0 * 77))
    Surface.blit(text1, (140, 86 + 1 * 77))
    Surface.blit(text2, (140, 86 + 2 * 77))
    Surface.blit(text3, (140, 86 + 3 * 77))
    Surface.blit(text4, (140, 86 + 4 * 77))
    Surface.blit(text5, (140, 86 + 5 * 77))
    Surface.blit(text6, (140, 86 + 6 * 77))
    Surface.blit(text7, (140, 86 + 7 * 77))
    if select == 0:
        text = font.render("Le but du jeu est de détruire le pharaon de votre adversaire en", 1, (0, 0, 0))
        text1 = font.render("faisant rebondir les faisceaux laser sur les pièces présentes sur le ", 1, (0, 0, 0))
        text2 = font.render("plateau. Orientez vos pièces pour vous donner l'avantage tout en ", 1, (0, 0, 0))
        text3 = font.render("évitant le laser de votre adversaire.", 1, (0, 0, 0))
        Surface.blit(text, (380,100))
        Surface.blit(text1, (380, 125))
        Surface.blit(text2, (380, 150))
        Surface.blit(text3, (380, 175))
        Surface.blit(info_select3, (600, 275))

    elif select == 1:
        map1 = pygame.image.load('map/map1.png')
        map2 = pygame.image.load('map/map2.png')
        map3 = pygame.image.load('map/map3.png')
        map4 = pygame.image.load('map/map4.png')
        nom1 = font.render("Classique", 1, (0, 0, 0))
        nom2 = font.render("Dynastie", 1, (0, 0, 0))
        nom3 = font.render("Imhotep", 1, (0, 0, 0))
        nom4 = font.render("Aléatoire", 1, (0, 0, 0))
        nom5 = font.render("Editée", 1, (0, 0, 0))
        text = font.render("Choisir une configuration de partie parmi 3 de base, 1 aléatoire et ", 1,(0, 0, 0))
        text1 = font.render("celle que vous avez pu éditer grâce à l'éditeur.", 1,(0, 0, 0))
        map1 = pygame.transform.scale(map1, (180, 180))
        map2 = pygame.transform.scale(map2, (180, 180))
        map3 = pygame.transform.scale(map3, (180, 180))
        map4 = pygame.transform.scale(map4, (180, 180))
        Surface.blit(text, (380, 100))
        Surface.blit(text1, (380, 125))

        Surface.blit(nom1, (450, 190))
        Surface.blit(nom2, (670, 190))
        Surface.blit(nom3, (890, 190))
        Surface.blit(nom4, (560, 430))
        Surface.blit(nom5, (780, 430))

        Surface.blit(map1, (440, 220))
        Surface.blit(map2, (660, 220))
        Surface.blit(map3, (880, 220))
        Surface.blit(map4, (550, 460))
        Surface.blit(map4, (770, 460))

    elif select == 2:
        map1 = pygame.image.load('sprites/commun/info_2.png')
        text = font.render("A chaque tour, deux options s'offrent à vous : ", 1,(0, 0, 0))
        text1 = font.render("-   Déplacer une de vos pièces sur une case libre adjaçante y ", 1,(0, 0, 0))
        text2 = font.render("     compris en diagonale.", 1, (0, 0, 0))
        text3 = font.render("-   Ou faire pivoter une pièce d'un quart de tour dans le sens voulu.", 1, (0, 0, 0))
        text4 = font.render("Une pièce ne peut pas être déplacée et tournée pendant le même ", 1, (0, 0, 0))
        text5 = font.render("tour. Après qu'un joueur ait joué, le laser est tiré (Sphinx).", 1, (0, 0, 0))
        text6 = font.render("Si une pièce est frappée sur un côté non-miroité, la pièce est ", 1, (0, 0, 0))
        text7 = font.render("détruite et retirée du plateau de jeu, sinon elle rebondit et continue ", 1, (0, 0, 0))
        text8 = font.render("jusqu'à la pièce suivante, à moins de sortir du plateau. ", 1, (0, 0, 0))
        text9 = font.render("[COMMANDES]   Clic Gauche : Sélectionner, Clic Droit : Désélectionner ", 1, (0, 0, 0))

        Surface.blit(text, (380, 100))
        Surface.blit(text1, (380, 150))
        Surface.blit(text2, (380, 175))
        Surface.blit(text3, (380, 200))
        Surface.blit(text4, (380, 250))
        Surface.blit(text5, (380, 275))
        Surface.blit(text6, (380, 325))
        Surface.blit(text7, (380, 350))
        Surface.blit(text8, (380, 375))
        Surface.blit(text9, (380, 425))
        Surface.blit(map1, (125, 260))

    elif select == 3:
        Surface.blit(pharaon, (670, 300))
        text = font.render("Pièce principale du joueur, celle-ci doit être protégée des faisceaux  ", 1, (0, 0, 0))
        text1 = font.render("laser. Si elle est touchée, le joueur perd la partie.", 1, (0, 0, 0))
        Surface.blit(text, (380,100))
        Surface.blit(text1, (380, 125))

    elif select == 4:
        Surface.blit(sphinx, (670, 300))
        text = font.render("Cette pièce tire un faisceau laser dans une direction. Elle ne peut", 1, (0, 0, 0))
        text1 = font.render("cependant pas être déplacée. Cependant, elle absorbe les lasers ", 1, (0, 0, 0))
        text2 = font.render("venant de toutes les directions.", 1, (0, 0, 0))
        Surface.blit(text, (380,100))
        Surface.blit(text1, (380, 125))
        Surface.blit(text2, (380, 150))

    elif select == 5:
        Surface.blit(scarabe, (670, 300))
        text = font.render("Cette pièce réfléchit le faisceau laser venant de n'importe quelle ", 1, (0, 0, 0))
        text1 = font.render("direction et la dévie de 90° (dépend de la provenance initiale du ", 1, (0, 0, 0))
        text2 = font.render("faisceau).", 1, (0, 0, 0))
        Surface.blit(text, (380,100))
        Surface.blit(text1, (380, 125))
        Surface.blit(text2, (380, 150))

    elif select == 6:
        Surface.blit(pyramide, (660, 300))
        text = font.render("Cette pièce est senblable au Scarabé mais ne refléchit le laser ", 1, (0, 0, 0))
        text1 = font.render("provenant que de deux directions adjaçantes, symbolisées par", 1, (0, 0, 0))
        text2 =  font.render("un côté miroité. Sinon, cette pièce est détruite.", 1, (0, 0, 0))
        Surface.blit(text, (380,100))
        Surface.blit(text1, (380, 125))
        Surface.blit(text2, (380, 150))

    elif select == 7:
        Surface.blit(anubis, (670, 300))
        text = font.render("Cette pièce absorbe le faisceau laser provenant d'une seule  ", 1, (0, 0, 0))
        text1 = font.render("direction (face avant de la pièce). Dans les autres cas, celle-ci", 1, (0, 0, 0))
        text2 = font.render('est détruite.', 1, (0, 0, 0))
        Surface.blit(text, (380,100))
        Surface.blit(text1, (380, 125))
        Surface.blit(text2, (380, 150))


def rules(Surface, select):
    font = pygame.font.SysFont("Calibri", 28)
    noir = (0, 0, 0)
    info_cadre = pygame.image.load('sprites/commun/info_cadre.png')
    info_select = pygame.image.load('sprites/commun/info_select.png')
    info_select2 = pygame.image.load('sprites/commun/info_select2.png')
    info_select3 = pygame.image.load('sprites/commun/info_cadre.png')
    info_cadre = pygame.transform.scale(info_cadre, (1200, 700))
    info_select = pygame.transform.scale(info_select, (300, 110))
    info_select3 = pygame.transform.scale(info_select, (300, 225))
    info_select4 = pygame.transform.scale(info_select2, (300, 225))


    Surface.blit(info_cadre,(50, 25))

    for i in range(4):
        if i == select:
            Surface.blit(info_select4, (80, 15 +i * 154))
        else:
            Surface.blit(info_select3, (80, 15 +i * 154))


    text0 = font.render("Solo", 1, (0, 0, 0))
    text1 = font.render("Multijoueur", 1, (0, 0, 0))
    text2 = font.render("Editeur", 1, (0, 0, 0))
    text3 = font.render("Thèmes et sons", 1, (0, 0, 0))

    Surface.blit(text0, (140, 123 + 0 * 154))
    Surface.blit(text1, (140, 123 + 1 * 154))
    Surface.blit(text2, (140, 123 + 2 * 154))
    Surface.blit(text3, (140, 123 + 3 * 154))

    if select == 0:
        text = font.render("Vos pions sont les rouges, ceux de l'adversaire sont les blancs.", 1, noir)
        text1 = font.render("Dans ce mode, affrontez un adversaire contrôlé par l'ordinateur.", 1, noir)
        text2 = font.render("Lors de votre tour, commencez par déplacer ou faire pivoter ", 1, noir)
        text3 = font.render("une de vos pièces sur le plateau. Une fois effectué, cliquez sur le ", 1, noir)
        text4 = font.render("bouton 'Tirer' pour déclencher votre laser.", 1, noir)
        text5 = font.render("Pour plus de détails sur le déroulement de la partie, référez vous à ", 1, noir)
        text6 = font.render("l'onglet informations dans le menu principal (cliquez sur l'icône).", 1, noir)
        Surface.blit(text, (370, 100))
        Surface.blit(text1, (370, 130))
        Surface.blit(text2, (370, 160))
        Surface.blit(text3, (370, 190))
        Surface.blit(text4, (370, 220))
        Surface.blit(text5, (370, 280))
        Surface.blit(text6, (370, 310))


    if select == 1:
        text = font.render("Le premier joueur contrôle les pions rouges et le second les blancs.", 1, noir)
        text1 = font.render("Dans ce mode, deux joueurs s'affrontent sur un même ordinateur.", 1, noir)
        text2 = font.render("Les règles de la partie dans le mode solo s'appliquent exactement ", 1, noir)
        text3 = font.render("de la même manière dans ce mode de jeu.", 1, noir)
        text4 = font.render("Dans le menu de selection de partie, 3 onglets s'offrent à vous : ", 1, noir)
        text5 = font.render("   1) Mode Ordinateur, les deux joueurs s'affrontent sur le même", 1, noir)
        text6 = font.render("        ordinateur.", 1, noir)
        text7 = font.render("   2) Mode Hébergeur, les deux joueurs possèdent la même version ", 1, noir)
        text8 = font.render("        du jeu et sont connectés via un même réseau local. Le premier", 1, noir)
        text9 = font.render("        premier joueur (rouge) héberge et contrôle les paramètres de la", 1, noir)
        text10 = font.render("        partie.", 1, noir)
        text11 = font.render("   3) Mode Rejoindre, à l'inverse du cas ci-dessus, le deuxième joueur,", 1, noir)
        text12 = font.render("     (blanc) va simplement rejoindre la partie précédemment créée.", 1, noir)
        Surface.blit(text, (370, 100))
        Surface.blit(text1, (370, 130))
        Surface.blit(text2, (370, 160))
        Surface.blit(text3, (370, 190))
        Surface.blit(text4, (370, 250))
        Surface.blit(text5, (370, 280))
        Surface.blit(text6, (370, 310))
        Surface.blit(text7, (370, 340))
        Surface.blit(text8, (370, 370))
        Surface.blit(text9, (370, 400))
        Surface.blit(text10, (370, 430))
        Surface.blit(text11, (370, 460))
        Surface.blit(text12, (370, 490))


    if select == 2:
        text = font.render("L'éditeur permet de créer une carte qui une fois validée, pourra être ", 1, noir)
        text1 = font.render("sélectionnée dans les différents modes de jeu.", 1, noir)
        text2 = font.render("Pour éditer une carte valide, veillez à placer les Sphinx dans les ", 1, noir)
        text3 = font.render("coins supérieur gauche (rouge)  et inférieur droit (blanc), tous les  ", 1, noir)
        text4 = font.render("deux respectivement tournés vers le bas et vers le haut. ", 1, noir)
        text5 = font.render("Pour le reste des pièces, veillez à placer un exemplaire de chaque ", 1, noir)
        text6 = font.render("Pharaon, au moins une Pyramide et un Sacrabée par joueur, Anubis  ", 1, noir)
        text7 = font.render("Anubis n'étant pas obligatoire dans la configuration minimale valide.", 1, noir)
        text8 = font.render("Pour enregistrer une configuration de carte valide, veillez à cliquer ", 1, noir)
        text9 = font.render("sur le bouton valider. Si le bouton 'Valider' est rouge, la configuration  ", 1, noir)
        text10 = font.render("entrée est erronée. S'il passe au vert, cliquez sur sauvegarder pour", 1, noir)
        text11 = font.render("enregistrer la carte. Vous pouvez alors retourner au menu.", 1, noir)
        Surface.blit(text, (370, 100))
        Surface.blit(text1, (370, 130))
        Surface.blit(text2, (370, 190))
        Surface.blit(text3, (370, 220))
        Surface.blit(text4, (370, 250))
        Surface.blit(text5, (370, 310))
        Surface.blit(text6, (370, 340))
        Surface.blit(text7, (370, 370))
        Surface.blit(text8, (370, 430))
        Surface.blit(text9, (370, 460))
        Surface.blit(text10, (370, 490))
        Surface.blit(text11, (370, 520))


    if select == 3:
        text = font.render("Accédez au menu des thèmes pour changer l'interface et les sons ", 1, noir)
        text1 = font.render("du jeu. Contrôlez le son via le menu principal pour l'activer ou le", 1, noir)
        text2 = font.render("désactiver. 2 thèmes sont présents dans le jeu, Egypte Ancienne par ", 1, noir)
        text3 = font.render("défaut et un autre Mario, avec des pièces personnellement éditées.", 1, noir)
        Surface.blit(text, (370, 100))
        Surface.blit(text1, (370, 130))
        Surface.blit(text2, (370, 160))
        Surface.blit(text3, (370, 190))


def verif_editeur(Surface, choice):
    info_cadre = pygame.image.load('sprites/commun/info_cadre.png')
    info_cadre = pygame.transform.scale(info_cadre, (1200, 700))
    noir = (0, 0, 0)
    font = pygame.font.SysFont('Calibri', 50)
    font2 = pygame.font.SysFont('Calibri', 35)
    text = font.render("Configuration minimale requise", 1, noir, 1)
    Surface.blit(info_cadre,(50, 25))
    Surface.blit(text, (345, 100))
    pygame.draw.line(Surface, noir, (645, 180), (645, 620), 3)
    p1 =  pygame.image.load('sprites/pack' + str(choice) + '/pieces/pharaon 1.png')
    p2 = pygame.image.load('sprites/pack' + str(choice) + '/pieces/pharaonb 1.png')
    s1 =  pygame.image.load('sprites/pack' + str(choice) + '/pieces/scaraber 1.png')
    s2 = pygame.image.load('sprites/pack' + str(choice) + '/pieces/scaraberb 1.png')
    m1 =  pygame.image.load('sprites/pack' + str(choice) + '/pieces/mirroir 1.png')
    m2 = pygame.image.load('sprites/pack' + str(choice) + '/pieces/mirroirb 1.png')
    l1 =  pygame.image.load('sprites/pack' + str(choice) + '/pieces/laser 1.png')
    l2 = pygame.image.load('sprites/pack' + str(choice) + '/pieces/laserb 1.png')

    p1 = pygame.transform.scale(p1, (60, 60))
    p2 = pygame.transform.scale(p2, (60, 60))
    s1 = pygame.transform.scale(s1, (60, 60))
    s2 = pygame.transform.scale(s2, (60, 60))
    m1 = pygame.transform.scale(m1, (60, 60))
    m2 = pygame.transform.scale(m2, (60, 60))
    l1 = pygame.transform.scale(l1, (60, 60))
    l2 = pygame.transform.scale(l2, (60, 60))

    text_p1 = font2.render("x1", 1, noir)
    text_p2 = font2.render("x1", 1, noir)
    text_s1 = font2.render("> 0 ", 1, noir)
    text_s2 = font2.render("> 0 ", 1, noir)
    text_m1 = font2.render("> 0", 1, noir)
    text_m2 = font2.render("> 0 ", 1, noir)
    text_l1 = font2.render("x1 (tourné vers le bas)", 1, noir)
    text_l2 = font2.render("x1 (tourné vers le haut)", 1, noir)


    Surface.blit(p1, (170, 200))
    Surface.blit(m1, (170, 320))
    Surface.blit(s1, (170, 440))
    Surface.blit(l1, (170, 560))
    Surface.blit(p2, (700, 200))
    Surface.blit(s2, (700, 320))
    Surface.blit(m2, (700, 440))
    Surface.blit(l2, (700, 560))

    Surface.blit(text_p1, (240, 215))
    Surface.blit(text_p2, (770, 215))
    Surface.blit(text_s1, (240, 335))
    Surface.blit(text_s2, (770, 335))
    Surface.blit(text_m1, (240, 455))
    Surface.blit(text_m2, (770, 455))
    Surface.blit(text_l1, (240, 575))
    Surface.blit(text_l2, (770, 575))


def A_laser(Surface,gameBoard,gameBoard_coordonnée,T_joueur, choice, need_rotat):
    if need_rotat == False:
        move = True
    else:
        move = False
    direction_affichage = [-1, -1]
    direction = [-1, -1]
    laser_img = pygame.image.load('sprites/pack' + str(choice) + '/imgs/laser.png')
    for x in range(10):
        for y in range(8):
            if gameBoard[x][y][1] == 5 and gameBoard[x][y][0] == T_joueur:
                direction_affichage[0] = gameBoard_coordonnée[x][y][0] + 6
                direction_affichage[1] = gameBoard_coordonnée[x][y][1] + 10
                direction[0] = x
                direction[1] = y
                rotation = gameBoard[x][y][2]
    for x in range(30):
        Surface.blit(laser_img, (direction_affichage[0], direction_affichage[1]))
        direction_affichage[0], direction_affichage[1] = laser_move_affichage(rotation, direction_affichage[0],direction_affichage[1])

        pygame.time.delay(2)
    direction[0], direction[1] = laser_move_affichage(rotation, direction[0], direction[1])
    while move:

        if direction[0] == 10 or direction[0] == -1 or direction[1] == 8 or direction[1] == -1 or rotation == "mur":
            direction = [-1, -1]
            move = False

        elif gameBoard[direction[0]][direction[1]][1] == 0:
            for x in range(65):
                Surface.blit(laser_img, (direction_affichage[0], direction_affichage[1]))
                direction_affichage[0], direction_affichage[1] = laser_move_affichage(rotation, direction_affichage[0],direction_affichage[1])
                pygame.display.flip()
                pygame.time.delay(2)
            direction[0], direction[1] = laser_move_affichage(rotation, direction[0], direction[1])

        elif gameBoard[direction[0]][direction[1]][1] == 1:
            move = False

        elif gameBoard[direction[0]][direction[1]][1] == 2:
            for x in range(38):
                Surface.blit(laser_img, (direction_affichage[0], direction_affichage[1]))
                direction_affichage[0], direction_affichage[1] = laser_move_affichage(rotation, direction_affichage[0],direction_affichage[1])
                pygame.display.flip()
                pygame.time.delay(2)
            rotation = laser_direction(gameBoard[direction[0]][direction[1]][2],rotation,1)
            for x in range(30):
                Surface.blit(laser_img, (direction_affichage[0], direction_affichage[1]))
                direction_affichage[0], direction_affichage[1] = laser_move_affichage(rotation, direction_affichage[0],direction_affichage[1])
                pygame.display.flip()
                pygame.time.delay(2)
            direction[0], direction[1] = laser_move_affichage(rotation, direction[0], direction[1])

        elif gameBoard[direction[0]][direction[1]][1] == 3:
            rotation = laser_direction(gameBoard[direction[0]][direction[1]][2], rotation, 3)
            if rotation == "bloque":
                direction = [-1,-1]
                move = False
            else:
                move = False

        elif gameBoard[direction[0]][direction[1]][1] == 4:
            for x in range(38):
                Surface.blit(laser_img, (direction_affichage[0], direction_affichage[1]))
                direction_affichage[0], direction_affichage[1] = laser_move_affichage(rotation, direction_affichage[0],direction_affichage[1])
                pygame.display.flip()
                pygame.time.delay(2)
            rotation = laser_direction(gameBoard[direction[0]][direction[1]][2],rotation,2)
            if rotation == "mur":
                move = False
            for x in range(30):
                Surface.blit(laser_img, (direction_affichage[0], direction_affichage[1]))
                direction_affichage[0], direction_affichage[1] = laser_move_affichage(rotation, direction_affichage[0],direction_affichage[1])
                pygame.display.flip()
                pygame.time.delay(2)
            direction[0], direction[1] = laser_move_affichage(rotation, direction[0], direction[1])

        elif gameBoard[direction[0]][direction[1]][1] == 5:
            direction = [-1, -1]
            move = False

        else:
            direction = [-1, -1]
            move = False

    if need_rotat:
        return direction, rotation
    else:
        return direction

    pygame.time.delay(1000)
    return direction


def win(Surface,T_joueur, choice):
    cadre = pygame.image.load('sprites/pack' + str(choice) + '/imgs/win.png')
    cadre = pygame.transform.scale(cadre, (1280, 720))
    blanc = (255, 255, 255)
    Surface.blit(cadre, (0, 0))
    font = pygame.font.SysFont("Calibri", 60)
    font2 = pygame.font.SysFont("Calibri", 40)
    victoire = font.render("Victoire du Joueur " + str(T_joueur), 1, blanc, 1)
    rejouer = font2.render("Rejouer", 1, blanc, 1)
    again = font2.render("Menu", 1, blanc,1)
    quitter = font2.render("Quitter", 1, blanc, 1)
    Surface.blit(victoire, (400, 150))
    Surface.blit(rejouer, (50, 650))
    Surface.blit(again, (610, 650))
    Surface.blit(quitter, (1100, 650))