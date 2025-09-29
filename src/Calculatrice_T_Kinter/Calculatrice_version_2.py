import tkinter as tk
from tkinter import messagebox
import math

class CalculatriceAmelioree:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Calculatrice Évoluée")
        self.fenetre.geometry("350x500")
        self.fenetre.configure(bg='#2C2C2C')
        
        # État de la calculatrice
        self.expression = ""
        self.resultat_var = tk.StringVar(value="0")
        
        self.creer_interface()
        self.configurer_raccourcis()
    
    def creer_interface(self):
        """Interface avec style moderne"""
        # Affichage
        ecran = tk.Entry(
            self.fenetre,
            textvariable=self.resultat_var,
            font=('Arial', 20, 'bold'),
            justify='right',
            state='readonly',
            bg='#1A1A1A',
            fg='white',
            bd=0
        )
        ecran.pack(pady=20, padx=20, fill=tk.X, ipady=15)
        
        # Cadre des boutons
        cadre_boutons = tk.Frame(self.fenetre, bg='#2C2C2C')
        cadre_boutons.pack(pady=10, padx=20, expand=True, fill=tk.BOTH)
        
        # Boutons avec couleurs différentes
        boutons_speciaux = {'C': '#FF6B6B', '⌫': '#4ECDC4', '=': '#45B7D1'}
        boutons_normaux = {
            '7': '#3D3D3D', '8': '#3D3D3D', '9': '#3D3D3D', '/': '#FFA726',
            '4': '#3D3D3D', '5': '#3D3D3D', '6': '#3D3D3D', '*': '#FFA726', 
            '1': '#3D3D3D', '2': '#3D3D3D', '3': '#3D3D3D', '-': '#FFA726',
            '0': '#3D3D3D', '.': '#3D3D3D', '+': '#FFA726'
        }
        
        boutons = [
            ('C', 0, 0, 1, boutons_speciaux['C']), 
            ('⌫', 0, 1, 1, boutons_speciaux['⌫']),
            ('/', 0, 2, 1, boutons_normaux['/']), 
            ('*', 0, 3, 1, boutons_normaux['*']),
            ('7', 1, 0, 1, boutons_normaux['7']), 
            ('8', 1, 1, 1, boutons_normaux['8']),
            ('9', 1, 2, 1, boutons_normaux['9']), 
            ('-', 1, 3, 1, boutons_normaux['-']),
            ('4', 2, 0, 1, boutons_normaux['4']), 
            ('5', 2, 1, 1, boutons_normaux['5']),
            ('6', 2, 2, 1, boutons_normaux['6']), 
            ('+', 2, 3, 1, boutons_normaux['+']),
            ('1', 3, 0, 1, boutons_normaux['1']), 
            ('2', 3, 1, 1, boutons_normaux['2']),
            ('3', 3, 2, 1, boutons_normaux['3']), 
            ('=', 3, 3, 1, boutons_speciaux['=']),
            ('0', 4, 0, 2, boutons_normaux['0']), 
            ('.', 4, 2, 1, boutons_normaux['.'])
        ]
        
        for (texte, ligne, colonne, largeur, couleur) in boutons:
            bouton = tk.Button(
                cadre_boutons,
                text=texte,
                font=('Arial', 14, 'bold'),
                bg=couleur,
                fg='white',  # ✅ CORRIGÉ : Simplifié la condition
                relief='flat',
                command=lambda t=texte: self.clic_bouton(t)
            )
            bouton.grid(
                row=ligne, column=colonne, columnspan=largeur,
                sticky="nsew", padx=2, pady=2, ipady=10
            )
        
        for i in range(5):
            cadre_boutons.grid_rowconfigure(i, weight=1)
        for i in range(4):
            cadre_boutons.grid_columnconfigure(i, weight=1)
    
    def configurer_raccourcis(self):
        """Configure les raccourcis clavier"""
        touches = [str(i) for i in range(10)] + ['+', '-', '*', '/', '.', '=']
        for touche in touches:
            self.fenetre.bind(touche, lambda e, t=touche: self.clic_bouton(t))
        
        self.fenetre.bind('<Return>', lambda e: self.clic_bouton('='))
        self.fenetre.bind('<BackSpace>', lambda e: self.clic_bouton('⌫'))
        self.fenetre.bind('<Escape>', lambda e: self.clic_bouton('C'))
        self.fenetre.bind('<KeyPress>', self.verifier_touche)
    
    def verifier_touche(self, event):
        """Empêche la saisie directe dans le champ"""
        if event.char in '0123456789+-*/.':
            return "break"
    
    # ✅ AJOUT : Méthodes manquantes pour que la calculatrice fonctionne
    def clic_bouton(self, valeur):
        """Gère le clic sur un bouton"""
        try:
            if valeur == '=':
                self.calculer()
            elif valeur == 'C':
                self.effacer()
            elif valeur == '⌫':
                self.effacer_dernier()
            else:
                self.ajouter_caractere(valeur)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur: {e}")
    
    def ajouter_caractere(self, caractere):
        """Ajoute un caractère à l'expression"""
        if self.expression == "0" or self.expression == "Erreur":
            self.expression = ""
        self.expression += str(caractere)
        self.mettre_a_jour_affichage()
    
    def effacer(self):
        """Efface toute l'expression"""
        self.expression = ""
        self.resultat_var.set("0")
    
    def effacer_dernier(self):
        """Efface le dernier caractère"""
        self.expression = self.expression[:-1]
        if not self.expression:
            self.resultat_var.set("0")
        else:
            self.mettre_a_jour_affichage()
    
    def mettre_a_jour_affichage(self):
        """Met à jour l'affichage"""
        self.resultat_var.set(self.expression)
    
    def calculer(self):
        """Évalue l'expression mathématique"""
        if not self.expression:
            return
        
        try:
            # Évaluation sécurisée
            if any(c not in '0123456789+-*/.() ' for c in self.expression):
                raise ValueError("Caractères non autorisés")
            
            # Calcul du résultat
            resultat = eval(self.expression)
            
            # Formatage
            if isinstance(resultat, float):
                resultat = round(resultat, 10)
            
            self.expression = str(resultat)
            self.resultat_var.set(self.expression)
            
        except ZeroDivisionError:
            messagebox.showerror("Erreur", "Division par zéro!")
            self.expression = ""
            self.resultat_var.set("Erreur")
        except Exception as e:
            messagebox.showerror("Erreur", f"Expression invalide: {e}")
            self.expression = ""
            self.resultat_var.set("Erreur")
    
    def lancer(self):
        """Lance l'application"""
        self.fenetre.mainloop()

if __name__ == "__main__":
    calc = CalculatriceAmelioree()
    calc.lancer()