
string1 = "Vagetable"
string2 = "vagetable"

print(string1 == string2)

print(string1 != string2)

if string1.lower() == string2.lower():
    print("the strings are equal!")
else:
    print("the strings are not equal!")

# if else practice(true or fales)

number1 = 25
number2 = 30

if number1 > number2:
    print("number1 is greater")
else:
    print("number2 is greater")

name_1 = "Paul"
name_2 = "Tommy"

number_1 = 30
number_2 = 30
# and or differentce
if name_1 == name_2 and number_1 == number_2:
    print("True")

if name_1 == name_2 or number_1 == number_2:
    print("True")
