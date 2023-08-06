musicalyaccounts = ["test", "tma.0000001"]

class information():
	def version():
		print("TikOt API for all platforms")
	def ver_musicaly():
		print("TikOt API 1.0.7. TikOt Musicaly API 1.0.0")

class musicaly():
	tokens = ["token.09877!!!@@@###$$$^^^&&&***((("]
	def account(artistid):
		if artistid == musicalyaccounts[0]:
			print("Hello TikOt!")
			print("Your tracks:\nShort chill")
		elif artistid == musicalyaccounts[1]:
			print("Hello, user!")
			print("This account for testing api!")
	def version():
		print("TikOt Musicaly API 1.0.0")

	def tutorial():
		print("Hello! Your join on tutorial for TikOt Musicaly API!")
		print("musicaly.account(tma.id) - Login on account artist")
		print("more on: tikotmusicalyapi.7m.pl")