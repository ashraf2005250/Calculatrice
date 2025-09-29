**1 - ALGORITHME CalculatriceBasique**

**DEBUT
    AFFICHER "=== CALCULATRICE BASIQUE ==="**

 **TANT QUE VRAI FAIRE
        // PHASE 1 : SAISIE UTILISATEUR
        ESSAYER
            SAISIR nombre1 ← input("Entrez le premier nombre: ")
            SAISIR operateur ← input("Entrez l'opérateur (+, -, *, /): ")
            SAISIR nombre2 ← input("Entrez le deuxième nombre: ")**

 **CONVERTIR nombre1 EN float
            CONVERTIR nombre2 EN float**

 **SI ERREUR ValueError ALORS
            AFFICHER "Erreur: Veuillez entrer des nombres valides."
            CONTINUER (retour au début de la boucle)
        FIN ESSAYER**

 **// PHASE 2 : CALCUL
        SELON operateur
            CAS "+":
                resultat ← nombre1 + nombre2
            CAS "-":
                resultat ← nombre1 - nombre2
            CAS "*":
                resultat ← nombre1 * nombre2
            CAS "/":
                SI nombre2 = 0 ALORS
                    AFFICHER "Erreur: Division par zéro."
                    CONTINUER
                SINON
                    resultat ← nombre1 / nombre2
                FIN SI
            AUTRE:
                AFFICHER "Erreur: Opérateur non reconnu."
                CONTINUER
        FIN SELON**

 **// PHASE 3 : AFFICHAGE
        AFFICHER "Résultat: {nombre1} {operateur} {nombre2} = {resultat}"**

 **// PHASE 4 : CONTINUATION
        SAISIR continuer ← input("Nouvelle tentative? (o/n): ")
        SI continuer ≠ "o" ALORS
            QUITTER BOUCLE
        FIN SI
    FIN TANT QUE
FIN**

**2 - ORGANIGRAMME**

**Fichier drawio :**

**Image :**

**3 - Concepts Algorithmiques Etudiés**

**3.1 - Structure de controle Fondamentales**

###### 1. SÉQUENCE - Exécution linéaire

print("=== CALCULATRICE BASIQUE ===")

... instructions dans l'ordre ...

**2. SÉLECTION - Prise de décision**

if operateur == "+":
    resultat = nombre1 + nombre2
elif operateur == "-":
    resultat = nombre1 - nombre2

... autres conditions ...

**3.1 ITÉRATION - Répétition avec condition**

while True:  # Boucle infinie contrôlée
    # ... logique répétée ...
    if continuer != 'o':  # Condition de sortie
        break

 **3.2 - Gestion des Entrées/Sorties**

**ENTREES**

nombre1 = float(input("Entrez le premier nombre: "))

**SORTIES**

print(f"Résultat: {nombre1} {operateur} {nombre2} = {resultat}")

**VALIDATION**

try:
    # Conversion risquée
except ValueError:
    # Gestion d'erreur

3.3 - Gestion d'erreurs et Robustesse

###### Pattern try/except pour saisie utilisateur

try:
    nombre1 = float(input("..."))
except ValueError:
    print("Erreur: nombres invalides")
    continue  # Reprendre au début de la boucle

**Vérification explicite des conditions critiques**

if nombre2 == 0:
    print("Erreur: Division par zéro")
    continue

**4 - Architecture du Programme**

CalculatriceBasique/
│
├── Phase 1: Saisie et Validation
│   ├── Récupération des 3 entrées utilisateur
│   ├── Conversion en types numériques
│   └── Gestion des erreurs de format
│
├── Phase 2: Calcul
│   ├── Reconnaissance de l'opérateur
│   ├── Exécution de l'opération correspondante
│   └── Vérification des conditions spéciales (division par 0)
│
├── Phase 3: Affichage
│   └── Formatage et présentation du résultat
│
└── Phase 4: Contrôle de Flux
    ├── Demande de continuation
    └── Gestion de la terminaison du programme
