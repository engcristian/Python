'''
Checking palindrome texts without accents
'''

text = str(input('Type a sentence to check: ')).strip().upper() #removing unecessary spaces and putting uppercase
join = text.replace(' ', '')   #removing the spaces and joining the words
palindrome = ''
for letra in range(len(join) -1, -1, -1):
    palindrome += join[letra]
print(f'The text {text}  inverted is {palindrome}.')
if palindrome == join:
    print("It's a palindrome.")
else:
    print("It isn't a palindrome.")