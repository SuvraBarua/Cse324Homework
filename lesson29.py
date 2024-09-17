class Keyboard:
	def definition(self):
		print("The keyboard is an input device")
	def number_of_keys(self):
		print("My keyboard has 114 keys")


my_keyboard = Keyboard()
my_keyboard.definition()
my_keyboard.number_of_keys()
my_keyboard.brand = "Havit"
print(my_keyboard.brand)

new_keyboard = Keyboard()
new_keyboard.definition()
new_keyboard.brand = "Dell"
print(new_keyboard.brand)
