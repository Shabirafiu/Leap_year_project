#year = int(input("Which year do you want to check ?:"))

#if year % 4 ==0:
#    print("This is A LEAP YEAR ")
#elif year % 100 ==0:
#    print("This is A LEAP YEAR ")
#elif year % 400 ==0:
#    print("This is A LEAP YEAR ")
#else:
 #   print("Not A LEAP YEAR ")


#                      OR


year = int(input("Which year do you want to check? "))

if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("Leap year.")
        else:
            print("Not leap year")
    else:
        print("Not leap year")
else:
    print("Not leap year")
