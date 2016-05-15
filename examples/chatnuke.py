import mctk


def nuke_trigger():

	def func(chats):
		for chat in chats:
			if chat.message == "nuke":
				print("nuking now!")
				mctk.utils.clear_by_player(40)
				print("nuked!")
				
	mctk.interact.chat_daemon(func)

if __name__ == "__main__":
	nuke_trigger()