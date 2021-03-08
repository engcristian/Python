import requests

def dados_cep_return(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['bairro'])
    print(dados_cep['localidade'])
    

num = int(input('CEP: '))
print(dados_cep_return(num))
