'''
Reading the car's speed and checking the fee
'''
speed = int(input("What is the actual car's speed?"))

if speed > 80:

    print('Fenied! You have exceeded the speed limit which is 80km/h!\n'
          f'You will be required to pay a ${(speed-80)*7:.2f} fee!')
print('Have a nice day! Drive safely.')