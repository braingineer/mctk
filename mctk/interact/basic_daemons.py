'''
Some examples on how you can write daemons to check for 
different conditions
'''

import time
from mcpi2.minecraft import Minecraft


def chat_daemon(func):
	mc = Minecraft.create()
	while True:
		chats = mc.events.pollChatPosts()
		if len(chats) > 0:
			func(chats)
		else:
			time.sleep(0.1)

def pos_change_daemon(func):
	mc = Minecraft.create()
	pos = mc.player.getPos()
	while True:
		new_pos = mc.player.getPos()
		difference = pos - new_pos
		if difference.length() > 1:
			func(new_pos)
		else:
			time.sleep(0.1)