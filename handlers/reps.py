from globais import *

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