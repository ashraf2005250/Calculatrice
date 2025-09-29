**Calculatrice_CLI_version_1**

**1 - Algorithmes**

ALGORITHME CalculatriceCLI
DEBUT
    // DÉFINITION DES RESSOURCES
    OPS ← {
        "+": fonction_addition,
        "-": fonction_soustraction,
        "*": fonction_multiplication,
        "/": fonction_division
    }

    // PHASE 1 : SAISIE UTILISATEUR
    SAISIR expression ← input("Entrez un calcul (ex: 2 +3): ")
    expression ← SUPPRIMER_ESPACES(expression)

    // PHASE 2 : DÉCOMPOSITION
    elements ← DIVISER(expression, " ")
    SI LONGUEUR(elements) ≠ 3 ALORS
        LANCER ERREUR "Format invalide"
    FIN SI

    a_str, op, b_str ← elements

    // PHASE 3 : CONVERSION NUMÉRIQUE
    ESSAYER
        a ← CONVERTIR(a_str, float)
        b ← CONVERTIR(b_str, float)
    SI ERREUR ALORS
        LANCER ERREUR "Conversion numérique échouée"
    FIN ESSAYER

    // PHASE 4 : VALIDATION OPÉRATEUR
    SI op ∉ OPS ALORS
        LANCER ERREUR "Opérateur inconnu: " + op
    FIN SI

    // PHASE 5 : CALCUL ET AFFICHAGE
    fonction_calcul ← OPS[op]
    resultat ← fonction_calcul(a, b)
    AFFICHER resultat

FIN

**2 - Organnigramme**

Drawio

**3 - Concepts Algorithmiques** 

**1. DICTIONNAIRE DE FONCTIONS - Dispatch dynamique**

OPS = {
    "+": operator.add,      # Référence à fonction
    "-": operator.sub,      # Pas d'appel, juste référence
    "*": operator.mul,
    "/": operator.truediv
}

**Utilisation: Appel dynamique**

fonction = OPS[op]         # Récupération fonction
resultat = fonction(a, b)  # Appel fonction

**2. DÉSTRUCTURATION - Unpacking avancé**

a_str, op, b_str = raw.split()  # Assignation multiple

**3. GESTION D'ERREURS IMPLICITE**

Le code laisse les exceptions remonter (approche différente)

**4 - Architecture du Programme**

CalculatriceCLI/
│
├── Couche Configuration
│   └── Dictionnaire OPS (mapping symboles → fonctions)
│
├── Couche Entrée/Sortie
│   ├── Saisie utilisateur (input)
│   ├── Prétraitement (strip)
│   └── Affichage résultat (print)
│
├── Couche Traitement
│   ├── Tokenization (split)
│   ├── Conversion (float)
│   ├── Validation (vérification opérateur)
│   └── Dispatch (appel fonction via OPS)
│
└── Couche Logique Métier
    └── Fonctions operator (add, sub, mul, truediv)
