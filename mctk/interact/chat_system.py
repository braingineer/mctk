
import time
from mcpi2.minecraft import Minecraft

class Chat:
	def __init__(self, mc=None):
		if mc is None:
			mc = Minecraft.create()
		self.mc = mc
		self.listeners = {}
		self.constants = {}
		self.add_help_listener()


	def run(self):
		while True:
			self.notify_constants()
			chats = self.mc.events.pollChatPosts()
			if len(chats) > 0:
				self.notify_listeners(chats)
			else:
				time.sleep(0.1)

	def add_help_listener(self):
		def func(daemon, message):
			message = message.split(" ")
			if message[0] == "help":
				self.mc.postToChat("Chat Trigger Menu")
				for trigger in self.listeners.keys():
					self.mc.postToChat("- [{}]".format(trigger))
		self.register_listener("help", func)

	def register_listener(self, trigger, func):
		if trigger in self.listeners:
			self.listeners[trigger].append(func)
		else:
			self.listeners[trigger] = [func]

	def notify_listeners(self, chats):
		# check all of the chats
		for chat in chats:
			# get the actual message
			message = chat.message
			# go through each trigger and function list
			for trigger, funcs in self.listeners.items():
				# see if the trigger is in what was said
				if trigger in message:
					print("Notifying for {}".format(trigger))
					# if it is, then notify all of the functions
					for func in funcs:
						func(self, message)

	def add_constant(self, name, func):
		self.constants[name] = func

	def remove_constant(self, name):
		if name in self.constants:
			del self.constants[name]

	def notify_constants(self):
		for func in self.constants.values():
			func()

def chat_daemon(func):
	mc = Minecraft.create()
	while True:
		chats = mc.events.pollChatPosts()
		if len(chats) > 0:
			func(chats)
		else:
			time.sleep(0.1)