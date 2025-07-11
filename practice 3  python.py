set={1,2,2,3,4,5,6,7,7,6,5,4,}
print(set)#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
x=(input("your 1st favourite movie:"))
y=(input("your 2nd favourite movie:"))
z=(input("your 3rd favourite movie:"))
list=[x,y,z]
print("list=",list)
#complete


# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
# [1, 2, 3, 2, 1]
# [1 "abc", "abc", 1]
# part (a)
x=[1,2,3,2,1,]
p=list.sort()
print(p)
q=list.sort(reverse=True)
print(q)
if(p==q):
  print("list is palindrome")
else:
  print("list is not palindrome")
 #part(a) complete 

#part(b)
# z=[1, "abc", "abc", 1,]
# q=list.sort(z)
# print(q)
# d=list.sort(reverse=True)
# print(d)
# if(q==d):
#   print("list is palindrome")
# else:
#   print("list is not palindrome")
#mistake   =  code galat hai kyoki strings aa gayi

z=[1,"abc","abc",1]
copy_z=z.copy()
copy_z.reverse()
if(copy_z==z):
  print("list is palindrome")
else:
  print("list is not palindrome")
 
#complete


  
# WAP to count the number of students with the "A" grade in the following tuple.
# ["C", "D", "A", "A", "B", "В", "A"]
tup=["C", "D", "A", "A", "B", "В", "A"]
x=tup.count("A")
print(x)
#complete


#["C", "D", "A", "А", "В", "В", "A"]
#Store the above values in a list & sort them from "A" to "D".
s=["C", "D", "A", "А", "В", "В", "A"]
s.sort()
print(s)


