city= input("enter your city name")
temp= float(input("enter todays temp"))


if temp > 35:
 print("stay inside")

elif temp > 15:
 print("Nice weather to play outside")
 
elif temp > 10:
  print("wear hot cloaths / jackets")

elif temp > 5 :
  print ("Be safe")

else :
  print("stay at home")

import calendar
print(calendar.calendar(2026))