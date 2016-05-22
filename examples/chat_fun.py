import mctk
from mcpi2.minecraft import Minecraft

def forward():
	mc = Minecraft.create()
	x,y,z = mc.player.getPos()
	xd,yd,zd = mc.player.getDirection()
	mctk.utils.clear_region(x+xd*100,y,z+zd*100,100)

def nuke_trigger():

	def func(chats):
		for chat in chats:
			print("seeing a chat")
			if chat.message == "nuke":
				print("nuking now!")
				mctk.utils.clear_by_player(40)
				print("nuked!")
			elif chat.message == "forward":
				print("got forward")
				forward()
				
	mctk.interact.chat_daemon(func)

if __name__ == "__main__":
	nuke_trigger()