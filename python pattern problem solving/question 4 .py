'''
    *
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''
for s in range (0 , 5 ) :
    for p in range (0, 4-s ) :
        print (" " , end = '')
    for p in range ( 0 , s+1 ):
        print ("*","", end = "")
    print ()
for s in range ( 6 , 11 ) :
    for p in range (0,s-6  ):
        print (" " , end ='')
    for p in range (6 , 17-s ) :
        print ("*" ,'', end ='')
    print ()

    
             

