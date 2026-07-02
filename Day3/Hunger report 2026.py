# ================================
# MY DAILY FOOD ADVISOR
# ================================
name = input("Enter your name: ")
food = input("What are you craving today? pulao/chicken handi/karahi/biryani/nihari: ")
hunger = int(input("Enter your hunger level from 1 to 10: "))
if hunger < 3:
    print("Alert: You don't seem very hungry. A light snack might be enough.")
if hunger >= 5:
    print("You're hungry enough for a full, meal!")
else:
    print("Maybe go for a small portion or something light.")
if food == "burger":
    advice = "Great choice! burger goes perfectly with cheese sauce and katchup."
elif food == "Beaf tikka":
    advice = "Beaf tikka is best with rice — best enjoyed with paratha and ketchup."
elif food == "kunna":
    advice = "Kunna is spicy and full of flavor, perfect with roti or naan."
elif food == "biryani":
    advice = "Biryani is a classic! Pair it with raita to balance the spices."
else:
    advice = "Any food is good food! Enjoy whatever you're having today."

import datetime
today = datetime.datetime.now()

print("================================")
print("DAILY FOOD ADVISOR REPORT")
print("================================")
print("Name:", name)
print("Food Craving:", food)
print("Hunger Level:", hunger)
print("Date and Time:", today)
print("Advice:", advice)
print("================================")