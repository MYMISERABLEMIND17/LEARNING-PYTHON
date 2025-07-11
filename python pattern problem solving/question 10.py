'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

nums ="12345"
for row in range (0 , 6) :
    for col in range (0,5-row ) :
        print (nums[col] , end= ' ')
    print ()



