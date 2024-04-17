import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


# On définit une fonction qui nous affichera le Menu
def Afficher_Menu():
    print("Menu Principal")
    print("1) Calcul du Taux Directeur avec valeur données")
    print("2) Observer l'impact d'une variable sur le taux directeur")
    print("3) Effectuer la courbe du taux directeur de la BCE sur une période choisie")
    print("4) Scénario 'catastrophe'")
    print("5) Définition des variables")
    choix = input("Que voulez vous faire ? : ")
    return choix


def main():
    while True:

        choix = Afficher_Menu()

        if choix == "1":
            # Définition des paramètres
            coefficient1 = 0.7  # Constante définis
            coefficient2 = 2  # Constante définis
            tauxCroissanceReel = 0.02  # Objectif 2%
            tauxInflation = 0.03  # Objectif 3%
            elasticite = 0.02  # Variation 2 2 point par pourcentage
            ratioDeficitPIB = 0.8  # Objectif à 80%
            tauxInteretReelPolitiqueMonetaire = 0.03  # Objectif à 3%

            PIB = float(input("Entrez le PIB: "))
            tauxDirecteurPrecedent = float(input("Entrez le taux directeur precedent (%): ")) / 100
            reponseInflation = float(input("Entrez le taux de réponse à l'inflation (%): ")) / 100
            DettePublique = float(input("Entrez la Dette Publique : "))

            # Calul des paramètres intermédiaire
            ratioDettePubliquePIB = DettePublique / PIB
            valeurEtatStable = (ratioDeficitPIB / 4) * (
                        tauxCroissanceReel * tauxInflation / (tauxCroissanceReel * tauxInflation - 1))

            # Calcul du taux directeur
            tauxDirecteur = (
                    (tauxDirecteurPrecedent) ** coefficient1 *
                    ((tauxCroissanceReel * tauxInflation * (1 + elasticite *
                                                            (ratioDettePubliquePIB - valeurEtatStable))) /
                     tauxInteretReelPolitiqueMonetaire)*(1 - coefficient1) *
                    (reponseInflation / tauxInflation * 4) * (((1 - coefficient1) * coefficient2) / 4)
            )

            # Affichage du résultat
            print(f"Le taux directeur recommandé est de {tauxDirecteur * 100:.2f} %\n\n\n\n")

        if choix == "2":

            # Définition des paramètres
            coefficient1 = 0.7  # Constante définis
            coefficient2 = 2  # Constante définis
            tauxCroissanceReel = 0.02  # Objectif 2%
            tauxInflation = 0.03  # Objectif 3%
            elasticite = 0.02  # Variation 2 2 point par pourcentage
            ratioDeficitPIB = 0.8  # Objectif à 80%
            tauxInteretReelPolitiqueMonetaire = 0.03  # Objectif à 3%

            print("1) PIB")
            print("2) Taux Directeur Précédent")
            print("3) Reponse à l'inflation")
            print("4) Dette Publique")
            print("5) Inflation")

            variable = float(input("Observer l'évolution du taux directeur en fontion de quelle variable ? :"))

            # On observe l'évolution du taux Directeur en fonction du PIB
            if variable == 1:

                tauxDirecteurPrecedent = float(input("Entrez le taux directeur precedent (%): ")) / 100
                reponseInflation = float(input("Entrez le taux de réponse à l'inflation (%): ")) / 100
                DettePublique = float(input("Entrez la Dette Publique : "))

                # Définition d'un tableau Numpy le PIB
                # Dans notre cas un PIB allant de 500 Milliards à 3 Trillions de 100 points
                Valeur_PIB = np.linspace(500000000000, 3000000000000, 100)

                # On initialise une liste vide afin de stocker les valeurs du taux directeur
                # par rapport à chaque valeur du PIB définit précédemment
                Liste_tauxDirecteur = []

                # On remplit le tableau
                for PIB in Valeur_PIB:
                    # Calul des paramètres intermédiaire
                    ratioDettePubliquePIB = DettePublique / PIB
                    valeurEtatStable = (ratioDeficitPIB / 4) * (
                                tauxCroissanceReel * tauxInflation / (tauxCroissanceReel * tauxInflation - 1))

                    # Calcul du taux directeur
                    tauxDirecteur = (
                            (tauxDirecteurPrecedent) ** coefficient1 *
                            ((tauxCroissanceReel * tauxInflation * (1 + elasticite *
                                                                    (ratioDettePubliquePIB - valeurEtatStable))) /
                             tauxInteretReelPolitiqueMonetaire)*(1 - coefficient1) *
                            (reponseInflation / tauxInflation * 4) * (((1 - coefficient1) * coefficient2) / 4)
                    )

                    Liste_tauxDirecteur.append(tauxDirecteur)

                # On affiche
                plt.figure(figsize=(10, 6))
                plt.plot(Valeur_PIB, Liste_tauxDirecteur, linestyle='-', color='blue', linewidth=2)

                # On affiche le graphique

                plt.xlabel('PIB', fontsize=12, fontweight='bold')
                plt.ylabel('Taux Directeur', fontsize=12, fontweight='bold')
                plt.title('Évolution du taux directeur en fonction du PIB', fontsize=14, fontweight='bold')
                plt.grid(True)
                plt.xticks(fontweight='bold')
                plt.yticks(fontweight='bold')

                plt.tight_layout()

                plt.show()

            # On observe l'évolution du taux Directeur en fonction du taux Directeur Précédent
            if variable == 2:

                PIB = float(input("Entrez le PIB: "))
                reponseInflation = float(input("Entrez le taux de réponse à l'inflation (%): ")) / 100
                DettePublique = float(input("Entrez la Dette Publique : "))

                # Définition d'un tableau Numpy le taux Directeur précédent
                # Dans notre cas un taux allant de 0.5% à 5% avec 100 points
                Valeur_tauxDirecteurPrecedent = np.linspace(0.5, 5, 100)

                # On initialise une liste vide afin de stocker les valeurs du taux directeur
                # par rapport à chaque valeur du taux Directeur précédent définit précédemment
                Liste_tauxDirecteur = []

                for tauxDirecteurPrecedent in Valeur_tauxDirecteurPrecedent:
                    # Calul des paramètres intermédiaire
                    ratioDettePubliquePIB = DettePublique / PIB
                    valeurEtatStable = (ratioDeficitPIB / 4) * (
                                tauxCroissanceReel * tauxInflation / (tauxCroissanceReel * tauxInflation - 1))

                    # Calcul du taux directeur
                    tauxDirecteur = (
                            (tauxDirecteurPrecedent) ** coefficient1 *
                            ((tauxCroissanceReel * tauxInflation * (1 + elasticite *
                                                                    (ratioDettePubliquePIB - valeurEtatStable))) /
                             tauxInteretReelPolitiqueMonetaire)*(1 - coefficient1) *
                            (reponseInflation / tauxInflation * 4) * (((1 - coefficient1) * coefficient2) / 4)
                    )

                    Liste_tauxDirecteur.append(tauxDirecteur)

                # On affiche avec plot
                plt.figure(figsize=(10, 6))
                plt.plot(Valeur_tauxDirecteurPrecedent, Liste_tauxDirecteur, linestyle='-', color='green', linewidth=2)
                plt.xlabel('Taux Directeur Précédent', fontsize=12, fontweight='bold')
                plt.ylabel('Taux Directeur', fontsize=12, fontweight='bold')
                plt.title('Évolution du taux directeur en fonction du taux Directeur précédent', fontsize=14,
                          fontweight='bold')
                plt.grid(True)
                plt.xticks(fontweight='bold')
                plt.yticks(fontweight='bold')

                plt.tight_layout()
                plt.show()

            # On observe l'évolution du taux Directeur en fonction de la Réponse à l'Inflation
            if variable == 3:

                PIB = float(input("Entrez le PIB: "))
                tauxDirecteurPrecedent = float(input("Entrez le taux directeur precedent (%): ")) / 100
                DettePublique = float(input("Entrez la Dette Publique : "))

                # Définition d'un tableau Numpy pour la réponse à l'inflation
                # Dans notre cas un taux allant de 0.5% à 2% avec 100 points
                Valeur_reponseInflation = np.linspace(0.5, 5, 100)

                # On initialise une liste vide afin de stocker les valeurs du taux directeur
                # par rapport à chaque valeur du taux de la réponse à l'Inflation définit précédemment
                Liste_tauxDirecteur = []

                for reponseInflation in Valeur_reponseInflation:
                    # Calul des paramètres intermédiaire
                    ratioDettePubliquePIB = DettePublique / PIB
                    valeurEtatStable = (ratioDeficitPIB / 4) * (
                                tauxCroissanceReel * tauxInflation / (tauxCroissanceReel * tauxInflation - 1))

                    # Calcul du taux directeur
                    tauxDirecteur = (
                            (tauxDirecteurPrecedent) ** coefficient1 *
                            ((tauxCroissanceReel * tauxInflation * (1 + elasticite *
                                                                    (ratioDettePubliquePIB - valeurEtatStable))) /
                             tauxInteretReelPolitiqueMonetaire)*(1 - coefficient1) *
                            (reponseInflation / tauxInflation * 4) * (((1 - coefficient1) * coefficient2) / 4)
                    )

                    Liste_tauxDirecteur.append(tauxDirecteur)

                # On affiche le graphe
                plt.figure(figsize=(10, 6))
                plt.plot(Valeur_reponseInflation, Liste_tauxDirecteur, linestyle='-', color='orange', linewidth=2)

                # On affcihe en gras, on met les titres ect...
                plt.xlabel('Réponse à Inflation', fontsize=12, fontweight='bold')
                plt.ylabel('Taux Directeur', fontsize=12, fontweight='bold')
                plt.title('Évolution du taux directeur en fonction de la Réponse à Inflation', fontsize=14,
                          fontweight='bold')
                plt.grid(True)
                plt.xticks(fontweight='bold')
                plt.yticks(fontweight='bold')

                plt.tight_layout()
                plt.show()

            # On observe l'évolution du taux Directeur en fonction de la Dette Publique
            if variable == 4:

                PIB = float(input("Entrez le PIB: "))
                tauxDirecteurPrecedent = float(input("Entrez le taux directeur precedent (%): ")) / 100
                reponseInflation = float(input("Entrez le taux de réponse à l'inflation (%): ")) / 100

                # Définition d'un tableau Numpy la Dette Publique
                # Dans notre cas une valeure allant de 500000000000 à 3000000000000$ du PIB avec 100 points
                Valeur_DettePublique = np.linspace(500000000000, 3000000000000, 100)

                # On initialise une liste vide afin de stocker les valeurs du taux directeur
                # par rapport à chaque valeur de la Dette Publique définit précédemment
                Liste_tauxDirecteur = []

                for DettePublique in Valeur_DettePublique:
                    # Calul des paramètres intermédiaire
                    ratioDettePubliquePIB = DettePublique / PIB
                    valeurEtatStable = (ratioDeficitPIB / 4) * (
                                tauxCroissanceReel * tauxInflation / (tauxCroissanceReel * tauxInflation - 1))

                    # Calcul du taux directeur
                    tauxDirecteur = (
                            (tauxDirecteurPrecedent) ** coefficient1 *
                            ((tauxCroissanceReel * tauxInflation * (1 + elasticite *
                                                                    (ratioDettePubliquePIB - valeurEtatStable))) /
                             tauxInteretReelPolitiqueMonetaire)*(1 - coefficient1) *
                            (reponseInflation / tauxInflation * 4) * (((1 - coefficient1) * coefficient2) / 4)
                    )

                    Liste_tauxDirecteur.append(tauxDirecteur)

                # On affiche le graphique
                plt.figure(figsize=(10, 6))
                plt.plot(Valeur_DettePublique, Liste_tauxDirecteur, linestyle='-', color='red', linewidth=2)
                plt.xlabel('Dette Publique', fontsize=12, fontweight='bold')
                plt.ylabel('Taux Directeur', fontsize=12, fontweight='bold')
                plt.title('Évolution du taux directeur en fonction de la Dette Publique', fontsize=14,
                          fontweight='bold')
                plt.grid(True)
                plt.xticks(fontweight='bold')
                plt.yticks(fontweight='bold')

                plt.tight_layout()
                plt.show()

            if variable == 5:

                PIB = float(input("Entrez le PIB: "))
                tauxDirecteurPrecedent = float(input("Entrez le taux directeur precedent (%): ")) / 100
                reponseInflation = float(input("Entrez le taux de réponse à l'inflation (%): ")) / 100
                DettePublique = float(input("Entrez la Dette Publique: "))

                # Définition d'un tableau Numpy le taux d'Inflation
                # Dans notre cas une valeure allant de 1% à 20% du taux d'Inflation avec 100 points
                Valeur_tauxInflation = np.linspace(0.01, 0.2, 100)

                # On initialise une liste vide afin de stocker les valeurs du taux directeur
                # par rapport à chaque valeur du taux d'Inflation définit précédemment
                Liste_tauxDirecteur = []

                for tauxInflation in Valeur_tauxInflation:
                    # Calul des paramètres intermédiaire
                    ratioDettePubliquePIB = DettePublique / PIB
                    valeurEtatStable = (ratioDeficitPIB / 4) * (
                                tauxCroissanceReel * tauxInflation / (tauxCroissanceReel * tauxInflation - 1))

                    # Calcul du taux directeur
                    tauxDirecteur = (
                            (tauxDirecteurPrecedent) ** coefficient1 *
                            ((tauxCroissanceReel * tauxInflation * (1 + elasticite *
                                                                    (ratioDettePubliquePIB - valeurEtatStable))) /
                             tauxInteretReelPolitiqueMonetaire)*(1 - coefficient1) *
                            (reponseInflation / tauxInflation * 4) * (((1 - coefficient1) * coefficient2) / 4)
                    )

                    Liste_tauxDirecteur.append(tauxDirecteur)

                # On affiche le graphique
                plt.figure(figsize=(10, 6))
                plt.plot(Valeur_tauxInflation, Liste_tauxDirecteur, linestyle='-', color='blue', linewidth=2)
                plt.xlabel('Taux Inflation', fontsize=12, fontweight='bold')
                plt.ylabel('Taux Directeur', fontsize=12, fontweight='bold')
                plt.title('Évolution du taux directeur en fonction du taux Inflation', fontsize=14, fontweight='bold')
                plt.grid(True)
                plt.xticks(fontweight='bold')
                plt.yticks(fontweight='bold')

                plt.tight_layout()
                plt.show()

        if choix == "3":

            # On charge le txt qui contient les valeurs réelles du taux directeur
            # Dans le temps
            name_file = 'Data.txt'
            columns = ['Date', 'Taux directeur %']
            data_in = pd.read_csv(name_file, names=columns, sep=' ')

            # On affecte toute les dates et toutes les valeurs de taux dans des numpy différents
            Date = np.asarray([datetime.strptime(date, "%d/%m/%Y") for date in data_in['Date']])
            Taux = np.asarray(data_in['Taux directeur %'])

            # Affichage des choix de dates avec compteur
            for i, value in enumerate(Date):
                print(f"{i}) Date {value.strftime('%d/%m/%Y')}")

            DateChoix = int(input("A partir de quelle date voulez commencer la courbe ? : "))
            # Création de 2 nouveaux numpy avec les valeurs finales
            Date1 = Date[DateChoix:]
            Taux1 = Taux[DateChoix:]

            # On affiche le graphique avec améliorations
            plt.figure(figsize=(10, 6))  # Ajuste la taille du graphique

            plt.plot(Date1, Taux1, linestyle='-', color='red', label='Taux directeur')

            plt.xlabel('Date', fontsize=12, fontweight='bold')
            plt.ylabel('Taux directeur %', fontsize=12, fontweight='bold')
            plt.title('Évolution du taux directeur de la BoE', fontsize=14, fontweight='bold')

            # On améliore l'affichage de la courbe
            # On ajoute une grille
            plt.grid(True)

            # On ajoute une légende
            plt.legend()

            # On ajuste le layout
            plt.tight_layout()

            # On améliore l'affichage avec des contours en gras
            plt.gca().spines['top'].set_linewidth(2)
            plt.gca().spines['bottom'].set_linewidth(2)
            plt.gca().spines['left'].set_linewidth(2)
            plt.gca().spines['right'].set_linewidth(2)

            # On met en gras les étiquettes
            plt.xticks(fontweight='bold')
            plt.yticks(fontweight='bold')
            plt.show()

        if choix == "4":

            # Cas où le Taux Inflation très élevé, Taux direcetur précédent bas
            # et taux d'intérêt réel Politique Monétaire négatif car inflation élevée
            print("1) Hyperinflation et Perte de Confiance : ")
            # Cas où le PIB baisse, Dette Publique augmente en % du PIB
            # et taux croissance réel négatif
            print("2) Récession Soudaine")
            # Dette Publique très élevée comparé au PIB, Ratio/Déficit PIB élevé
            # Réponse à l'inflation faible car taux d'intérêt bas
            print("3) Crise de la Dette Souveraine")

            choix1 = input("Que voulez vous faire ? : ")

            if choix1 == "1":
                # Définition des paramètres
                coefficient1 = 0.7  # Constante définis
                coefficient2 = 2  # Constante définis
                tauxCroissanceReel = 0.02  # Objectif 2%
                elasticite = 0.02  # Variation 2 2 point par pourcentage
                ratioDeficitPIB = 0.8  # Objectif à 80%
                PIB = 3000000000000
                DettePublique = 2000000000000
                reponseInflation = 0.01

                tauxInflation = float(input("Entrez le taux d'inflation (Supérieur à 50%): ")) / 100
                tauxDirecteurPrecedent = float(
                    input("Entrez le taux directeur precedent (Comprit entre 2 et 5%): ")) / 100
                tauxInteretReelPolitiqueMonetaire = float(
                    input("Entrez le taux d'intérêt réel Politique Monétaire (Très bas max 1%): ")) / 100

                # Calul des paramètres intermédiaire
                ratioDettePubliquePIB = DettePublique / PIB
                valeurEtatStable = (ratioDeficitPIB / 4) * (
                            tauxCroissanceReel * tauxInflation / (tauxCroissanceReel * tauxInflation - 1))

                # Calcul du taux directeur
                tauxDirecteur = (
                        (tauxDirecteurPrecedent) ** coefficient1 *
                        ((tauxCroissanceReel * tauxInflation * (1 + elasticite *
                                                                (ratioDettePubliquePIB - valeurEtatStable))) /
                         tauxInteretReelPolitiqueMonetaire)*(1 - coefficient1) *
                        (reponseInflation / tauxInflation * 4) * (((1 - coefficient1) * coefficient2) / 4)
                )

                # Affichage du résultat
                print(
                    f"Le taux directeur recommandé lors d'une telle catastrophe est de {tauxDirecteur * 100:.2f} %\n\n\n\n")

            if choix1 == "2":
                # Définition des paramètres
                coefficient1 = 0.7  # Constante définis
                coefficient2 = 2  # Constante définis
                elasticite = 0.02  # Variation 2 2 point par pourcentage
                ratioDeficitPIB = 0.8  # Objectif à 80%
                reponseInflation = 0.01
                tauxInflation = 0.03
                tauxDirecteurPrecedent = 0.02
                tauxInteretReelPolitiqueMonetaire = 0.03
                PIB = 3000000000000
                DettePublique = 2000000000000

                PIB = float(input("Entrez la diminution du PIB (En % entre 2 et 10%): ")) / 100 * PIB
                DettePublique = float(
                    input("Entrez l'augmentation de la Dette Publique (Comprit entre 20 et 40%): ")) / 100 * PIB
                tauxCroissanceReel = float(input("Entrez le taux de Croissance Réel (Très très faible max 1%): ")) / 100

                # Calul des paramètres intermédiaire
                ratioDettePubliquePIB = DettePublique / PIB
                valeurEtatStable = (ratioDeficitPIB / 4) * (
                            tauxCroissanceReel * tauxInflation / (tauxCroissanceReel * tauxInflation - 1))

                # Calcul du taux directeur
                tauxDirecteur = (
                        (tauxDirecteurPrecedent) ** coefficient1 *
                        ((tauxCroissanceReel * tauxInflation * (1 + elasticite *
                                                                (ratioDettePubliquePIB - valeurEtatStable))) /
                         tauxInteretReelPolitiqueMonetaire)*(1 - coefficient1) *
                        (reponseInflation / tauxInflation * 4) * (((1 - coefficient1) * coefficient2) / 4)
                )

                # Affichage du résultat
                print(
                    f"Le taux directeur recommandé lors d'une telle catastrophe est de {tauxDirecteur * 100:.2f} %\n\n\n\n")

            if choix1 == "3":
                # Définition des paramètres
                coefficient1 = 0.7  # Constante définis
                coefficient2 = 2  # Constante définis
                elasticite = 0.02  # Variation 2 2 point par pourcentage
                tauxCroissanceReel = 0.02  # Objectif 2%
                ratioDeficitPIB = 0.8
                reponseInflation = 0.01
                tauxInflation = 0.03
                tauxDirecteurPrecedent = 0.02
                tauxInteretReelPolitiqueMonetaire = 0.03
                PIB = 3000000000000

                DettePublique = float(
                    input("Entrez la valeure de la Dette Publique comparé au PIB (En % minimum 80%): ")) * PIB / 100

                # Calul des paramètres intermédiaire
                ratioDettePubliquePIB = DettePublique / PIB
                valeurEtatStable = (ratioDeficitPIB / 4) * (
                            tauxCroissanceReel * tauxInflation / (tauxCroissanceReel * tauxInflation - 1))

                # Calcul du taux directeur
                tauxDirecteur = (
                        (tauxDirecteurPrecedent) ** coefficient1 *
                        ((tauxCroissanceReel * tauxInflation * (1 + elasticite *
                                                                (ratioDettePubliquePIB - valeurEtatStable))) /
                         tauxInteretReelPolitiqueMonetaire)*(1 - coefficient1) *
                        (reponseInflation / tauxInflation * 4) * (((1 - coefficient1) * coefficient2) / 4)
                )

                # Affichage du résultat
                print(
                    f"Le taux directeur recommandé lors d'une telle catastrophe est de {tauxDirecteur * 100:.2f} %\n\n\n")

        if choix == "5":

            print(
                "tauxCroissanceReel: Taux de croissance du Produit Intérieur Brut (PIB) réel, ajusté pour l'inflation, sur une période donnée.\n\n")
            print(
                "tauxInflation: Taux de variation annuel de l'indice des prix à la consommation, reflétant la diminution du pouvoir d'achat de la monnaie.\n\n")
            print(
                "elasticite: Mesure de la sensibilité d'une variable économique en réponse à une variation d'une autre variable économique.\n\n")
            print(
                "ratioDeficitPIB: Rapport entre le déficit budgétaire annuel d'un gouvernement et son PIB, souvent exprimé en pourcentage.\n\n")
            print(
                "PIB: Valeur totale de tous les biens et services produits par une économie sur une période donnée.\n\n")
            print(
                "tauxDirecteurPrecedent: Valeur précédente du taux d'intérêt principal fixé par la banque centrale pour guider les autres taux d'intérêt.\n\n")
            print(
                "reponseInflation: Mesure de la manière dont la politique monétaire s'ajuste en réponse aux changements dans le taux d'inflation.\n\n")
            print(
                "DettePublique: Montant total de l'argent emprunté par le gouvernement, à tous les niveaux, qui n'a pas encore été remboursé.\n\n")
            print(
                "tauxDirecteur: Taux d'intérêt principal fixé par la banque centrale pour influencer les conditions de crédit et la monnaie de l'économie.\n\n")
            print(
                "ratioDettePubliquePIB: Rapport entre le montant total de la dette publique d'un pays et son Produit Intérieur Brut, indiquant le niveau d'endettement par rapport à la taille de l'économie.\n\n")
            print(
                "tauxInteretReelPolitiqueMonetaire: Taux d'intérêt défini par la banque centrale, ajusté pour l'inflation, utilisé pour influencer l'économie.\n\n")
            print(
                "valeurEtatStable: Dans un contexte économique, cela peut se référer à une condition d'équilibre où un modèle économique atteint un état stable sans tendance à l'inflation ou à la déflation excessive, souvent utilisé pour décrire un niveau d'endettement ou de déficit soutenable à long terme.\n\n\n\n")


        else:
            print("Choix non valide\n\n\n\n")


# Sinon le code ne compile pas
if __name__ == "__main__":
    main()