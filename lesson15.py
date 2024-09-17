for character in ‘python’:
	print(character)
for item in ['rice', 'jute', 'sugarcane', 'apple', 'pineapple']:
	print(item)
for number in [1, 2, 3, 4, 5]:
	print(number)
for number in range(5, 10, 2):
	print(number)
bills = [10, 30, 50, 10]
total = 0
for bill in bills:
	total += bill
print(f"total bill: ${total}")
