class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Type a velue beteween 0 and 10: '))
        print(x)
        if x > 10:
            raise InputError('The value is higher than 10.')
        elif x < 0:
            raise InputError('The value is lower than 0')
        break
    except ValueError:
        print('Error: Only acept numbers not strings ')
    except InputError as ex:
        print(ex)