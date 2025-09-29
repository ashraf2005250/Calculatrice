import sys, math, re

# =====================================
# PARTIE 1 : DEFINITIONS DES CONSTANTES ET FONCTIONS
# =====================================

# Constantes mathématiques
CONSTS = {"pi": math.pi, "e": math.e} 

# Fonctions mathématiques disponibles
FUNCS = {
    "abs": abs,
    "sqrt": math.sqrt,
    "log": math.log,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "pow": math.pow,
}

# =====================================
# PARTIE 2 : DEFINITION DES OPERATEURS ET PRIORITES
# =====================================

LEFT, RIGHT = "L", "R" # Associativité (gauche/droite)

# Opérateurs: (priorité, associativité, fonction)
OPS = {
    "+": (2, LEFT, lambda a, b: a + b),
    "-": (2, LEFT, lambda a, b: a - b),
    "*": (3, LEFT, lambda a, b: a * b),
    "/": (3, LEFT, lambda a, b: a / b),  
    "//": (3, LEFT, lambda a, b: a // b),
    "%": (3, LEFT, lambda a, b: a % b),
    "^": (4, RIGHT, lambda a, b: a ** b),
}

# Facilitations de la saisie
ALIASES = {"**": "^"}

# =====================================
# PARTIE 3 : ANALYSE LEXICALE (TOKENIZATION)
# =====================================

# Expression régulière pour reconnaitre les tokens
TOKEN_RX = re.compile(r"\s*(\d+(?:\.\d+)?|[A-Za-z_]\w*|\*\*|//|[+\-*/%^(),])")

def tokenize(s: str):
    """
    Transformation d'une chaine en liste de tokens
    Ex: "2 + 3" -> ["2", "+", "3"]  
    """
    pos = 0
    tokens = []
    
    while pos < len(s):
        m = TOKEN_RX.match(s, pos)
        if not m:
            raise ValueError(f"Jeton invalide près de: {s[pos:pos+10]!r}")
        tok = m.group(1)
        pos = m.end()
        if not tok:
            continue
        tokens.append(ALIASES.get(tok, tok)) 
    return tokens

# =====================================
# PARTIE 4 : CONVERSION NOTATION INFIXE -> POSTFIXE (RPN)
# =====================================

def infix_to_rpn(tokens):
    """
    Convertit la notation infixe en notation polonaise inversée (RPN)
    Algorithme de shunting_yard de Dijkstra
    """
    def is_unary_minus(i):
        """
        Détecte si le '-' est unaire (ex: -5) ou binaire (ex: 2 - 1)  
        """
        t = tokens[i]
        if t != "-":
            return False
        if i == 0:
            return True
        prev = tokens[i-1]
        return prev in OPS or prev in ("(", ",")
    
    out = [] # sortie en RPN
    stack = [] # Pile d'opérateurs
    
    for i, t in enumerate(tokens):
        # Nombre
        if re.fullmatch(r"\d+(?:\.\d+)?", t):
            out.append(float(t))
            
        # Constante (pi, e)
        elif t in CONSTS:
            out.append(CONSTS[t])
            
        # Fonction (sin, cos, etc.)
        elif t in FUNCS:
            stack.append(t)
            
        # Virgule (séparateur d'arguments)
        elif t == ",":
            while stack and stack[-1] != "(":
                out.append(stack.pop())
            if not stack:
                raise ValueError("Virgule mal placée")
            
        # Opérateur
        elif t in OPS:
            if is_unary_minus(i):
                # Traite le moins unaire comme fonction 'neg' 
                stack.append("neg")
            else:
                p1, assoc1, _ = OPS[t]
                while stack and stack[-1] in OPS:
                    p2, assoc2, _ = OPS[stack[-1]]
                    if (assoc1 == LEFT and p1 <= p2) or (assoc1 == RIGHT and p1 < p2):
                        out.append(stack.pop())
                    else:
                        break
                stack.append(t)
                
        # Parenthèse ouvrante
        elif t == "(":
            stack.append(t)
            
        # Parenthèse fermante  
        elif t == ")":
            while stack and stack[-1] != "(":
                out.append(stack.pop())
            if not stack:  
                raise ValueError("Parenthèse mal appariées")
            stack.pop() # Enlève "(" 
            
            # Si une fonction était avant la parenthèse 
            if stack and stack[-1] in FUNCS:
                out.append(stack.pop())
                
        else:
            raise ValueError(f"Token inconnu: {t}")
    
    
    while stack:
        top = stack.pop()
        if top in ("(", ")"):
            raise ValueError("Parenthèse mal appariées")
        out.append(top)
        
    return out

# =====================================
# PARTIE 5 : EVALUATION DE LA NOTATION RPN
# =====================================

def eval_rpn(rpn, ans=None):  
    """
    Evalue une expression en notation polonaise inversée
    Utilise une pile pour l'évaluation
    """
    stack = []
    
    for x in rpn:
        if isinstance(x, (int, float)):
            stack.append(x)
            
        # Opérateur unaire personnalisé 
        elif x == "neg":
            if not stack:
                raise ValueError("Opérateur unaire mal formé")
            stack.append(-stack.pop())
            
        # Opérateur binaire
        elif x in OPS:
            if len(stack) < 2:
                raise ValueError("Expression incomplète")
            b = stack.pop()
            a = stack.pop()  
            try:
                result = OPS[x][2](a, b)
                stack.append(result)
            except ZeroDivisionError:
                raise ZeroDivisionError("Division par zéro")
            
        # Fonction mathématique
        elif x in FUNCS:
            if not stack:
                raise ValueError("Appel de fonction sans argument")
            arg = stack.pop()
            stack.append(FUNCS[x](arg))
            
        # Variable spéciale 'ans'
        elif x == ":ans":
            if ans is None:
                raise ValueError("Pas de valeur précédente (ans)")
            stack.append(ans)
            
        else:
            raise ValueError(f"Symbole inconnu en RPN: {x}")
        
    if len(stack) != 1:
        raise ValueError("Expression invalide")
    
    return stack[0]

# =====================================
# PARTIE 6 : FONCTIONS PRINCIPALES ET INTERFACE 
# =====================================

def eval_expr(s: str, ans=None):  
    """Evalue une expression complète"""
    s = s.replace("ans", ":ans")
    tokens = tokenize(s)
    rpn = infix_to_rpn(tokens)
    return eval_rpn(rpn, ans=ans)

def repl():
    """Interface interactive (Read-Eval-Print-Loop)"""
    print("Calculatrice avancée. Fonctions: abs, sqrt, log, sin, cos, tan, pow")
    print("Constantes: pi, e ; Variable: ans ; Opérateurs: + - * / // % ^")
    print("Tapez :q pour quitter.")  

    ans = None
    while True:
        try:
            s = input(">>> ").strip()
            if s in (":q", ":quit", ":exit"):  
                break
            res = eval_expr(s, ans=ans)
            ans = res
            print(res)
        except Exception as e:
            print(f"Erreur: {e}")
            
def main():
    """Point d'entrée principal"""
    if len(sys.argv) > 1:
        expr = " ".join(sys.argv[1:])
        print(eval_expr(expr))
    else:
        repl()
        
if __name__ == "__main__":
    main()