L = {}
escolhido = ['S']
final = 'G'
incial = 'S'



L['S'] = ['C','B']
L['B'] = ['D','E']
L['C'] = ['H']
L['D'] = ['G','F']
L['E'] = ['F']
L['H'] = ['G']
L['F'] = []
L['G'] = []

Y = {}

Y['S'] = 8
Y['B'] = 7
Y['C'] = 3
Y['D'] = 1
Y['E'] = 7
Y['F'] = 6
Y['G'] = 0
Y['H'] = 100 

def busca(nodo):
	menor = 9999999
	for i in range (len(L[nodo])):
		atual = L[nodo][i]
		if (Y[L[nodo][i]] < menor):
			menor = Y[L[nodo][i]]
			lsMenor = L[nodo][i]
	escolhido.append(lsMenor)
	if (lsMenor == final):
		return 0
	else:
		busca(lsMenor)

busca('S')
print(escolhido)





