#Greeting users
def greet_user():
  usernames = ['delly', 'brad01', 'cocoonly', 'kappakappa', 'admin', 'alder333']
  for username in usernames:
    if username == 'admin':
      print(f"Hello {usernames[-2]}, would you like to see a status report?")
    else:
      print(f"Hello {username}, Thank you for logging in again")
greet_user()

#Checking for no user
def no_user():
  usernames = []
  if usernames:
    for username in usernames:
      print("Hello! Thank you for logging in")
  else:
    print("We need to find some users")

no_user()

#Website users
def web_users():
  current_users = ['delly', 'brad01', 'cocoonly', 'kappakappa', 'admin', 'alder333']
  new_users = ['brad01', 'delilah4ever','admin','jobbamanny', 'rey666']
  for new_user in new_users:
    if new_user in current_users:
      print("Sorry! This username has already been used. Please enter another username")
    else:
      print("This username is available for use")

web_users()

#Ordinal numbers
def ordinal_numbers():
  numbers = list(range(1, 10))
  for number in numbers:
    if number == 1:
      print(f"{number}st")
    elif number == 2:
      print(f"{number}nd")
    elif number == 3:
      print(f"{number}rd")
    else:
      print(f"{number}th")

ordinal_numbers()

