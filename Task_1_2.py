a=input()
 if a[0]=='-':
     b=a[1::]
     if b[::-1][0]=='0':
         if -2**7<=int('-'+b[::-1][1::])<=2**7-1:
             print('-'+b[::-1][1::])
         else:
             print('no solution')
     else:
         if -2**7<=int('-'+b[::-1])<=2**7-1:
             print('-'+b[::-1])
         else:
             print('no solution')
 else:
     if -2**7<=int(a[::-1])<=2**7-1:
         print(a[::-1])
     else:
         print('no solution')
