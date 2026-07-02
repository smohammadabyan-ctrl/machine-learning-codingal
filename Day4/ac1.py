for i in range(1,21,4):
 print(f" 23 x {i} ={23*i}")



 n = int(input("enter the number of rows"))
 for i in range(n):
  for j in range (i+1):
   print('$',end= '')
  print()

  total_sum = 0
  num = 1
  while num <= 10:
   total_sum += num
   num += 1
   print(f"The sum of the first ten number is {total_sum}")