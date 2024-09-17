actual_price = 10
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
	guess = int(input("Enter your guess: "))
	guess_count += 1
	if guess == actual_price:
		print("You've won!")
		break
else:
    print("You've failed")
