
def welcome_message():
    mc.postToChat("Welcome to the Atlantis! Hop on board!")
    mc.postToChat("Created by Ishan, Lyndon, and Sahil")
    mc.postToChat("Copyright Hill Billy Productions, Neverland USA")
welcome_message()


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from mctk.build import taxicab_circle_x, taxicab_circle_y, set_points, translate_points, rotate_points


def wheel_middle(size):
    pos = mc.player.getPos()
    x, y, z = pos
    points = taxicab_circle_x(size)
    new_points = translate_points(points, x, y, z)
    set_points(new_points, mc, 129)

def wheel_x_first(size):
    pos = mc.player.getPos()
    x, y, z = pos
    points = taxicab_circle_x(size)
    new_points = translate_points(points, x, y, z)
    set_points(new_points, mc, 168)

def wheel_x_second(size):
    pos = mc.player.getPos()
    x, y, z = pos
    points = taxicab_circle_x(size)
    new_points = translate_points(points, x, y, z)
    set_points(new_points, mc, 169)

def wheel_x_third(size):
    pos = mc.player.getPos()
    x, y, z = pos
    points = taxicab_circle_x(size)
    new_points = translate_points(points, x, y, z)
    set_points(new_points, mc, 168)

def wheel_axle():
    point = mc.player.getPos()
    x, y, z = point
    mc.setBlock(x, y, z, 57)

def cart():
    pos = mc.player.getPos()
    x, y, z = pos
    mc.setBlocks(x-2, y, z+16, x+2, y+3, z+21, 168)

def cart_2():
    pos = mc.player.getPos()
    x, y, z = pos
    mc.setBlocks(x-2, y, z-16, x+2, y+3, z-21, 168)

def cart_3():
    pos = mc.player.getPos()
    x, y, z = pos
    mc.setBlocks(x-2, y+15, z+2, x+2, y+19, z-3, 168)
def cart_4():
    pos = mc.player.getPos()
    x, y, z = pos
    mc.setBlocks(x-2, y-15, z+2, x+2, y-19, z-3, 168)


def make():
	wheel_middle(3)
	wheel_x_first(11)
	wheel_x_second(13)
	wheel_x_third(15)
	wheel_axle()
	cart()
	cart_2()
	cart_3()
	cart_4()

make()
