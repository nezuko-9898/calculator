print( ' ========Calculator========')
print('1.Addition')
print('2.Substraction')
print('3.Multiplication')
print('4.Division')
print('5.Exit')

while True:

    choice = input("Enter your choice....")

    if choice == '5':
        print('Your are Exit....')
        break

    if choice in ('1','2','3','4'):
        num1 = float(input("Enter Yourn Number 1 ===>"))
        num2 = float(input("Enter Your Number 2 ===>"))

        if choice == '1':
          print(f'Result:{num1+num2}')

        elif choice == '2':
           print(f'Result:{num1-num2}')

        elif choice == '3':
           print(f'Result:{num1*num2}')

        elif choice =='4':

           if num2 != 0:

            print(f'Result:{num1 / num2}')

           else:

             print('Error! | Can not Divide by Zero')

        else:

           print('Invalid Input')                            

    


    