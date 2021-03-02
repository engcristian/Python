
text = open('C:\\Users\crist\Desktop\sobre.txt','r')
count = dict()
for line in text:
    words = line.split()
    for word in words:
        count[word]= count.get(word, 0) +1

bigcount = None # how many times the most repeated word repeats
bigword = None # the word that repeats many times
for word, counts in count.items():
    if bigcount is None or counts > bigcount:
        bigword = word
        bigcount = counts
print(bigword, bigcount)