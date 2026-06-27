# ===== LES VARIABLES =====

# Types de base
nom = "Samy"           # str = texte
age = 25               # int = nombre entier
taille = 1.75          # float = nombre décimal
etudiant = True        # bool = vrai ou faux

# Afficher les variables
print("Nom :", nom)
print("Age :", age)
print("Taille :", taille)
print("Etudiant :", etudiant)

# ===== LES TYPES =====
print("\n--- Types ---")
print(type(nom))
print(type(age))
print(type(taille))
print(type(etudiant))

# ===== LES OPÉRATIONS =====
print("\n--- Calculs ---")
a = 10
b = 3
print("Addition :", a + b)
print("Soustraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Division entière :", a // b)
print("Reste :", a % b)
print("Puissance :", a ** b)

# ===== LES STRINGS =====
print("\n--- Texte ---")
prenom = "Samy"
metier = "Développeur"
print("Bonjour je suis " + prenom)
print(f"Je veux devenir {metier}")
print("Majuscules :", prenom.upper())
print("Longueur :", len(prenom))

# ===== INPUT =====
print("\n--- Saisie ---")
votre_nom = input("Entrez votre nom : ")
print(f"Bonjour {votre_nom} !")
