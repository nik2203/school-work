import pyxel
from constants import *
from random import randint

def float_equal(x1, x2, eps = 0.00000001):
    return (x2 - eps < x1 < x2 + eps)

def square_distance(player, tile):
    return (player.x - tile.x)**2 + (player.y - tile.y)**2

def make_object_array(n, p):
    array = []
    for i in range(n):
        array.append([])
    for i in range(n):
        for j in range(p):
            array[i].append([])
    return array

def make_zeros_array(n, p):
    array = []
    for i in range(n):
        array.append([])
    for i in range(n):
        for j in range(p):
            array[i].append([0])
    return array

def get_level_map(level):
    data = pyxel.image(1, system=True).data
    array = make_zeros_array(TN, TN)
    offset_i, offset_j = TN * (level // 8), TN*(level%8)
    for i in range(TN):
        for j in range(TN):
            array[i][j] = data[j+offset_j][i+offset_i]
    print("level :", level)
    return array

 ######  ######## ##    ##  ######   #######  ########   ######
##    ## ##       ###   ## ##    ## ##     ## ##     ## ##    ##
##       ##       ####  ## ##       ##     ## ##     ## ##
 ######  ######   ## ## ##  ######  ##     ## ########   ######
      ## ##       ##  ####       ## ##     ## ##   ##         ##
##    ## ##       ##   ### ##    ## ##     ## ##    ##  ##    ##
 ######  ######## ##    ##  ######   #######  ##     ##  ######


class Sensor:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hitbox = [0, 0, self.w, self.h]
        self.color = randint(0,15)

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)


def are_recangles_overlapping(xmin1, xmax1, ymin1, ymax1, xmin2, xmax2, ymin2, ymax2):
    x_collide = xmax1 > xmin2 and xmin1 < xmax2
    y_collide = ymax1 > ymin2 and ymin1 < ymax2
    return x_collide and y_collide

def objects_overlapping(obj1, obj2):
    return are_recangles_overlapping(obj1.x + obj1.hitbox[0], obj1.x + obj1.hitbox[2], obj1.y + obj1.hitbox[1], obj1.y + obj1.hitbox[3], obj2.x + obj2.hitbox[0], obj2.x + obj2.hitbox[2], obj2.y + obj2.hitbox[1], obj2.y + obj2.hitbox[3])

def make_sensors(parent_object, offset_x, offset_y):
    x = parent_object.x
    y = parent_object.y
    w = parent_object.w
    h = parent_object.h
    top_sensor = Sensor(x + offset_x, y, w - 2*offset_x, h/2)
    right_sensor = Sensor(x + w/2, y + offset_y, w/2+1, h - 2*offset_y)
    bottom_sensor = Sensor(x + offset_x, y + h/2, w - 2*offset_x, h/2)
    left_sensor = Sensor(x, y + offset_y, w/2, h - 2*offset_y)
    parent_object.sensors = [top_sensor, right_sensor, bottom_sensor, left_sensor]

def update_sensors(object, offset_x, offset_y, floor_sensors=True, side_sensors=True):
    x = object.x
    y = object.y
    w = object.w
    h = object.h
    object.sensors[0].x = x + offset_x + 1
    object.sensors[0].y = y
    object.sensors[1].x = x + w/2 - 1
    object.sensors[1].y = y + offset_y
    object.sensors[2].x = x + offset_x + 1
    object.sensors[2].y = y + h/2
    object.sensors[3].x = x
    object.sensors[3].y = y + offset_y

    if floor_sensors:
        object.sensors[4].x = x + 2
        object.sensors[4].y = y + h/2
        object.sensors[5].x = x
        object.sensors[5].y = y + h/2
    if side_sensors:
        object.sensors[6].x = x - 1
        object.sensors[6].y = y + h/2 - 1
        object.sensors[7].x = x + w/2 + 1
        object.sensors[7].y = y + h/2 - 1


def sensor_sensor(sens1, sens2):
    if objects_overlapping(sens1[0], sens2[2]):
        return 0
    elif objects_overlapping(sens1[2], sens2[0]):
        return 2
    elif objects_overlapping(sens1[1], sens2[3]):
        return 1
    elif objects_overlapping(sens1[3], sens2[1]):
        return 3
    else:
        return -1

def sensor_object(sens1, obj):
    if objects_overlapping(sens1[0], obj):
        return 0
    elif objects_overlapping(sens1[2], obj):
        return 2
    elif objects_overlapping(sens1[1], obj):
        return 1
    elif objects_overlapping(sens1[3], obj):
        return 3
    else:
        return -1

def tile_collision(obj, tile):
    update_sensors(obj, obj.offset_x, obj.offset_y)
    if objects_overlapping(obj.sensors[0], tile):
        obj.y = tile.y + tile.h
        obj.vy *= -0.2
    if objects_overlapping(obj.sensors[1], tile):
        obj.x = tile.x - obj.w
        obj.vx = 0
    if objects_overlapping(obj.sensors[2], tile):
        obj.y = tile.y - obj.h
        obj.vy = 0
        obj.on_ground = True
    if objects_overlapping(obj.sensors[3], tile):
        obj.x = tile.x + tile.w
        obj.vx = 0
    update_sensors(obj, obj.offset_x, obj.offset_y)
