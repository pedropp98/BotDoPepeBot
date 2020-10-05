from helpers import loadFile

def materias(update, context):
    comando = update.message.text
    if "@" in comando:
        nomeDaMateria = comando.partition("@")[0][1:]
    else:
        nomeDaMateria = comando[1:]
    
    caminhoArquivo = f"Files/{nomeDaMateria}.txt"
    
    try:
        mensagem = loadFile(caminhoArquivo)
    except FileNotFoundError:
        mensagem = "Desculpa, não tenho informação sobre essa matéria ainda\.\.\. Ou o meu programador é preguiçoso demais\. Pqp viu @pedropp98"
    
    chatId = update.message.chat_id
    messageId = update.message.message_id
    context.bot.sendMessage(chat_id = chatId, text = mensagem, reply_to_message_id = messageId, 
                            parse_mode = "MarkdownV2", disable_web_page_preview = True) 