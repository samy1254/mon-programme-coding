# ===== CONDITIONS =====

age = int(input("Entrez votre age : "))

if age < 18:
    print("Tu es mineur")
elif age < 25:
    print("Tu es jeune adulte")
elif age < 60:
    print("Tu es adulte")
else:
    print("Tu es senior")

# ===== COMPARAISONS =====
print("\n--- Comparaisons ---")
a = 10
b = 20

print(a == b)   # égal ?
print(a != b)   # différent ?
print(a > b)    # plus grand ?
print(a < b)    # plus petit ?
print(a >= 10)  # plus grand ou égal ?

# ===== CONDITIONS MULTIPLES =====
print("\n--- Conditions multiples ---")
note = int(input("Entrez votre note sur 20 : "))
while True:
    note = int(input("Entrez votre note sur 20 : "))
    
    if note < 0 or note > 20:
        print("Erreur ! La note doit être entre 0 et 20.")
    else:
        break  # sort de la boucle si la note est correcte

# Ici on est sorti de la boucle, la note est valide
if note >= 16:
    print("Très bien !")
elif note >= 14:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")
# ===== EXEMPLE CONCRET =====
print("\n--- Connexion ---")
mot_de_passe = input("Entrez le mot de passe : ")

if mot_de_passe == "python123":
    print("Accès autorisé !")
else:
    print("Mot de passe incorrect !")
