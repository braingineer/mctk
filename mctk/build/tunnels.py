from ..utils import set_points, translate_points
from .circles import *

def tunnel_y(height, size, mc, pos=None, block=17):
    if pos is None:
        pos = mc.player.getPos()
    x,y,z = pos
    points = taxicab_circle_y(size)
    for i in range(height):
        new_points = translate_points(points, x, y+i, z)
        set_points(new_points, mc, block)

def tunnel_x(length, size, mc, pos=None, block=17):
    if pos is None:
        pos = mc.player.getPos()
    x,y,z = pos
    points = taxicab_circle_x(size)
    for i in range(length):
        new_points = translate_points(points, x+i, y, z)
        set_points(new_points, mc, block)

def tunnel_z(length, size, mc, pos=None, block=17):
    if pos is None:
        pos = mc.player.getPos()
    x,y,z = pos
    points = taxicab_circle_z(size)
    for i in range(length):
        new_points = translate_points(points, x, y, z+i)
        set_points(new_points, mc, block)

def filled_y(height, size, mc, pos=None, block=17):
    if pos is None:
        pos = mc.player.getPos()
    x,y,z = pos
    points = taxicab_filled_y(size)
    for i in range(height):
        new_points = translate_points(points, x, y+i, z)
        set_points(new_points, mc, block)