c_menu = True
c_editeur = False
c_solo = False
c_multi = False
c_themes = False
c_menu_solo = False
c_chargement = False
c_menu_pause = False
c_sauvegarde = False
c_menu_multi = False
c_menu_hebergement = False
c_menu_rejoindre = False
c_rules = False
c_menu_info = False
c_verif_editeur = False
c_multi_local = False
c_win = False


etat_sauvegarde = 0  # 0 par défaut, les conditons de la map éditée ne sont pas respectées
var1 = 1
musique = 1
etat_menu = ''
etat_alea = 0

type = 1
etat_son = 1
piece = 1
couleur = 1
select = 0
choice = 1
choice_map = 1
A = 0
T_joueur = 1
difficulty = 1
fps = 120
action = 1
anime = 0
select_info = 0
select_piéce = [-1,-1]
gameBoard = [[[0 for k in range(3)] for j in range(8)] for i in range(10)]
gameBoard_coordonnée = [[[0 for k in range(2)] for j in range(8)] for i in range(10)]
read_save = open("save/editeur.txt", "r")
gameBoard = eval(read_save.readline())
read_save.close()

for i in range(10):
    for j in range(8):
        gameBoard_coordonnée[i][j][0] = i * 65 + 600
        gameBoard_coordonnée[i][j][1] = j * 65 + 125