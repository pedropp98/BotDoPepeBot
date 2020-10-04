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
import os

import flask_server
 
from helpers import loadFile
from dotenv import load_dotenv
from handlers import *
from globais import *

#version 6.4.1

# IDS = loadFile("Ignore/Groups.txt").split()
'''
grupo_teste = [int(IDS[0])]
mat_discreta = [int(IDS[1])]
icc = [int(IDS[2])]
fisica = [int(IDS[3]), int(IDS[4])]
algoritmos = [int(IDS[4]), int(IDS[5])]
grupos_sala = [int(IDS[5]), int(IDS[6])]
grupos_permitidos = [grupo_teste, grupos_sala[0], grupos_sala[1]]
'''

def main():
    TOKEN = os.getenv("TELEGRAM_TOKEN")

    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # dp.add_handler(commandStart)
    
    dp.add_handler(comandoMaterias)
    # Comandos que nao dependem da funcao materias
    dp.add_handler(comandoProvas)
    dp.add_handler(comandoProbability)
    dp.add_handler(comandoDoggos)
    dp.add_handler(comandoCotacao)
    dp.add_handler(comandoReps)
    dp.add_handler(comandoTeste)

    updater.start_polling(clean=True)
    logging.info("=== Bot running! ===")
    updater.idle()
    
if __name__ == "__main__":
    load_dotenv()
    main()
    logging.info("=== Bot shutting down! ===")
