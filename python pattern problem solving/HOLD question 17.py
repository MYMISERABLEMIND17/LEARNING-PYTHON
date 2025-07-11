'''
*        *   
**      **   
***    ***   
****  ****   
**********   
**********
****  ****
***    ***
**      **
*        *
'''
for row  in range (1 , 6 ) :
    for col in range (1,1+row):
       print ("*" , end = '')
    print ()
for row in range (6 , 11) :
    for col in range ( 0 , 11-row ):
        print ("*" , end = '') 
    print ()












