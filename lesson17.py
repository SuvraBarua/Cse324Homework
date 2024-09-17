grocery_list  = ['egg', 'bread', 'rice', 'sugar']
print(grocery_list)
print(grocery_list[0])
print(grocery_list[1])
print(grocery_list[-1])
print(grocery_list[:2])
print(grocery_list[1:])
grocery_list[1] = 'oil'
print(grocery_list)

price = [5, 10, 15, 12, 1, 17, 3]
max = 0
for value in price:
	if value>max:
		max = value
print(max)
