'''
       **  
      *  *
     *    * 
    *      *
    *      *
     *    * 
      *  *
       **
'''
for row in range (1 , 9 ) :
    for col in range (1 , 9) :
        if (col-row == 4 or col+ row ==5 or row-col == 4 or row+ col== 13  ) :
            print ("*" , end = "")
        else :
            print (" ", end = '' )
    print ()