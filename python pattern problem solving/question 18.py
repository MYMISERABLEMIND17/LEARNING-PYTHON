'''
1
2 1
1 2 3
4 3 2 1
1 2 3 4 5
'''
n=5
nums = int(12345)
for row  in range (0 , 6) :
    for col in range (1,row+1) :
        if (row==1 or row==3 or row==5)  :
           print (col, end = " ")
    for col in range (0, row) :
        if (row ==2 or row==4 ) :
           print (row-col ,end =" " )
    print ()