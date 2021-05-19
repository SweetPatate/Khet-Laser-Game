from Affichage import A_laser
from random import randint
from copy import copy


def choose_piece(game_board, t_joueur, surface, game_board_coord, choice):
    vulnerable, direction = is_vulnerable(
        game_board, t_joueur, surface, game_board_coord, choice)
    select_piece = [-1, -1]
    new_position = [-1, -1]
    new_rotation = -1
    pharaoh_position = []
    if direction[0] != 0 and vulnerable:
        coming_from = "h"
    elif direction[1] != 0 and vulnerable:
        coming_from = "v"
    done = False
    for y in range(9):
        for x in range(7):
            if game_board[y][x][1] == 1 and game_board[y][x][0] == t_joueur:
                pharaoh_position = [x, y]
                done = True
                break
        if done:
            break

    if vulnerable:
        if coming_from == "v":
            for y in range(7, 0):
                if game_board[pharaoh_position[0]][y - 1][0] == t_joueur and 5 < game_board[pharaoh_position[0]][y - 1][1] > 1:
                    if game_board[pharaoh_position[0]][y - 1][1] == 4 or game_board[pharaoh_position[0]][y - 1][1] == 2:
                        select_piece = [pharaoh_position[0], y - 1]
                        new_position = [pharaoh_position[0], y - 1]
                        new_rotation = direction - 1
                else: # search for near pawn to move
                    for y in range(7, 0):
                        if pharaoh_position[0] > 0 and game_board[pharaoh_position[0] - 1][y - 1][0] == t_joueur and 5 < game_board[pharaoh_position[0] - 1][y - 1][1] > 1:
                            select_piece = [pharaoh_position[0] - 1, y - 1]
                            new_position = [pharaoh_position[0], y - 1]
                            new_rotation = direction
                        elif pharaoh_position[0] < 7 and game_board[pharaoh_position[0] + 1][y - 1][0] == t_joueur and 5 < game_board[pharaoh_position[0] + 1][y - 1][1] > 1:
                            select_piece = [pharaoh_position[0] + 1, y - 1]
                            new_position = [pharaoh_position[0], y - 1]
                            new_rotation = direction
                        elif pharaoh_position[1] < 9 and game_board[pharaoh_position[0]][pharaoh_position[1] + 1] == t_joueur and game_board[pharaoh_position[0]][pharaoh_position[1] + 1][1] > 1:
                            select_piece = [pharaoh_position[0]][pharaoh_position[1] + 1]
                            new_position = [pharaoh_position[0] + 1][pharaoh_position[1]]
                            new_rotation = direction
                        elif pharaoh_position[1] > 0 and game_board[pharaoh_position[0]][pharaoh_position[1] - 1] == t_joueur and game_board[pharaoh_position[0]][pharaoh_position[1] - 1][1] > 1:
                            select_piece = [pharaoh_position[0]][pharaoh_position[1] - 1]
                            new_position = [pharaoh_position[0] + 1][pharaoh_position[1]]
                            new_rotation = direction
        elif coming_from == "h":
            for x in range(9, 0):
                if game_board[x - 1][pharaoh_position[1]][0] == t_joueur and game_board[x - 1][pharaoh_position[1]][1] > 1:
                    if game_board[x - 1][pharaoh_position[1]][1] == 4 or game_board[x - 1][pharaoh_position[1]][1] == 2:
                        select_piece = [x - 1, pharaoh_position[1]]
                        new_position = [x - 1, pharaoh_position[1]]
                        new_rotation = direction - 1
                else: # search for near pawn to move
                    for x in range(9, 0):
                        if pharaoh_position[1] > 0 and game_board[x - 1][pharaoh_position[1] - 1][0] == t_joueur and game_board[x - 1][pharaoh_position[1] - 1][1] > 1:
                            select_piece = [x - 1, pharaoh_position[1] - 1]
                            new_position = [x - 1, pharaoh_position[1] - 1]
                            new_rotation = direction
                        elif pharaoh_position[1] < 9 and game_board[x - 1][pharaoh_position[1] + 1][0] == t_joueur and game_board[x - 1][pharaoh_position[1] + 1][1] > 1:
                            select_piece = [x - 1, pharaoh_position[1] + 1]
                            new_position = [x - 1, pharaoh_position[1] + 1]
                            new_rotation = direction
                        elif pharaoh_position[0] < 7 and game_board[pharaoh_position[0] + 1][pharaoh_position[1]] == t_joueur and game_board[pharaoh_position[0] + 1][pharaoh_position[1]][1] > 1:
                            select_piece = [pharaoh_position[0] + 1][pharaoh_position[1]]
                            new_position = [pharaoh_position[0]][pharaoh_position[1] + 1]
                            new_rotation = direction
                        elif pharaoh_position[0] > 0 and game_board[pharaoh_position[0] - 1][pharaoh_position[1]] == t_joueur and game_board[pharaoh_position[0] - 1][pharaoh_position[1]][1] > 1:
                            select_piece = [pharaoh_position[0] - 1][pharaoh_position[1]]
                            new_position = [pharaoh_position[0]][pharaoh_position[1] + 1]
                            new_rotation = direction
    else: # Offensive move
        pawnList = []
        number = 0
        for y in range(9):
            for x in range(7):
                if game_board[y][x][0] == 2:
                    pawnList.append([[y, x], game_board[y][x][2]])
                    number += 1
        choser = randint(0, number - 1)
        chosenPawn = pawnList[choser][0]
        select_piece = copy(chosenPawn)
        move = randint(1, 3)
        if move == 1:
            randomMove = randint(0, 7)
            if chosenPawn[0] == 7:
                while randomMove > 4:
                    randomMove -= 1
            if chosenPawn[0] == 0:
                while 0 < randomMove < 4:
                    randomMove += 1
            if chosenPawn[1] == 0:
                while randomMove < 2:
                    randomMove += 1
                if randomMove == 7:
                    randomMove -= 1
            if chosenPawn[1] == 9:
                while 6 > randomMove > 2:
                    randomMove -= 1
            if randomMove == 0:
                new_position = [chosenPawn[1], chosenPawn[0] - 1]
            elif randomMove == 1:
                new_position = [chosenPawn[1] - 1, chosenPawn[0] - 1]
            elif randomMove == 2:
                new_position = [chosenPawn[1] - 1, chosenPawn[0]]
            elif randomMove == 3:
                new_position = [chosenPawn[1] - 1, chosenPawn[0] + 1]
            elif randomMove == 4:
                new_position = [chosenPawn[1], chosenPawn[0] + 1]
            elif randomMove == 5:
                new_position = [chosenPawn[1] + 1, chosenPawn[0] + 1]
            elif randomMove == 6:
                new_position = [chosenPawn[1] + 1, chosenPawn[0]]
            elif randomMove == 7:
                new_position = [chosenPawn[1] + 1, chosenPawn[0] - 1]
            new_rotation = pawnList[choser][1]
        else:
            new_rotation = pawnList[choser][1] + 1
            new_position = copy(select_piece)

    if new_rotation < 0:
        new_rotation = 3
    return select_piece, new_position, new_rotation


def is_vulnerable(game_board, t_joueur, surface, game_board_coord, choice):
    t_joueur = 1 if t_joueur == 2 else 2
    direction, rotation = A_laser(surface, game_board, game_board_coord, t_joueur, choice, True)
    if game_board[direction[0]][direction[1]][1] == 1 and direction != [-1, -1]:
        return True, rotation
    return False, [-1, -1]
