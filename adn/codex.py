import sys

nom_fichier = sys.argv[1]

#ouverture du fichier
f = open(nom_fichier, 'r')

list_entree=[]

for (i, line) in enumerate(f):
	list_entree.append(line.strip())

adn = list_entree[0]
code_maladie = list_entree[1]

test_general = False

for i in range(len(adn)-len(code_maladie)+1):
	test = True
	for j in range(len(code_maladie)):
		if (adn[i+j] == code_maladie[j]) and (test == True):
			test = True
		else :
			test = False
	if (test == True):
		test_general = True
		
print(test_general)


