import tkinter as tk
from tkinter import messagebox

class Calculatrice:
    def __init__(self):
        # Création de la fenêtre principale
        self.fenetre = tk.Tk()
        self.fenetre.title("Calculatrice")
        self.fenetre.geometry("300x400")
        self.fenetre.resizable(False, False)
        
        # Variables pour stocker les données
        self.expression = ""  # Stocke l'expression en cours
        self.resultat_var = tk.StringVar()  # Variable pour l'affichage
        
        # Initialisation de l'interface
        self.creer_interface()
    
    def creer_interface(self):
        """Crée tous les éléments de l'interface"""
        # Cadre pour l'affichage
        cadre_affichage = tk.Frame(self.fenetre, height=100)
        cadre_affichage.pack(pady=20, padx=20, fill=tk.X)
        
        # Zone d'affichage du résultat
        self.ecran = tk.Entry(
            cadre_affichage, 
            textvariable=self.resultat_var,
            font=('Arial', 18),
            justify='right',
            state='readonly'
        )
        self.ecran.pack(fill=tk.X, ipady=10)
        
        # Cadre pour les boutons
        cadre_boutons = tk.Frame(self.fenetre)
        cadre_boutons.pack(pady=20, padx=20, expand=True, fill=tk.BOTH)
        
        # Création des boutons
        self.creer_boutons(cadre_boutons)
    
    def creer_boutons(self, parent):
        """Crée la grille des boutons"""
        # Définition des boutons : (texte, ligne, colonne, largeur)
        boutons = [
            ('7', 1, 0, 1), ('8', 1, 1, 1), ('9', 1, 2, 1), ('/', 1, 3, 1),
            ('4', 2, 0, 1), ('5', 2, 1, 1), ('6', 2, 2, 1), ('*', 2, 3, 1),
            ('1', 3, 0, 1), ('2', 3, 1, 1), ('3', 3, 2, 1), ('-', 3, 3, 1),
            ('0', 4, 0, 1), ('.', 4, 1, 1), ('=', 4, 2, 1), ('+', 4, 3, 1),
            ('C', 5, 0, 2), ('⌫', 5, 2, 2)
        ]
        
        # Création de chaque bouton
        for (texte, ligne, colonne, largeur) in boutons:
            bouton = tk.Button(
                parent,
                text=texte,
                font=('Arial', 14),
                command=lambda t=texte: self.clic_bouton(t)
            )
            bouton.grid(
                row=ligne, 
                column=colonne, 
                columnspan=largeur,
                sticky="nsew",
                padx=2, 
                pady=2
            )
        
        # Configuration des poids des lignes/colonnes
        for i in range(6):
            parent.grid_rowconfigure(i, weight=1)
        for i in range(4):
            parent.grid_columnconfigure(i, weight=1)
    
    def clic_bouton(self, valeur):  # ✅ CORRIGÉ : Bonne indentation
        """Gère le clic sur un bouton"""
        try:
            if valeur == '=':
                # Calcule le résultat
                self.calculer()
            elif valeur == 'C':
                # Efface tout
                self.effacer()
            elif valeur == '⌫':
                # Efface le dernier caractère
                self.effacer_dernier()
            else:
                # Ajoute le caractère à l'expression
                self.ajouter_caractere(valeur)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur de calcul: {e}")
    
    def ajouter_caractere(self, caractere):
        """Ajoute un caractère à l'expression"""
        self.expression += str(caractere)
        self.mettre_a_jour_affichage()
    
    def effacer(self):
        """Efface toute l'expression"""
        self.expression = ""
        self.mettre_a_jour_affichage()
    
    def effacer_dernier(self):
        """Efface le dernier caractère"""
        self.expression = self.expression[:-1]
        self.mettre_a_jour_affichage()
    
    def mettre_a_jour_affichage(self):
        """Met à jour l'affichage avec l'expression actuelle"""
        self.resultat_var.set(self.expression)
    
    def calculer(self):  # ✅ CORRIGÉ : Bonne indentation
        """Évalue l'expression mathématique"""
        if not self.expression:
            return
        
        try:
            # Remplace les opérateurs pour la compatibilité Python
            expression_eval = self.expression.replace('×', '*').replace('÷', '/')
            
            # Évaluation sécurisée
            if any(c not in '0123456789+-*/.() ' for c in expression_eval):
                raise ValueError("Caractères non autorisés")
            
            # Calcul du résultat
            resultat = eval(expression_eval)
            
            # Formatage du résultat
            if isinstance(resultat, float):
                resultat = round(resultat, 10)  # Évite les erreurs d'arrondi
            
            self.expression = str(resultat)
            self.mettre_a_jour_affichage()
            
        except ZeroDivisionError:
            messagebox.showerror("Erreur", "Division par zéro impossible!")
            self.effacer()
        except Exception as e:
            messagebox.showerror("Erreur", f"Expression invalide: {e}")
            self.effacer()
    
    def lancer(self):  # ✅ CORRIGÉ : Bonne indentation
        """Lance l'application"""
        self.fenetre.mainloop()

# Point d'entrée du programme  # ✅ CORRIGÉ : En dehors de la classe
if __name__ == "__main__":
    # Création et lancement de la calculatrice
    calc = Calculatrice()
    calc.lancer()