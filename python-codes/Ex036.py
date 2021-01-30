## valor da casa, salário do comprador e quantos anos ele vai pagar..
## condições: valor da prestação mensal , n pode passar de 30% do salário ou então será negado

print('-='*30)
print('      \033[7;30mBem vindo ao Sistema de Empréstimos Imobiliários\033[m')
print('-='*30)
nome = str(input('Qual é o seu nome?')).lower().title()
casa = float(input('Olá Sr(a) {}. Por favor, informe o valor da casa que deseja financiar: '.format(nome)))
salary = float(input('Sr(a) {}, agora informe o seu salário mensal: '.format(nome)))
anos = int(input('Muito bem Sr {}, para finalizar, insira quantos anos pretende quitar seu empréstimo: '.format(nome)))
parcela = anos * 12
valor = casa/parcela

if valor > salary * 30 / 100:
    print('Desculpa Sr(a) {}, mas o seu empréstimo foi negado, pois em {} anos a prestação será de R${:.2f}'.format(nome, anos, valor), end='')
    print(' e ultrapassa 30% do seu salário.')

elif valor <= salary * 30 /100:
    print('Que ótimo, seu emprétimo foi aprovado, com parcelas de R${:.2f}!'.format(valor))
