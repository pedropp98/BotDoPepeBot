from telegram.ext import *
import telegram
import logging
import requests
import re
import urllib
import random
import dontpad
from cotacao import DolarToFloat
import random

#version 6.4.1

'''def start(update, context):
    s = "hello, world!"
    #context.bot.send_message(chat_id=update.effective_chat.id, text=s)
    update.message.reply_text(s)'''

def loadFile(nomeArquivo):
    arquivo = open(nomeArquivo, encoding="UTF-8")
    linhasLidas = arquivo.readline()
    mensagem = ""
    while linhasLidas:
        mensagem += linhasLidas
        linhasLidas = arquivo.readline()
    arquivo.close()
    return mensagem

TOKEN = loadFile("Ignore/token.txt")
IDS = loadFile("Ignore/Groups.txt").split()
grupo_teste = [int(IDS[0])]
mat_discreta = [int(IDS[1])]
icc = [int(IDS[2])]
fisica = [int(IDS[3]), int(IDS[4])]
algoritmos = [int(IDS[4]), int(IDS[5])]
grupos_sala = [int(IDS[5]), int(IDS[6])]
grupos_permitidos = [grupo_teste, grupos_sala[0], grupos_sala[1]]

def separaProvas(materia, provas):
    splitProvas = provas.split("\n")
    textoFiltrado = f"{splitProvas[0]}\n"
    for i in splitProvas:
        if i.find(materia) != -1:
            textoFiltrado += f"{i}\n"
    return textoFiltrado

def image():
    allowedExtension = ['jpg', 'jpeg', 'png']
    while True:
        url = requests.get('https://random.dog/woof.json').json()['url']
        fileExtension = re.search("([^.]*)$", url).group(1).lower()
        if fileExtension in allowedExtension:
            break
    return url
    
def provas(update, context):
    chatId = update.message.chat_id
    messageId = update.message.message_id
    provas = dontpad.read("AvisosProvasBCC020")
    if chatId in mat_discreta:
        provas = separaProvas("Mat Discreta", provas)
    elif chatId in icc:
        provas = separaProvas("ICC", provas)
    elif chatId in fisica:
        if chatId == fisica[0]:
            provas = separaProvas("Hoyos", provas)
        else:
            provas = separaProvas("Esmerindo", provas) 
    elif chatId in algoritmos:
        if chatId == algoritmos[0]:
            provas = separaProvas("Rudinei", provas)
        else:
            provas = separaProvas("Manzato", provas)
    
    print(len(provas))

    context.bot.sendMessage(chat_id = chatId, text = provas, reply_to_message_id = messageId)
    if chatId in grupos_permitidos:
        msg = "Para editar essa mensagem, clique [aqui](http://www.dontpad.com/AvisosProvasBCC020)"
        context.bot.sendMessage(chat_id = chatId, text = msg, parse_mode = "MarkdownV2")

def doggos(update, context):
    update.message.reply_photo(photo = image())

def cattos(update, context):
    r = requests.get('https://api.thecatapi.com/v1/images/search')
    url = r.json()[0]['url']
    update.message.reply_photo(photo=url)

def cotacao(update, context):
    precoDolar = DolarToFloat()
    BandecoString = str(round((precoDolar / 2), 2)).replace(".",",")
    chatId = update.message.chat_id
    messageId = update.message.message_id
    texto = f"O dólar está {BandecoString} bandecos. ($ 1.00 = R$ {precoDolar:.2f})"
    context.bot.sendMessage(chat_id = chatId, text = texto, reply_to_message_id = messageId)

def probability(update, context):
    texto = context.args
    chatId = update.message.chat_id
    username = update.message.from_user.username
    member = f"@{username}"
    tamanhoLista = len(texto)
    if tamanhoLista == 0:
        men = f"{member} não consigo calcular a probabilidade sem saber o que é..."
    else:
        men = f"{member} a probabilidade de "
        for i in range(tamanhoLista):
            if "eu" == texto[i]:
                texto[i] = "você"
            men += f"{texto[i]} "
        prob = str(random.randint(0,100))
        men += f"é de: {prob}%"
    context.bot.sendMessage(chat_id = chatId, text = men)

def materias(update, context):
    print(context.args)
    comando = update.message.text
    if "@" in comando:
        nomeDaMateria = comando.partition("@")[0][1:]
    else:
        nomeDaMateria = comando[1:]
    print(nomeDaMateria)
    
    caminhoArquivo = f"Files/{nomeDaMateria}.txt"
    
    try:
        mensagem = loadFile(caminhoArquivo)
    except FileNotFoundError:
        mensagem = "Desculpa, não tenho informação sobre essa matéria ainda\.\.\. Ou o meu programador é preguiçoso demais\. Pqp viu @pedropp98"
    
    chatId = update.message.chat_id
    messageId = update.message.message_id
    context.bot.sendMessage(chat_id = chatId, text = mensagem, reply_to_message_id = messageId, 
                            parse_mode = "MarkdownV2", disable_web_page_preview = True) 

def reps(update, context):
    chatId = update.message.chat_id
    messageId = update.message.message_id
    print(chatId)
    if chatId in grupos_permitidos:
        listaAdminitradores = context.bot.getChatAdministrators(chat_id = update.message.chat_id)
        representantes = []
        retornaRepresentantes = []
        for itensLista in listaAdminitradores:
            if not itensLista.status == "creator":
                representantes.append(f"@{itensLista.user.username}")
        quantidadeReps = len(representantes) / 4
        print(quantidadeReps)
        if quantidadeReps > 4:
            for iterate in range(quantidadeReps / 4):
                retornaRepresentantes.append(representantes[iterate:iterate+3])
        else:
            retornaRepresentantes = representantes
        men = "Os lindes representantes da turma: "
        for iterate in range(len(retornaRepresentantes)):
            men += f"{retornaRepresentantes[iterate]} "            
    else:
        men = "Desculpe, esse grupo não é permitido para esse comando."
    context.bot.sendMessage(chat_id = chatId, text = men, reply_to_message_id = messageId)

def teste(update, context):
    print(update.message.chat_id)

def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    
    '''dp.add_handler(CommandHandler('start', start))'''
    #Comandos que dependem da funcao materias
    comandos = ['icc', 'labicc', 'algoritmos', 'fisica', 'humanidades', 'mat', 
                'calc', 'sistemas', 'praticasd', 'pesquisa', 'agendasd', 
                'agendalabicc', 'agendaicc']
    dp.add_handler(CommandHandler(comandos, materias))
    
    #Comandos que nao dependem da funcao materias
    dp.add_handler(CommandHandler('provas', provas))
    dp.add_handler(CommandHandler('doggos', doggos))
    dp.add_handler(CommandHandler('cattos', cattos))
    dp.add_handler(CommandHandler('cotacao', cotacao))
    dp.add_handler(CommandHandler('probability', probability))
    dp.add_handler(CommandHandler('reps', reps))

    #Comando pra eu pegar info sobre grupos
    dp.add_handler(CommandHandler('teste', teste))    
    
    updater.start_polling(clean=True)

    logging.info("=== Bot running! ===")
    
    updater.idle()
    
if __name__ == "__main__":
    
    main()
    logging.info("=== Bot shutting down! ===")
