import mctk
from mcpi2.minecraft import Minecraft
import time
import math

def nuke_action(daemon, message):
	message_split = message.split(" ")
	if len(message_split) > 1:
		if message_split[1].isdigit():
			size = int(message_split[1])
		else:
			size = 30
		mctk.utils.clear_by_player(size)

def tnt_vision(daemon, message):
	mc = daemon.mc
	message_split = message.split(" ")
	if len(message_split) == 1:
		mc.postToChat("specify on or off!!")
		return
	if message_split[1] == "on":
		def func():
			x,y,z = mc.player.getPos()
			xd,yd,zd = mc.player.getDirection()
			mc.setBlock(x+10*xd, y-2, z+10*zd, 17)
			mc.setBlock(x+10*xd, y-1, z+10*zd, 76)
			mc.setBlock(x+10*xd, y, z+10*zd, 46, 1)
			mc.setBlock(x+10*xd, y-2, z+10*zd,0)
		daemon.add_constant("tnt_vision", func)
	elif message_split[1] == "off":
		daemon.remove_constant("tnt_vision")

def tunnels_for_days(daemon, message):
	message_split = message.split(" ")
	if len(message_split) == 1:
		mc.postToChat("specify on or off!!")
		return
	if message_split[1] == "on":
		def func():
			mc = daemon.mc
			x,y,z = mc.player.getPos()
			xd,yd,zd = mc.player.getDirection()
			if abs(xd)<abs(zd):
				mctk.build.tunnels.tunnel_z(1,3,mc, block=(95,14))
			else:				
				mctk.build.tunnels.tunnel_x(1,3,mc, block=(95,14))
		daemon.add_constant('tunnels', func)
	elif message_split[1] == "off":
		daemon.remove_constant('tunnels')

def castle(daemon, message):
	mc = daemon.mc
	x,y,z = mc.player.getPos()
	print(message)
	message = message.split(" ")
	try:
		W = int(message[1])
		H = int(message[2])
		wall(mc, (x+W//2,y,z), W, 2, H, 'z')
		wall(mc, (x,y,z+W//2), W, 2, H, 'x')
		wall(mc, (x-W//2,y,z), W, 2, H, 'z')
		wall(mc, (x,y,z-W//2), W, 2, H, 'x')
	except Exception as e:
		print("failed", e)


def wall(mc, pos, length, width, height, axis='x', block=89):
	x,y,z = pos
	if axis=='x':
		mc.setBlocks(x-length//2, y, z-width//2, x+length//2, y+height, z+width//2, block)
		for i in range(0, length, 3):
			mc.setBlock(x-length//2+i, y+1+height, z, block)
	else:
		mc.setBlocks(x-width//2, y, z-length//2, x+width//2, y+height, z+length//2, block)
		for i in range(0, length, 3):
			mc.setBlock(x, y+1+height, z-length//2+i, block)

def forced_tunnel(daemon, message):

	message_split = message.split(" ")
	if len(message_split) == 1:
		mc.postToChat("specify on or off!!")
		return
	if message_split[1] == "on":
		facing = 1
		if len(message_split) == 3:
			if message_split[2] == "backward":
				facing = -1

		def func():
			mc = daemon.mc
			x,y,z = mc.player.getPos()
			xd,yd,zd = mc.player.getDirection()
			if abs(xd)<abs(zd):
				if zd > 0:
					zd = math.ceil(zd)*facing
				else:
					zd = math.floor(zd)*facing
				mctk.build.tunnels.tunnel_z(1,3,mc, block=(95,14))
				mc.setBlocks(x-1,y-1,z+zd,x+1,y+2,z+zd*3,0)
				mc.player.setPos(x,y,z+zd)

			else:			
				if xd > 0:
					xd = math.ceil(xd)*facing
				else:
					xd = math.floor(xd)*facing
				mctk.build.tunnels.tunnel_x(1,3,mc, block=(95,14))
				mc.setBlocks(x+xd,y-1,z-1,x+xd*3,y+2,z+1,0)
				mc.player.setPos(x+xd,y,z)
			
		daemon.add_constant('forcedtunnels', func)
	elif message_split[1] == "off":
		daemon.remove_constant('forcedtunnels')


def run():
	daemon = mctk.interact.Chat()
	daemon.register_listener('nuke', nuke_action)
	daemon.register_listener('tntvision', tnt_vision)
	daemon.register_listener('tunnels', tunnels_for_days)
	daemon.register_listener('forcedtunnel', forced_tunnel)
	daemon.register_listener('castle', castle)
	daemon.run()

if __name__ == "__main__":
	run()