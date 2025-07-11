'''
1
12
123
1234
12345
123456
1234567
12345678
123456789
'''
nums = "123456789"
for row in range (0 , len(nums)) :
    for col in range (0 , row +1 ) :
        print (nums[col] , end = " ")
    print ()