# Store following word meanings in a python dictionary:
# table: "a piece of furniture", "list of facts & figures"
# cat: "a small animal"
dictionary={"table:""a piece of furniture","list of facts & figures"}
dictionary.add("cat:""a small animal")
print(dictionary)
#complete



# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# "python", "java", "C++", "python", "javascript",
# "java", "python", "java", "C++", "C"
# Output
set={"python", "java", "C++", "python", "javascript","java", "python", "java", "C++", "C"}
x=len(set)
print("number of classrooms needed by all students",x)
#complete



#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
ed={}
p=int(input("enter marks of physics:"))
ed.update({"physics":p})
c=int(input("enter marks of chemistry:"))
ed.update({"chemistry":c})
m=int(input("enter marks of maths:"))
ed.update({"maths":m})
print(ed)
#complete




