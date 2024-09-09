from os import replace


name = input("Enter your name :")
print(f"Good Morning {name}")

letter = '''Dear <name> 
you are selected
<date>
'''

print(letter.replace("<name>","Tanish").replace("<date>","12/3/2005"))

str = input("Enter string : ")

print(str.find("  "))
print(str.replace("  "," "))