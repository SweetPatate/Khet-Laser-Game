def laser_move_affichage(rotation,direction_x,direction_y):
    if rotation == 3:
        direction_x += 1
    elif rotation == 0:
        direction_y += 1
    elif rotation == 1:
        direction_x -= 1
    elif rotation == 2:
        direction_y -= 1
    return direction_x,direction_y

def laser_direction(rotation_piéce,rotation_laser,type):
    if type == 1:
        if rotation_piéce == 0 or rotation_piéce == 2:
            if rotation_laser == 0:
                rotation_laser = 1
            elif rotation_laser == 1:
                rotation_laser = 0
            elif rotation_laser == 2:
                rotation_laser = 3
            elif rotation_laser == 3:
                rotation_laser = 2
            else:
                rotation_laser = "mur"

        elif rotation_piéce == 1 or rotation_piéce == 3:
            if rotation_laser == 0:
                rotation_laser = 3
            elif rotation_laser == 1:
                rotation_laser = 2
            elif rotation_laser == 2:
                rotation_laser = 1
            elif rotation_laser == 3:
                rotation_laser = 0
            else:
                rotation_laser = "mur"

    elif type == 2:
        if rotation_piéce == 0:
            if rotation_laser == 3:
                rotation_laser = 0
            elif rotation_laser == 2:
                rotation_laser = 1
            else:
                rotation_laser = "mur"

        elif rotation_piéce == 1:
            if rotation_laser == 3:
                rotation_laser = 2
            elif rotation_laser == 0:
                rotation_laser = 1
            else:
                rotation_laser = "mur"

        elif rotation_piéce == 2:
            if rotation_laser == 1:
                rotation_laser = 2
            elif rotation_laser == 0:
                rotation_laser = 3
            else:
                rotation_laser = "mur"

        elif rotation_piéce == 3:
            if rotation_laser == 1:
                rotation_laser = 0
            elif rotation_laser == 2:
                rotation_laser = 3
            else:
                rotation_laser = "mur"
    elif type == 3:
        if rotation_piéce == 0:
            if rotation_laser == 2:
                rotation_laser = "bloque"
        elif rotation_piéce == 1:
            if rotation_laser == 3:
                rotation_laser = "bloque"
        elif rotation_piéce == 2:
            if rotation_laser == 0:
                rotation_laser = "bloque"
        elif rotation_piéce == 3:
            if rotation_laser == 1:
                rotation_laser = "bloque"

    return rotation_laser