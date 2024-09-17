good_condition = True
reasonable_price = False
poor_foundation = False

if good_condition and reasonable_price:
    print('We will buy the house')
if good_condition or reasonable_price:
    print('We are interested')
if good_condition and not poor_foundation:
    print("It's a very good deal")
