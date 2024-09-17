def total_cost():
    price_1 = 10
    shipping_1 = 5
    discount_1 = 1
    print(f"Total cost = ${price_1+shipping_1-discount_1}")
    
def total_cost_2(price, shipping, discount):
	print(f"Total cost = ${price+shipping-discount}")
	
def welcome(first_name, last_name):
	print(f"Hi, {first_name} {last_name}.")


total_cost()
total_cost_2(40, 10, 2)
total_cost_2(shipping = 10, price = 40, discount = 2)
welcome("Shuvro", "Barua")
