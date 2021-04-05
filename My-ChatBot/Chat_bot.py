'''
This is my ChatBot, I call it as Dante.
I'm still improving it to give better rsponses and interact well with users.
'''
# Importing main libs
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer




my_bot = ChatBot('Dante',
        storage_adapter ='chatterbot.storage.SQLStorageAdapter',
        dante_db = 'sqlite:///dante_db.sqlite3'
        )
my_bot = ChatBot('Dante')
conversation = ListTrainer(my_bot)
conversation.train([
        'Oi',
        'Olá',
        'Qual é o seu nome?',
        'Dante',
        'Prazer em te conhcer.',
        'Igualmente!',
        'Tudo bem?',
        'Muito bem e você?',
        'Ótimo',
        'Como foi seu dia?',
        'Bem e o seu? Espeero que tenha sido um ótimo dia.',
        'Gosta de músicas',
        'Sim, adoro! Gosto de Muica POP, e você?',
        'Bom, agora tenho que ir',
        'Okay, entendo, a conversa estava boa.',
        'Adeus',
        'Volte sempre!',
])

treinamento = ChatterBotCorpusTrainer(my_bot)
treinamento.train('chatterbot.corpus.portuguese')

while True:
        resposta = my_bot.get_response(str(input('Usuário: ')))
        
                     
        if float(resposta.confidence) > 0.5:
                        print('Dante: ', resposta)

        else:
                print('Desculpa, eu não entendi.')

