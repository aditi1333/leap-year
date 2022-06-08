
year = int(input("Which year do you want to check? "))
div_by_100 = year % 100
div_by_400 = year % 400
div_by_4 = year % 4

if div_by_100 ==0:
    if  div_by_400 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
elif div_by_4 == 0:
    print("Leap year")
else:
    print("Not a leap year")      
    
