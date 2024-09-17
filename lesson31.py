class Laptop:
	def parts(self):
		print("display, keyboard, motherboard")
my_laptop = Laptop()
my_laptop.parts()

class Desktop(Laptop):
	print("Desktops are heavy-weighted")

my_desktop = Laptop()
my_desktop.parts
