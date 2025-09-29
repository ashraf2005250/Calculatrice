def evaluer_expression(expression):
    """
    Evalue une expression simple comme "2 + 5" ou "15 / 5"
    """
    
    # SEPARATION DES ELEMENTS
    elements = expression.split()
    
    # VALIDATION FORMAT
    if len(elements) != 3:
        return "Erreur: Format attendu 'nombre opérateur nombre'"
    
    nombre1_str, operateur, nombre2_str = elements
    
    # CONVERSION EN NOMBRES
    try:
        nombre1 = float(nombre1_str)
        nombre2 = float(nombre2_str)
    except ValueError:
        return "Erreur: Les deux premiers éléments doivent etre des nombres"
    
    # CALCUL
    if operateur == "+":
        return nombre1 + nombre2
    elif operateur == "-":
        return nombre1 - nombre2
    elif operateur == "*":
        return nombre1 * nombre2
    elif operateur == "/":
        if nombre2 == 0:
            return "Erreur: Division par zéro"
        return nombre1 / nombre2
    else:
        return f"Erreur: Operateur '{operateur}' non supporté"
    
def calculatrice_expression():
        """
        Version avec traitement d'expression complète
        """
        print("============= CALCULATRICE ============")
        print("Exemple: tapez '2 + 3' puis Entrée")
        
        while True:
            expression = input(">>> ").strip()
            
            if expression.lower() in ('quit', 'exit', 'q'):
                break
            
            if not expression:
                continue
            
            resultat = evaluer_expression(expression)
            print(f"= {resultat}")
            
if __name__ == "__main__":
        calculatrice_expression()
    