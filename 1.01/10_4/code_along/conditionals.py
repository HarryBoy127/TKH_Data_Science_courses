# TODO: implement conditionals here
...

#list_numbers = (1, 2, 44, 1.1)
#for number in list_numbers: 
 #   if number % 2 == 0:
  #      print ("even numebr")

   # elif number % 2 ==1:
    #    print("odd")
    #else: 
     #   print ("decimal")

#value = float(input("write here"))
#if value < 0: 
 #   print(-value)
#else: 
 #   print(value)

#x=0 
#while x<=40:
 #   x+=2
  #  if x%20 == 0:
   #    print(x)

participants = 0
heard = 0

while True:
    if participants == 10:
	    break

    ans = input("Have you ever heard of product XYZ?")
    if ans == "no":
	    continue
    elif ans == "yes":
	    heard += 1
        participants += 1