'''
1
22
333
4444
55555
'''
str = "12345"
for row in range ( 0 , 5  ) :
    for col in range (0 , row+1 ) :
        print (str[row], end =" ")
    print ()