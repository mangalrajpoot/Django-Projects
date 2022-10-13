import time
import pyttsx3
engine=pyttsx3.init()
bal=50000
engine.say('Please Enter Pin')
pin=int(input('Please Enter Pin:'))

if(pin==1234):
    print('Welcome to Our Bank')
    engine.say('Welcome to Our Bank')
else:
    exit()
ch=input('Press B for Balance \n Press C for Credit \n Press D for Debit')
engine.say('Press B for Balance \n Press C for Credit \n Press D for Debit')
while True:
    if(ch=='B' or ch=='b'):
       print('Your Balance: ',bal)
       
       engine.say('Your Balance: {0}'.format(bal))
       break
    elif(ch=='C' or ch=='c'):
        amt=int(input('Enter Amount: '))
        engine.say('Enter Amount: ')
        bal+=amt
        print('Transaction Success')
        engine.say('Transaction Success')
        print('Your Balance: ',bal)
        engine.say('Your Balance: {0} '.format(bal))
        print('Thank you for Banking with us')
        engine.say('Thank you for Banking with us')
        break
    elif(ch=='D' or ch=='d'):
        amt=int(input('Enter Amount: '))
        engine.say('Enter Amount : ')
        if(amt>bal):
            print('You have no sufficient balance')
            engine.say('You have no sufficient balance')
            break
        else:
            bal-=amt
            print('Transaction Success')
            engine.say('Transaction Success')
            print('Your Balance {0}'.format(bal))
            engine.say('Your Balance {0}'.format(bal))
            print('Thank you for Banking with us')
            engine.say('Thank you for Banking with us')
            break
engine.runAndWait()
    

    
    



    
