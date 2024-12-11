#age
def boys_age():
  age = 23
  if age >= 30:
    print("The person is an adult")
  elif age >= 25:
    print("The person is in his mid twenties")
  else:
    print("The person is in his early twenties\n")

boys_age()



#Grade point
def grade_point():
  Grades = [90, 40, 50, 78, 34, 15, 55, 48, 59, 69, 35, 20]
  for grade in Grades:
    if grade >= 75:
      print("Congrats! You got an A\n")
    elif grade >= 60:
      print("Congrats! You got a B\n")
    elif grade >= 50:
      print("You got a C, try harder next time\n") 
    elif grade >= 35:
      print("You got a D, You barely passed\n") 
    elif grade >= 20:
      print("You got an E, sorry for you oo!\n")
    else:
      print("you're such a failure to mankind\n")
      
grade_point()




#Alien color for just "if statement"
def first_color():
  Alien_color = "green"
  if Alien_color == "green":
    print("You've just earned yourself five points")
  Alien_color = "red"

first_color()


#Alien color for just "if statement" 
def second_color():
  Alien_color = "green"
  if Alien_color == "green":
    print("You've just earned yourself five points")
  else:
    print("You've just earned yourself ten points")

  Alien_color = "black"
  if Alien_color != "green":
    print("You've just earned yourself ten points")

second_color()


#Alien color for "if_else" 
def third_color():
  Alien_color = "green"
  if Alien_color == "green":
    print("You've just earned yourself five points")
  else:
    print("you've just earned yourself ten points")

  Alien_color = "red"
  if Alien_color == "red":
    print("You've just earned yourself fifteen points")
  else:
    print("you've just earned yourself five points")

  Alien_color = "yellow"
  if Alien_color == "yellow":
    print("You've just earned yourself ten points")
  else:
    print("you've just earned yourself fifteen points")


third_color()


#Alien color for "if_elif_else"
def third_color():
  Alien_color = "red"
  if Alien_color == "yellow":
    print("You've just earned yourself ten points")
  elif Alien_color == "green":
    print("You've just earned yourself five points")
  else:
    print("you've just earned yourself fifteen points")

  Alien_color = "green"
  if Alien_color == "yellow":
    print("You've just earned yourself ten points")
  elif Alien_color == "green":
    print("You've just earned yourself five points")
  else:
    print("you've just earned yourself fifteen points")

  Alien_color = "red"
  if Alien_color == "yellow":
    print("You've just earned yourself ten points")
  elif Alien_color == "green":
    print("You've just earned yourself five points")
  else:
    print("you've just earned yourself fifteen points\n")

third_color()

#Stages of life
def life_stage():
  age = 24
  if age < 2:
    print("The person is a baby")
  elif age < 4:
    print("The person is a toddler")
  elif age < 13:
    print("The person is a kid")
  elif age < 20:
    print("The person is a teenager")
  elif age < 65:
    print("The person is an adult\n")
  else:
    print("The person is an elder")

life_stage()

#Favourite fruit
def fruits():
  favourite_fruit = ["Avocado", "Apricot", "Pear", "Apple", "Banana", "Kiwi"]
  if "Banana" in favourite_fruit:
    print(f"{favourite_fruit[-2]} is my least favourite")
  else:
    print("I love all fruits")
  
  favourite_fruits = ["Apple", "Strawberry", "Raspberry"]
  if "Apple" in favourite_fruits:
    print("You love Apples that much?!")

  if "Guava" in favourite_fruits:
    print("You really love guava")
  else:
    print("I dont see guava on your list, it seems you dont like it")
  
  if "Grapes" not in favourite_fruits:
    print("Grape is not one of my favourite")

  if "Banana" in favourite_fruits:
    print("I love banana because of smoothies")

  if "Watermelon" in favourite_fruits:
    print("I just love watermelon")
  else:
    print("watermelon is overhyped, its just filled with water as the name implies")

  for fruit in favourite_fruits:
    if fruit == "Banana":
      print(fruit.upper())
    else:
      print(fruit.lower())

  for fruit in favourite_fruits:
    if fruit == "Strawberry":
      print(fruit.upper())
  else:
      print(fruit.lower())

fruits()

