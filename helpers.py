
def escapeMarkdown(string):
  reservado = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!' ]
  for c in reservado:
    string = string.replace(c, '\\' + c)
  
  return string

def loadFile(nomeArquivo):
    arquivo = open(nomeArquivo, encoding="UTF-8")
    linhasLidas = arquivo.readline()
    mensagem = ""
    while linhasLidas:
        mensagem += linhasLidas
        linhasLidas = arquivo.readline()
    arquivo.close()
    return mensagem