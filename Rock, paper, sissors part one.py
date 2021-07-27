 # am tryna create the popular rock, paper, sissors game.
user_one_name = input ("Hey! You player one. What is your name? ")
user_two_name = input ("Hey! You player two . What is your name? ")
print()
user_one = input (f"{user_one_name} chose. Rock, paper, sissors? ").lower()
user_two = input (f"{user_two_name} chose. Rock, paper, sissors? ").lower()
print()
if user_one == "rock" or "rock " and  user_two == "paper" or "paper ":
    print (f"{user_two_name} wins. ")
elif user_one == "rock" or "rock " and  user_two == "sissors" or "sissors ":
    print (f"{user_one_name} wins. ")
elif user_one == "paper" or "paper " and user_two == "sissors " or "sissors": 
    print (f"{user_two_name} wins. ")
elif user_one == "paper" or "paper " and user_two == "rock " or "rock": 
    print (f"{user_one_name} wins. ")
elif user_one == "sissors " or "sissors " and user_two == "rock " or "rock": 
    print (f"{user_two_name} wins. ")
elif user_one == "sissors " or "sissors " and user_two == "paper " or "paper": 
    print (f"{user_one_name} wins. ")

elif user_two == "rock" or "rock " and  user_one == "paper" or "paper ":
    print (f"{user_one_name} wins. ")
elif user_two == "rock" or "rock " and  user_one == "sissors" or "sissors ":
    print (f"{user_two_name} wins. ")
elif user_two == "paper" or "paper " and user_one == "sissors " or "sissors": 
    print (f"{user_one_name} wins. ")
elif user_two == "paper" or "paper " and user_one == "rock " or "rock": 
    print (f"{user_two_name} wins. ")
elif user_two == "sissors " or "sissors " and user_one == "rock " or "rock": 
    print (f"{user_one_name} wins. ")
elif user_two== "sissors " or "sissors " and user_one== "paper " or "paper": 
    print (f"{user_one_name} wins. ")





