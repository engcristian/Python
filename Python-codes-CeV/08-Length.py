'''
By a length in meters you can check how it is in kilometer, hectometer
decimeter, centimeter and millimeter 
'''

m = float(input('Type a length in meters: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('The value in kilometer is {:.3f}. \nThe value in hectometer is {:.2f}. \nThe value in decameter is {:.2f}.'.format(km, hm, dam))
print('The value in decimeter is 25.5{:.2f}. \nThe value in centimeter is {:.2f}. \nThe value in millimeter is {:.2f}.'.format(dm, cm, mm))
