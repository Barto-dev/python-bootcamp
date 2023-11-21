year = int(input("Which year do you want to check? "))

evenly_divisible_by_4 = year % 4 == 0
evenly_divisible_by_100 = year % 100 == 0
evenly_divisible_by_400 = year % 400 == 0

if evenly_divisible_by_4:
  if not evenly_divisible_by_100:
    print("Leap year.")
  elif evenly_divisible_by_400:
    print("Leap year.")
  else:
    print("Not leap year.")
else:
  print("Not leap year.")