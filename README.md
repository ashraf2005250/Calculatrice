
# 🧮 Calculatrice Scientifique en Python

Une calculatrice **interactive et avancée** développée en Python.  
Elle utilise l’algorithme du **Shunting-Yard (Dijkstra)** pour convertir une expression en notation polonaise inversée (**RPN**), puis l’évalue via une pile.  
Ce projet illustre à la fois la **programmation orientée algorithmique** et la mise en place d’un **interpréteur mathématique**.

---

## 🚀 Fonctionnalités principales

- **Opérateurs pris en charge :**
  - `+` addition  
  - `-` soustraction (y compris le **moins unaire**, ex : `-5`)  
  - `*` multiplication  
  - `/` division réelle  
  - `//` division entière  
  - `%` modulo  
  - `^` ou `**` puissance  

- **Constantes mathématiques :**
  - `pi` (≈ 3.14159)  
  - `e` (≈ 2.71828)  

- **Fonctions mathématiques intégrées :**
  - `abs(x)` : valeur absolue  
  - `sqrt(x)` : racine carrée  
  - `log(x)` : logarithme népérien  
  - `sin(x)`, `cos(x)`, `tan(x)` : trigonométrie  

- **Variable spéciale :**
  - `ans` → stocke le dernier résultat calculé  

- **Mode REPL interactif :**
  - Saisie et évaluation d’expressions mathématiques en boucle  
  - Historique implicite avec la variable `ans`  
  - Quitter avec `:q`, `:quit` ou `:exit`  

---

## 📂 Structure du projet

