import sys

nom_fichier = sys.argv[1]

#ouverture du fichier
f = open(nom_fichier, 'r')

listeMots=[]

for (i, line) in enumerate(f):
	listeMots.append(line.strip())


Teste = False

def TesteP(m): 
	Teste = False 
	longueur = int(len(m)/2)
	start = 0
	end = len(m) - 1
	for l in range (len(m)):
		if m[start + l] == m[end - l] :
			Teste = True 
		else : Teste = False
	return Teste 


for i in range(len(listeMots)):
	Teste = TesteMotP(listeMots[i])
	print(listeMots[i], "= ", Teste)


#adn = list_entree[0]
#code_maladie = list_entree[1]

#test_general = False

#for i in range(len(adn)-len(code_maladie)+1):
#	test = True
#	for j in range(len(code_maladie)):
#		else :
#			test = False
#	if (test == True):
#		test_general = True
		
#print(test_general)
