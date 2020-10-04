def mediaAritmetica(notas):
    soma = 0
    for nota in notas:
        soma += float(nota)
    media = soma/len(notas) 
    return media

def mediaPonderada(notas, pesos):
    peso_total = 0
    soma = 0
    for peso, nota in zip(pesos, notas):
        peso_total += peso
        soma += nota * peso
    media =  soma/peso_total
    return media

def mediaGeometrica(notas):
    produto = 1
    
    for nota in notas:
        produto *= float(nota)
    
    media = pow(produto, 1/len(notas))
    
    return media

def mediaHarmonica(notas):
    denominador = 0
    for nota in notas:
        denominador += 1/float(nota)
    
    media = len(notas)/denominador
    return media