#import sys para mudar o encoding do sys.stdout para utf-8
import sys
sys.stdout.reconfigure(encoding='utf-8')

#ignorar warnings do tensorflow
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#importar a classe ChatBot do arquivo chatbot.py
from chatbot import ChatBot
myChatBot = ChatBot()

#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo do zero com os dados do arquivo json atual
myChatBot.createModel()

#print de boas vindas
print("Bem vindo ao Chatbot FEI")

#primeira pergunta do usuário para iniciar a conversa
pergunta = input("Oque deseja saber?\n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")

#loop para continuar a conversa até que o usuário deseje sair
while (intencao[0]['intent']!="despedida"):
    pergunta = input("posso lhe ajudar com algo a mais?")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")

print("Foi um prazer ajudá-lo")