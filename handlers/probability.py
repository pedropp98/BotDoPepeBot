import random

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