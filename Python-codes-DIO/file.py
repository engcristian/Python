def write_file(text):
    file = open('my_text.txt', 'w')
    file.write(text)
    file.close()
def updt_file(text):
    file = open('my_text.txt', 'a')
    file.write(text)
    file.close()

if __name__== '__main__':
    updt_file('Now in other line.\n')