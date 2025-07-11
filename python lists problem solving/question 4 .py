'''
Program to interchange first and last elements in a 
list
'''
list = [2 , 4 , 6 , 8 , 10 ]
first =list.pop(0)
last = list.pop(-1)
list.insert (-1,first)
list .insert  (0, last )
print (list )