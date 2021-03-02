count = dict()
text = '''Ex servente de ladrilheiro que largou o canteiro de obras para realizar um sonho de infância, a tal sonhada
sonhada formação acadêmica. Formado em engenharia de controle e automação em 2019, com um dos melhores rendimentos da turma
agregei valores e informações preciosas. 

Durante a graduação em 2017 abri minha própria microempresa de redes de internet onde durante três anos realizei trabalhos
de instalação, manutenção e análises de internet, alcançando mais de 60 clientes na vizinhaça.

Mas nem tudo é um mar de rosas... a crise veio, e é onde surge o professor de inglês e professor de música, com projetos
alcançados em diversas igrejas da zona Oeste, aulas de bateria, violão, baixo e teclado, além de ministrar aulas de inglês básico para diversas faixas etárias.

Me especializando em análise de dados, com auxílio do Python como principal linguagem, SQLs na aquisição de 
dados, Jupyter no tratamento e  análise gráfica e apliando conhecimentos em bibliotecas como pandas, numpy e TensorFlow.
Atualmente em busca de uma oportunidade de crescimento profissional em equipe, desenvolvendo soluções e gerando valores
como programador. A caminhada sempre foi difícil, mas desistir nunca foi uma opção.'''
words = text.split()
for word in words:
    count[word] = count.get(word, 0) + 1


print(count)