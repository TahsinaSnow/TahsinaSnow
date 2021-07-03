y = int (input("Enter a year:"))
#removes the last two zeros

if y%100==0:
    y = y/100
    if y%4==0:
        print("Leap year")
    else:
        print("Not leap year")

    
else:

    if y%4==0:
        print("Leap year")

    else: 
          print("Not leap year")
