import mctk


def print_chats():

	def func(chats):
		for chat in chats:
			print(chat)

	mctk.interact.chat_daemon(func)

if __name__ == "__main__":
	print_chats()