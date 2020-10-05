from cotacao import DolarToFloat

def cotacao(update, context):
    precoDolar = DolarToFloat()
    BandecoString = str(round((precoDolar / 2), 2)).replace(".",",")
    chatId = update.message.chat_id
    messageId = update.message.message_id
    texto = f"O dólar está {BandecoString} bandecos. ($ 1.00 = R$ {precoDolar:.2f})"
    context.bot.sendMessage(chat_id = chatId, text = texto, reply_to_message_id = messageId)