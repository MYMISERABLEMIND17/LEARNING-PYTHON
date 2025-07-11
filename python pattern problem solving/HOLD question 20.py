'''
abcdefg
 abcdef
  abcde
   abcd
    abc
     ab
      a
     ab
    abc
   abcd
  abcde
 abcdef
abcdefg
'''
for row in range (1,8 ):
    for col in range (2,row+1) :
        print ("*", end="")
    print ()
for row in range (8 , 15 ) :
    for col in range (1 , 15-row) :
        print ("*" , end = '')
    print () 
str = "abcdefg" 
for row in range (1,8 ) :
    for col in range (1, 8 - row ):
        print (str[col] ," ", end ="" )
    print =()

    



