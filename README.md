# Modèle de Taux Directeur de Banque Centrale

Ce projet est une implémentation d'un modèle de taux directeur de banque centrale en Python. Le modèle est conçu pour aider à déterminer le taux directeur optimal en fonction de divers paramètres économiques tels que le PIB, l'inflation, la dette publique, etc.

## Prérequis

Assurez-vous d'avoir Python installé sur votre système.

Ensuite, installez les bibliothèques requises :

pip install numpy pandas matplotlib


## Fonctionnalités

- **Calcul du Taux Directeur avec Valeurs Données**
  - Demande à l'utilisateur de fournir des valeurs telles que le PIB, le taux directeur précédent, la réponse à l'inflation, et la dette publique pour calculer le taux directeur recommandé.

- **Observation de l'Impact d'une Variable sur le Taux Directeur**
  - Permet à l'utilisateur de choisir une variable (PIB, taux directeur précédent, réponse à l'inflation, dette publique, inflation) et observe son impact sur le taux directeur via des graphiques.

- **Courbe du Taux Directeur de la BCE sur une Période Choisie**
  - Charge les données historiques du taux directeur de la BCE à partir d'un fichier texte et affiche l'évolution du taux directeur au fil du temps.

- **Scénarios Catastrophe**
  - Propose différents scénarios catastrophes (hyperinflation, récession soudaine, crise de la dette souveraine) où le modèle ajuste le taux directeur en conséquence.

- **Définition des Variables**
  - Fournit une explication des différentes variables utilisées dans le modèle.

## Utilisation

1. Exécutez le fichier `ppe.py`.
2. Suivez les instructions du menu principal pour choisir l'opération souhaitée.
3. Fournissez les données nécessaires lorsque demandé.
4. Visualisez les résultats via des graphiques ou des affichages de texte.

## Auteur

Ce projet a été développé par le groupe #PPE23-R-193.

N'hésitez pas à explorer et à utiliser ce modèle pour mieux comprendre les déterminants du taux directeur d'une banque centrale.