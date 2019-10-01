groceries =  ["Apple", "Orange","Steak","Chicken"]
# check in or not in the list
if "Apple" in groceries:
    print("yes")
else:
    print("no")

if "Apple" not in groceries:
    print("yes")
else:
    print("no")

# age definding if else practice
age = 15
if age < 2 :
    print("Baby")
else:
    if age < 4 :
        print("Toddler")
    else :
        if age < 14 :
            print("Kid")
        else:
            if age < 20 :
                print("Teenager")
            else:
                if age < 65 :
                    print("Adult")
                else:
                    print("Elder")
# easier way to use elif insead of else: if
age = 30
if age < 2 :
    print("Baby")
elif age < 4 :
    print("Toddler")
elif age < 14 :
    print("Kid")
elif age < 20 :
    print("Teenager")
elif age < 65 :
    print("Adult")
else:
    print("Elder")

 

