from helpers import loadFile

IDS = loadFile("Ignore/Groups.txt").split()
grupo_teste = [int(IDS[0])]
mat_discreta = [int(IDS[1])]
icc = [int(IDS[2])]
fisica = [int(IDS[3]), int(IDS[4])]
algoritmos = [int(IDS[4]), int(IDS[5])]
grupos_sala = [int(IDS[5]), int(IDS[6])]
grupos_permitidos = [grupo_teste, grupos_sala[0], grupos_sala[1]]