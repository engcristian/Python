import itertools
print([i for i in ifilter(lambda x: x%5, islice(count(5),10))])