count_words = lambda lista: [len(w) for w in lista]
calculadora = {
'soma':lambda a, b: a + b,
'mult':lambda a, b: a * b,
'div' :lambda a, b: a / b,


}

if __name__ =='__main__':
    my_sum = calculadora['soma']
    print(my_sum(5,3))