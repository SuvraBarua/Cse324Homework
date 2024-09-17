#The formula to convert celsius to fahrenheit = (clesius * (9/5) + 32
celsius = input("Temperature in celsius: ")
celsius = int(celsius)
fahrenheit = (celsius * (9/5)) +32
fahrenheit = str(fahrenheit)
print("The temperature in fahrenheit is: " + fahrenheit+"F")