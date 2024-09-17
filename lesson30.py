class Keyboard:
	def __init__(self, language, connection):
		self.language = language
		self.connection = connection
	def definition(self):
		print("The keyboard is an input device")
	def number_of_keys(self):
		print("My keyboard has 114 keys")

my_keyboard = Keyboard('English', 'wired')
print(my_keyboard.language)
print(my_keyboard.connection)

class AboutMe:
	def __init__(self, name, address, occupation):
		self.name = name
		self.address = address
		self.occupation = occupation
	def talk(self):
		print(f"My name is {self.name}, I live in {self.address} And I am a {self.occupation}")

shuvro = AboutMe("Shuvro Barua", "Bangladesh", "Student")
shuvro.talk()
