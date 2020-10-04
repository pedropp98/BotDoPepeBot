from telegram.ext import *

from handlers.provas import provas
from handlers.probability import probability
from handlers.materias import materias
from handlers.doggos import doggos
from handlers.cotacao import cotacao
from handlers.reps import reps
from handlers.teste import teste
from handlers.start import start

comandosMateria = ['icc', 'labicc', 'algoritmos', 'fisica', 'humanidades', 'mat', 
                   'calc', 'sistemas', 'praticasd', 'pesquisa', 'agendasd', 
                   'agendalabicc', 'agendaicc']

# Comandos que dependem da funcao materias
comandoMaterias    = CommandHandler(comandosMateria, materias)
comandoProvas      = CommandHandler("provas", provas)
comandoProbability = CommandHandler("probability", probability)
comandoDoggos      = CommandHandler("doggos", doggos)
comandoCotacao     = CommandHandler("cotacao", cotacao)
comandoReps        = CommandHandler("reps", reps)
# Comando pra eu pegar info sobre grupos
comandoTeste       = CommandHandler("teste", teste)
comandoStart       = CommandHandler("start", start)