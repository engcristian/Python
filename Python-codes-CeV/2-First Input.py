'''
Simple way to get an string as input.
'''
name = input("What's your name?!")
print("Cool {}{}{}!. It's a pleasure to meet you!!".format('\033[1;7m', name, '\033[m'))