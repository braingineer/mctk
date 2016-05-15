from mcpi2.minecraft import Minecraft
from mctk.utils import every_arc
from mctk.build import *


def circlesquared(radius):
    mc = Minecraft.create()
    x,y,z = mc.player.getPos()
    def func(xn, zn):
        tunnel_z(1, radius//5, mc, (x+xn, y, z+zn), 57)
        tunnel_x(1, radius//5, mc, (x+xn, y, z+zn), 57)
    every_arc(30, func, radius)
    def func(xn, zn):
        tunnel_z(1, radius//5, mc, (x+xn, y+zn, z), 57)
        tunnel_x(1, radius//5, mc, (x+xn, y+zn, z), 57)
    every_arc(30, func, radius)
    def func(xn, zn):
        tunnel_z(1, radius//5, mc, (x, y+zn, z+xn), 57)
        tunnel_x(1, radius//5, mc, (x, y+zn, z+xn), 57)
    every_arc(30, func, radius)

def lava_columns(radius=10, width=2, height=20, offset=None,
                                     outter=20, inner=10, rate=12):
    mc = Minecraft.create()
    p = mc.player
    pos = p.getPos()
    offset = offset or (0,0,0)
    xoff, yoff, zoff = offset
    x,y,z = pos
    def func(xn, zn):
        filled_y(height, width, mc, (x+xn+xoff, y+yoff, z+zn+zoff), outter)
        #sleep(0.25)
        filled_y(height-2, width-1, mc, (x+xn+xoff, y+1+yoff, z+zn+zoff), inner)
    every_arc(rate, func, radius)
    for ydiff in range(0, height, 5):
        filled_y(1, radius-1, mc, (x+xoff, y+ydiff+yoff, z+zoff), outter)


def tree():
    mc = Minecraft.create()
    p = mc.player
    pos = p.getPos()
    tunnel_y(35, 10, mc, pos)
    x,y,z = pos
    for h in range(5,35,5):
        for offset in [10, -19]:
            xsidepos = (x+offset, y+h, z)
            tunnel_x(10, 3, mc, xsidepos, 17)
            tunnel_x(10, 2, mc, xsidepos, 0)
            tunnel_x(10, 1, mc, xsidepos, 0)
            #tunnel_x(10, 0, mc, xsidepos, 0)


            zsidepos = (x, y+h, z+offset)
            tunnel_z(10, 3, mc, zsidepos, 17)
            tunnel_z(10, 2, mc, zsidepos, 0)
            tunnel_z(10, 1, mc, zsidepos, 0)
            #tunnel_z(10, 0, mc, zsidepos, 0)
        print("iteration", h)
    tunnel_y(1, 10, mc, (x,y+35,z), 20)
    #sleep(0.1)

if __name__ == "__main__":
    lava_columns()