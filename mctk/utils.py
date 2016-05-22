import math
from mcpi.minecraft import Minecraft

def combine(point, block):
    return point+(block,)

def set_points(point_set, mc, block_num):
    if isinstance(block_num, tuple):
        block_num, block_type = block_num
    else:
        block_type = 0
    for point in point_set:
        x,y,z = point
        mc.setBlock(x, y, z, block_num, block_type)

def translate_points(point_set, xdiff, ydiff, zdiff):
    new_point_set = set()
    for point in point_set:
        x,y,z = point
        new_point = (x+xdiff, y+ydiff, z+zdiff)
        new_point_set.add(new_point)
    return new_point_set

def every_arc(rate, func, r):
    for angle in range(360):
        if angle % rate == 0:
            theta = math.radians(angle)
            x = int(r*math.sin(theta))
            z = int(r*math.cos(theta))
            func(x, z)

def clear_region(x,y,z, size):
    '''will clear a cube with sides = size'''
    mc = Minecraft.create()
    mc.setBlocks(x-size/2,y-size/2, z-size/2, x+size/2, y+size/2, z+size/2, 0)

def clear_by_player(size):
    mc = Minecraft.create()
    x,y,z = mc.player.getPos()
    clear_region(x,y,z,size)    