from telegram.ext import *
import telegram
import dontpad
from globais import *
from helpers import *

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

    markdown = escapeMarkdown(provas)

    if chatId in grupos_permitidos:
        msg = "Para editar essa mensagem, clique [aqui](http://www.dontpad.com/AvisosProvasBCC020)"
        markdown += "\n\n" + msg

    update.message.reply_text(text = markdown,
                              reply_to_message_id = messageId,
                              parse_mode = "MarkdownV2")

def separaProvas(materia, provas):
    splitProvas = provas.split("\n")
    textoFiltrado = f"{splitProvas[0]}\n"
    for i in splitProvas:
        if i.find(materia) != -1:
            textoFiltrado += f"{i}\n"

    return textoFiltrado