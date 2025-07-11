# # Get the character at position 1 (remember that the first character has the position 0):
# a = "Hello, World!"
# print(a[1])

# # The len() function returns the length of a string:
# a = "Hello, World!"
# print(len(a))

# # Check if "free" is present in the following text:
# txt = "The best things in life are free!"
# print("free" in txt)

# # Print only if "free" is present:
# txt = "The best things in life are free!"
# if ("free" in txt):
#     print("yes","it is present ")

# # Check if "expensive" is NOT present in the following text:
# txt = "The best things in life are free!"
# if ("expensive" in txt):
#     print("true")
# else:
#     print('false,expensive is not present in txt ')

# # Get the characters from position 2 to position 5 (not included):
# b = "Hello, World"
# print(b[2:6])

# # Get the characters from position 2, and all the way to the end:
# b = "Hello, World!"
# print(b[2:])

# # The upper() method returns the string in upper case:
# a = "Hello, World!"
# print(a.upper())

# # The lower() method returns the string in lower case:
# a = "Hello, World!"
# print(a.lower())

# # The replace() method replaces a string with another string:
# a = "Hello, World!"
# print(a.replace("o","p"))

# # The split() method splits the string into substrings if it finds instances of the separator:
# a = "Hello, World!"
# print(a.split(","))

# # To add a space between them, add a " ":
# a = "Hello"
# b = "World"
# c = a + " " + b
# # print(c)

# # Create an f-string:
# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

# # Add a placeholder for the price variable:
# price=10
# text=f"price of samosa is, {price} rs "
# print(text)

# # Display the price with 2 decimals:
# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# # Perform a math operation in the placeholder, and return the result:
# text=f"the price of item is {60+40+9-0} rs"
# print(text)

# # The escape character allows you to use double quotes when you normally would not be allowed:
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value


# # Print the second item of the list:
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])


# # Print the last item of the list:
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# # Return the third, fourth, and fifth item:
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])



# # This example returns the items from the beginning to, but NOT including, "kiwi":
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[0:4]),print(thislist[5:7])

# # This example returns the items from "cherry" to the end:
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# # this example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])\

# # Check if "apple" is present in the list:
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#     print("apple is present in the list")

# # Change the second item:
# thislist = ["apple", "banana", "cherry"]
# thislist[1]= "grapes"
# print(thislist)

# # Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3]= ["blackcurrant", "watermelon"]
# print(thislist)

# # Change the second value by replacing it with two new values:
# thislist = ["apple", "banana", "cherry"]
# thislist[1] ="grapes","watermelon"
# print(thislist)

# # Change the second and third value by replacing it with one value:
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3]=["mango"]
# print(thislist)

# # Insert "watermelon" as the third item:
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))
# thislist.insert( 2 ,"mango")
# print(thislist)
# print(len(thislist))

# # Using the append() method to append an item:
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# # Add the elements of tropical to thislist:
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# # Add elements of a tuple to a list:
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# # Remove "banana":
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("apple")
# print(thislist)

# # Remove the first occurrence of "banana":
# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# # Remove the second item:
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# # Remove the first item:
# thislist = ["apple", "banana", "cherry"]
# del thislist[1]
# print(thislist)

# # Delete the entire list:
# thislist = ["apple", "banana", "cherry"]
# del thislist

# # Clear the list content:
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# # Print i as long as i is less than 6:
# i=1
# while i<=6:
#     print(i)
#     i+=1

# # One line if else statement:
# a = 2
# b = 330
# print("A") if a > b else print("B")

# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")


# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# if a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# # One line if else statement:
# a = 2
# b = 330
# print("A") if a > b else print("B")

# # Test if a is greater than b, AND if c is greater than a:
# a = 200
# b = 33
# c = 500
# if c>a and  c>b :
#     print("both are true conditions ")

# # Test if a is greater than b, OR if a is greater than c:
# a = 200
# b = 33
# c = 500
# if a>b or a>c :
#     print("sahi hai ")

# # Test if a is NOT greater than b:
# a = 33
# b = 200
# if not a>b :
#     print("a is NOT greater than b")

# a = 33
# b = 200
# if b > a:
#   pass


# # Use an if statement to print "YES" if either a or b is equal to c.
# a = 2
# b = 50
# c = 2
# if a == c or b ==c  :
#   print("YES")

# WHILE LOOP

# # Print i as long as i is less than 6:
# i=1
# while i<=6:
#     print(i)
#     i+=1

# # Exit the loop when i is 3:
# i=1
# while i<=9:
#    print(i)
#    if i==3: 
#     break
#    i+=1

# # Continue to the next iteration if i is 3:
# i=0 
# while i<=10:
#     i+=1
#     if i==3:
#         continue 
#     print (i)

# # Print a message once the condition is false:
# i=0
# while i<=10:
#     i+=1
#     print(i)
# if i>=9:
#     print("the number is greater than 10")

# # Create a Tuple:
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# # Print the number of items in the tuple:
# thistuple = ("apple", "banana", "cherry","banana")
# print(len(thistuple))

# # Using the tuple() method to make a tuple:
# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# # Print the second item in the tuple:
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# # Print the last item of the tuple:
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# # Return the third, fourth, and fifth item:
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# # This example returns the items from the beginning to, but NOT included, "kiwi":
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[0:4]), print(thistuple[5:7])

# # This example returns the items from "cherry" and to the end:
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])

# # This example returns the items from index -4 (included) to index -1 (excluded)
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# # Check if "apple" is present in the tuple:
# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple :
#    print("apple is present ")

# # Convert the tuple into a list to be able to change it:
# x = ("apple", "banana", "cherry")
# z=list(x)
# z[2]="kiwi"
# x=tuple(z)
# print(z)

# # Convert the tuple into a list, add "orange", and convert it back into a tuple:
# thistuple = ("apple", "banana", "cherry")
# x=list(thistuple)
# x.append("yellow banana")
# thistuple=tuple(x)
# print(thistuple)

# # Create a new tuple with the value "orange", and add that tuple:
# thistuple = ("apple", "banana", "cherry")
# z=("orange",)
# print(type(z))
# thistuple += z
# print(thistuple)

# # Unpacking a tuple:
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# # Assign the rest of the values as a list called "red":
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

# # Add a list of values the "tropic" variable:
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (*tropica,green ) = fruits
# print (tropica)
# print(green)

def my_function():
  print("Hello from a function")
my_function()




































































