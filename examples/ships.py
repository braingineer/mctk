import mctk
from mcpi2.minecraft import Minecraft
from mcpi2 import block

def spawn_ship():
	mc = Minecraft.create()
	x,y,z = mc.player.getPos()
	y-=5
	mctk.build.pirateShipGen(x,y,z,block.WOOD, block.WOOL, block.DIAMOND_BLOCK)
	mc.player.setPos(x+3,y+10,z)


def armada(n=10):
	mc = Minecraft.create()
	x,y,z = mc.player.getPos()
	x += 30
	z -= n//2 * 20
	for i in range(n):
		mctk.build.pirateShipGen(x,y,z,block.WOOD, block.WOOL, block.DIAMOND_BLOCK)
		z += 20

if __name__ == "__main__":
	spawn_ship()