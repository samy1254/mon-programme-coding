# ===== BOUCLE FOR =====

# Compter de 1 à 5
print("--- Compter ---")
for i in range(1, 6):
    print(i)

# Compter de 0 à 10 par pas de 2
print("\n--- Nombres pairs ---")
for i in range(0, 11, 2):
    print(i)

# Parcourir une liste
print("\n--- Liste ---")
langages = ["HTML", "CSS", "Python", "Java", "C++", "Réseaux"]
for langage in langages:
    print("J'apprends :", langage)

# Boucle avec index
print("\n--- Avec numéro ---")
for i, langage in enumerate(langages):
    print(f"{i+1}. {langage}")

# ===== BOUCLE WHILE =====
print("\n--- While ---")
compteur = 0
while compteur < 5:
    print("Compteur :", compteur)
    compteur += 1

# ===== EXERCICE CONCRET =====
print("\n--- Table de multiplication ---")
nombre = int(input("Entrez un nombre : "))
for i in range(1, 11):
    print(f"{nombre} x {i} = {nombre * i}")
