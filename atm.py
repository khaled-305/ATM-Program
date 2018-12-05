print("Welcome to my ATM machine")
print("Please swipe your card to start your transaction")
atm_pin = 9999
transaction = ["Balance enquiry", "Withdraw Money", "Deposit", "Change your pin", "Transfer Money", "Quit"]
pin = input("Enter your 4 digit code!")
if(pin == "0000"):
	print("choose your transaction:")
	print("1. Balance enquiry")
	print("2. Withdraw Money")
	print("3. Deposit")
	print("4. Change your pin")
	print("5. Transfer Money")
	print("6. Quit")
	trans = input("transaction:")

	if(trans == "Balance enquiry"):
		print("your Balance is #5000.000.000.000.00")
		slip = input("Do you want to print a slip?")
		if(slip == "yes"):
			print("Here is your slip.... Thank you for Banking with us")
		else:
			print("Thank you for Banking with us!")
	elif(trans == "Withdraw Money"):
		amount = input("Enter your amount to proceed:")
		if(amount>0):
			print("collect your cash, thank you for banking with us")
		else:
			print("Please enter a valid amount to proceed")
	elif(trans == "Deposit"):
		deposit = input("How much would you like to deposit?")
		if(deposit > 0):
			print("Your deposit was successful, thank you for banking with us")
		else:
			print("enter a valid amount to proceed")
	elif(trans == "Change your pin"):
		change_pin = input("enter a new pin:")
		if (change_pin >= 0):
			print("pin change was successful, thank you for banking with us")
		else:
			print("enter a valid pin to proceed")
	elif(trans == "Transfer Money"):
		transfer_money = input("Enter an amount to transfer")
		if(transfer_money >0):
			print("Your transaction was successful, thank you for banking with us")
		else:
			print("enter a valid amount to proceed")
	elif(trans == "Quit"):
		quit_l = input("press yes to Quit!")
		if (quit_l == "yes"):
			print("Quit")
		else:
			print("choose another transaction")
else:
	print("wrong pin, try again")
