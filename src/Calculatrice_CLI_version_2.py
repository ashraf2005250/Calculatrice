
"""
Calculatrice utilisant l' AST ( Abstract Syntax Tree) de Python
Permet d'evaluer des expressions mathématiques de manière sécurisée
"""
import ast
import operator
import sys

#==================================================
# PARTIE 1 : DEFINITION DES OPERATIONS ET CONSTANTES 
#==================================================

class CalculatriceAST:
    def __init__(self):
        # Dictionnaire faisant le lien entre les noeuds AST et les opérateurs Python
        self.BIN_OPS = {
            ast.Add: operator.add,   # Addition: +
            ast.Sub: operator.sub,   # Soustraction: -
            ast.Mult: operator.mul,  # Multiplication: *
            ast.Div: operator.truediv,  # Division: /
            ast.FloorDiv: operator.floordiv,  # Division entiere: //
            ast.Mod: operator.mod,  # Modulo: %
            ast.Pow: operator.pow,  # Puissance: **
        }
        
        # Opérateurs unaires ( appliqués à un seul opérande)
        self.UNARY_OPS = {
            ast.UAdd: operator.pos,  # Plus unaire: +5
            ast.USub: operator.neg   # Moins unaire:  -3
        }
        
        # Constantes mathématiques prédéfinies
        self.CONSTANTES = {
            'pi': 3.141592653589793,
            'e': 2.718281828459045
        }
        
        # Stocke le dernier résultat pour la variable 'ans'
        self.ans = None
        
        
    # ==================================================
    
    # PARTIE 2 : EVALUATION RECURSIVE DE L' ARBRE SYNTAXIQUE
    # ==================================================
    
    def eval_ast(self, node):
        """
        Parcourt récursivement l'AST et évalue chaque noeurd
        C'est le COEUR ALGORITHMIQUE de la calculatrice
        """
        
        # 2.1: Noeud racine Expression - on descend dans le corps 
        if isinstance(node, ast.Expression):
            return self.eval_ast(node.body)
        
        # 2.2: Opération binaire (ex: 2 + 3, 4 * 5)
        elif isinstance(node, ast.BinOp):
            # Evalue récursivement le coté gauche
            left = self.eval_ast(node.left)
            # Evalue récursivement le coté droit
            right = self.eval_ast(node.right)
            
            # Récupère le type d'opérateur
            op_type = type(node.op)
            
            # Vérifie si l'opérateur est autorisé
            if op_type not in self.BIN_OPS:
                raise ValueError(f"Opérateur non supporté: {op_type.__name__}")
            
            # Applique l'opération correspondante
            return self.BIN_OPS[op_type](left, right)
        
        # 2.3: Opération unaire (ex: -5, +10)
        elif isinstance(node, ast.UnaryOp):
            # Evalue l'opérande 
            operand = self.eval_ast(node.operand)
            op_type = type(node.op)
            
            if op_type not in self.UNARY_OPS:
                raise ValueError(f"Opérateur unaire non supporté: {op_type.__name__}")
            
            return self.UNARY_OPS[op_type](operand)
        
        # 2.4: Constante numérique (int ou float)
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Constante non numérique")
        
        # 2.5: Variable ou constante ( ex: pi, e, ans)
        elif isinstance(node, ast.Name):
            if node.id in self.CONSTANTS:
                return self.CONSTANTS[node.id]
            elif node.id == 'ans' and self.ans is not None:
                return self.ans
            raise ValueError(f"Variable inconnue: {node.id}")
        else:
            raise ValueError(f"Type de noeur non supporté: {type(node).__name__}")
        
        
    # ==================================================
    
    # PARTIE 3 : SECURITE ET VALIDATION DES EXPRESSIONS
    
    # ===================================================
    
    def safe_eval(self, expr: str) -> float:
        
        """
        Evalue une expression mathématique de manière sécurisée
        """
        
        # 3.1: Validation des caractères autorisés (sécurité)
        allowed_chars = set("0123456789+-*/.()% pi e ans ")
        if not all(c in allowed_chars for c in expr.replace(' ', '' )):
            raise ValueError("Caractères non autorisés dans l'expression")
        
        # 3.2: Parsing de l'expression en AST
        tree = ast.parse(expr, mode='eval')
        
        # 3.3: Evaluation récursive de l'AST
        return self.eval_ast(tree)
    
    
    # ======================================================
    
    # PARTIE 4 : INTERFACE EN LIGNE DE COMMANDE (CLI)
    
    # ======================================================    
    
    def repl(self):
        
        """
        Read-Eval-Print-Loop: Interface interactive ligne de commande
        """
        
        print("Calculatrice AST Avancée")
        print("Commandes : :q pour quitter, :ans pour le résultat précédent")
        print("Exemples: 2 + 3 * 4, - 5 + 6, pi % 3")
        
        while True:
            
            try:
                # 4.1 : Lecture de l'entrée utilisateur
                s = input(">>> ").strip()
                
                
                # Gestion des entrées vides 
                if not s:
                    continue
                
                # 4.2 : Commandes spéciales
                if s in ("q", "quit", ":exit"):
                    break
                if s == ":ans":
                    if self.ans is not None:
                        print(f"Résulat précédent: {self.ans}")
                    else:
                        print("Aucun résultat précédent")
                    continue
                
                # 4.3 : Evaluation et affichage du résulat
                result = self.safe_eval(s)
                self.ans = result # Memorise pour le prochaine fois
                
                print(f"= {result}")
                
             # 4.4 : Gestion robuste des erreurs 
            except KeyboardInterrupt:
                print("\nAu revoir !")
                break
                    
            except Exception as e:
                print(f"Erreur: {e}")
                
                
# =====================================================

# PARTIE 5 : POINT D'ENTREE PRINCIPAL
# =====================================================

def main():
    # 5.1: Création de l'instance de la calculatrice
    calc = CalculatriceAST()
    
    # 5.2: Mode Ligne de Commande 
    
    if len(sys.argv) > 1:
        try:
            expression = " ".join(sys.argv[1:])
            result = calc.safe_eval(expression)
            print(result)
        except Exception as e:
            print(f"Erreur: {e}")
            sys.exit(1)
            
    # 5.3: Mode interactif
    else:
        calc.repl()
        
if __name__ == "__main__":
    main()
                
                
                
            