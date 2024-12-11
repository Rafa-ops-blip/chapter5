#comparison of strings
def car_type():
  car = 'Audi'
  print(car)
  print(car == "mercedes")
  print(car == "audi")
  print(car != "Audi")
  print(car.lower() == "audi")
  print(car.upper() == "audi")
  print(car.upper() != "AUDI")
  print(car.upper() == "AUDI")

car_type()



#comparison of numbers
def number():
  score = 50
  print(score >= 60)
  print(score <= 50)
  print(score != 50)
  print(score == 50)

number()


#comparing more than one entity using "or" and "and"
def two_people():
  age_1 = 10
  age_2 = 20
  print(age_1 >= 11 or age_2 <= 19)
  print(age_1 <= 20 and age_2 <= 30)

  age = 40
  print(age >= 60)
two_people()


#checking if a value is in a list or not

def compare_food():
  desired_food = ["chicken biryani", "masa and catfish peppersoup", "grilled chicken", "yamarita"]
  if "pancakes" in desired_food:
    print("You have a great menu")
  else:
    print("Sorry, I won't be patronizing you")

  favourite = "masa and goat meat peppersoup"
  if favourite not in desired_food:
    print(f"Sad! I would have loved to eat {favourite}")

  if favourite in desired_food:
    print(True)
  else:
    print(False)

  print("chicken biryani" != desired_food)
  print("masa and goat meat peppersoup" == favourite)
  print(favourite != "masa and goat meat peppersoup")

compare_food()

