## ler duas notas de um aluno e informar 3 médias , reprovado <5, recuperação 5 - 5,9 ou aprovado media 7
n1 = float(input('Informe a nota do primeiro bimestre: '))
n2 = float(input('Informe a nota do segundo bimestre: '))
m = (n1 + n2)/2

if m >= 7:
    print('Aluno com média \033[35m{}\033[m: \033[32mAPROVADO\033[m'.format(m))
elif m >= 5 and m < 7:
    print('Aluno com média \033[35m{}\033[m: \033[33mRECUPERAÇÂO\033[m'.format(m))
else:
    print('Aluno com média \033[35m{}\033[m: \033[31mREPROVADO\033[m'.format(m))