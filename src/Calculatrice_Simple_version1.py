def calculatrice_basique():
    """
    Version la plus simple possible - Concepts de base
    """
    print("=== CALCULATRICE BASIQUE ===")
    
    while True:
        # SAISIE UTILISATEUR
        try:
            nombre1 = float(input("Entrez le premier nombre: "))
            operateur = input("Entrez l'operateur (+, -, *, /) : ")
            nombre2 = float(input("Entrez le deuxieme nombre: "))
        except ValueError:
            print("Erreur: Veuillez entrer des nombres valides.")
            continue
        
        # CALCUL
        if operateur == "+":
            resultat = nombre1 + nombre2
        elif operateur == "-":
            resultat = nombre1 - nombre2
        elif operateur == "*":
            resultat = nombre1 * nombre2
        elif operateur == "/":
            if nombre2 == 0:
                print("Erreur: Division par zéro.")
                continue
            resultat = nombre1 / nombre2
        else:
            print("Erreur: Operateur non reconnu.")
            continue
        
        # AFFICHAGE 
        print(f"Résultat: {nombre1} {operateur} {nombre2} = {resultat}")
        
        # CONTINUER?
        continuer = input("Nouvelle tentative? (o/n): ").lower()
        if continuer != 'o':
            break
        
if __name__ == "__main__":
    calculatrice_basique()
    
    
    
    