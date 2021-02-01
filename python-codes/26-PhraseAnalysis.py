'''
Analysing the letter 'A' in a phrase.
'''
phrase = str(input('Type any phrase: ')).strip().lower()
print('The letter A appears {} times in this  phrase.'.format(phrase.count('a')))
print('The first letter A appeared on the {}º position.'.format(phrase.find('a')+1))
print('The last letter A appeared on the {}º position.'.format(phrase.rfind('a')+1))