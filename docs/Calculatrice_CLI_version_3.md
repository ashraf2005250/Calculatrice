**Calculatrice_CLI_version_1**

**1 . Algorithme**

ALGORITHME CalculatriceRPN
DEBUT
    // INITIALISATION
    CONSTS ← {"pi": π, "e": e}
    FUNCS ← {"sin": sin, "cos": cos, ...}
    OPS ← {symbole: (priorité, associativité, fonction)}
    ALIASES ← {"**": "^"}

    // MODE EXÉCUTION
    SI arguments > 1 ALORS
        expression ← concaténer arguments[1:]
        résultat ← eval_expr(expression)
        AFFICHER résultat
    SINON
        // MODE REPL INTERACTIF
        AFFICHER instructions
        ans ← None

    TANT QUE VRAI FAIRE
            SAISIR input ← input(">>> ")
            input ← TRIM(input)

    SI input ∈ (":q", ":quit", ":exit") ALORS BREAK
            SI input VIDE ALORS CONTINUER

    ESSAYER
                résultat ← eval_expr(input, ans)
                ans ← résultat
                AFFICHER résultat
            SI ERREUR ALORS
                AFFICHER "Erreur: {message}"
            FIN ESSAYER
        FIN TANT QUE
    FIN SI
FIN

// SOUS-ALGORITHME eval_expr
ALGORITHME eval_expr(expression, ans)
DEBUT
    expression ← REMPLACER(expression, "ans", ":ans")
    tokens ← tokenize(expression)
    rpn ← infix_to_rpn(tokens)
    RETOURNER eval_rpn(rpn, ans)
FIN

// SOUS-ALGORITHME tokenize
ALGORITHME tokenize(chaîne)
DEBUT
    tokens ← []
    position ← 0

    TANT QUE position < LONGUEUR(chaîne) FAIRE
        correspondance ← TOKEN_RX.match(chaîne, position)
        SI non correspondance ALORS
            LANCER ERREUR "Jeton invalide"
        FIN SI

    token ← correspondance.groupe(1)
        position ← correspondance.fin()

    SI token NON VIDE ALORS
            token ← ALIASES[token] SI existe SINON token
            AJOUTER token À tokens
        FIN SI
    FIN TANT QUE

    RETOURNER tokens
FIN

// SOUS-ALGORITHME infix_to_rpn (SHUNTING-YARD)
ALGORITHME infix_to_rpn(tokens)
DEBUT
    FONCTION is_unary_minus(i):
        SI tokens[i] ≠ "-" ALORS RETOURNER FAUX
        SI i = 0 ALORS RETOURNER VRAI
        précédent ← tokens[i-1]
        RETOURNER précédent ∈ OPS OU précédent ∈ ("(", ",")

    sortie ← []
    pile ← []

    POUR i, t DANS tokens FAIRE
        SELON type(t):
            CAS nombre: AJOUTER float(t) À sortie
            CAS constante: AJOUTER CONSTS[t] À sortie
            CAS fonction: EMPILER t
            CAS ",":
                TANT QUE pile NON VIDE ET SOMMET(pile) ≠ "(" FAIRE
                    AJOUTER DÉPILER() À sortie
                FIN TANT QUE
                SI pile VIDE ALORS ERREUR "Virgule mal placée"
            CAS opérateur:
                SI is_unary_minus(i) ALORS
                    EMPILER "neg"
                SINON
                    p1, assoc1, _ ← OPS[t]
                    TANT QUE pile NON VIDE ET SOMMET(pile) ∈ OPS FAIRE
                        p2, assoc2, _ ← OPS[SOMMET(pile)]
                        SI (assoc1 = GAUCHE ET p1 ≤ p2) OU (assoc1 = DROITE ET p1 < p2) ALORS
                            AJOUTER DÉPILER() À sortie
                        SINON
                            BREAK
                        FIN SI
                    FIN TANT QUE
                    EMPILER t
                FIN SI
            CAS "(": EMPILER t
            CAS ")":
                TANT QUE pile NON VIDE ET SOMMET(pile) ≠ "(" FAIRE
                    AJOUTER DÉPILER() À sortie
                FIN TANT QUE
                SI pile VIDE ALORS ERREUR "Parenthèses mal appariées"
                DÉPILER() // Enlève "("
                SI pile NON VIDE ET SOMMET(pile) ∈ FONCTIONS ALORS
                    AJOUTER DÉPILER() À sortie
                FIN SI
            AUTRE: ERREUR "Token inconnu"
        FIN SELON
    FIN POUR

    // Vidage final de la pile
    TANT QUE pile NON VIDE FAIRE
        top ← DÉPILER()
        SI top ∈ ("(", ")") ALORS ERREUR "Parenthèses mal appariées"
        AJOUTER top À sortie
    FIN TANT QUE

    RETOURNER sortie
FIN

// SOUS-ALGORITHME eval_rpn
ALGORITHME eval_rpn(rpn, ans)
DEBUT
    pile ← []

    POUR x DANS rpn FAIRE
        SELON type(x):
            CAS nombre: EMPILER x
            CAS "neg":
                SI pile VIDE ALORS ERREUR "Unaire mal formé"
                EMPILER -DÉPILER()
            CAS opérateur:
                SI TAILLE(pile) < 2 ALORS ERREUR "Expression incomplète"
                b ← DÉPILER(), a ← DÉPILER()
                ESSAYER
                    résultat ← OPS[x][2](a, b)
                    EMPILER résultat
                SI DivisionParZéro ALORS ERREUR "Division par zéro"
            CAS fonction:
                SI pile VIDE ALORS ERREUR "Fonction sans argument"
                argument ← DÉPILER()
                EMPILER FUNCS[x](argument)
            CAS ":ans":
                SI ans = NULL ALORS ERREUR "Pas de valeur précédente"
                EMPILER ans
            AUTRE: ERREUR "Symbole RPN inconnu"
        FIN SELON
    FIN POUR

    SI TAILLE(pile) ≠ 1 ALORS ERREUR "Expression invalide"
    RETOURNER pile[0]
FIN


**2 . Organigramme**

Drawio

**3 . Concepts Algorithmiques Etudiés**

Algorithmes classiques Implémentés


3 . 1. ALGORITHME SHUNTING-YARD (DIJKSTRA)

Conversion notation infixe → postfixe avec gestion priorités

while stack and stack[-1] in OPS:
    if (priorité_courante <= priorité_pile):
        out.append(stack.pop())
    else:
        break
stack.append(opérateur)

3 . 2. NOTATION POLONAISE INVERSÉE (RPN)

Évaluation avec pile - pas besoin de parenthèses

"3 4 + 5 *" → 3+4=7, 7*5=35

3 . 3. AUTOMATE À PILE

Évaluation séquentielle avec structure LIFO

Concepts Avancés

3 . 4. DÉTECTION OPÉRATEURS UNAIRES

def is_unary_minus(i):
    return (tokens[i] == "-" and
           (i == 0 or tokens[i-1] in OPS or tokens[i-1] in ("(", ",")))

3 . 5. GESTION ASSOCIATIVITÉ

(assoc1 == LEFT and p1 <= p2) or (assoc1 == RIGHT and p1 < p2)

3 . 6. WHITELIST TOKENS AVEC RÉGEX

TOKEN_RX = re.compile(r"\s*(\d+(?:\.\d+)?|[A-Za-z_]\w*|\*\*|//|[+\-*/%^(),])")

3 . 7 . évolution Algorithmique

VERSION 1: Conditions simples

if op == "+": result = a + b

VERSION 2: Dispatch dictionnaire

result = OPS[op](a, b)

VERSION 3: AST récursif

result = eval_ast(node)

VERSION RPN: Algorithmes classiques + automate pile

Shunting-yard + évaluation RPN

**4 . Architecture**

CalculatriceRPN/
│
├── Étape 1: Tokenization (Analyse Lexicale)
│   ├── Expression régulière TOKEN_RX
│   ├── Découpage en tokens
│   └── Gestion alias (**, → ^)
│
├── Étape 2: Parsing (Analyse Syntaxique)
│   └── Algorithme Shunting-yard
│       ├── Gestion priorités opérateurs
│       ├── Détection opérateurs unaires
│       ├── Gestion fonctions
│       └── Validation parenthèses
│
├── Étape 3: Évaluation (Analyse Sémantique)
│   └── Évaluation RPN
│       ├── Automate à pile
│       ├── Dispatch opérations
│       ├── Gestion fonctions
│       └── Variable 'ans'
│
├── Étape 4: Interface Utilisateur
│   ├── Mode REPL interactif
│   ├── Mode batch CLI
│   └── Gestion état (ans)
│
└── Couche Configuration
    ├── CONSTS, FUNCS, OPS, ALIASES
    └── Tables de symboles
