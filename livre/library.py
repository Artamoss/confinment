

def ouverture(nom_fichier):
	"""
	Ouvre un fichier et le lit
	"""
	with open(nom_fichier, 'r') as f:
		print(f.read())