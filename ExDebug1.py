def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température en °C (int ou float)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : taux d’humidité en % (int ou float)

    Retour :
    - "Tout est sous contrôle!" si toutes les conditions sont respectées
    - "Environnement non optimal" sinon (après avoir affiché les problèmes détectés)
    """

    alerte = False
    for i in range(len(temp)):
        # Vérification température
        if temp[i] < 18:
            print("Température trop basse")
            alerte = True
        elif temp[i] > 27:
            print("Température trop élevée")
            alerte = True

        # Vérification humidité
        if humidite[i] <= 30:
            print("Humidité trop basse")
            alerte = True
        elif humidite[i] >= 50:
            print("Humidité trop élevée")
            alerte = True

        # Vérification poussière
        if poussiere[i] == "fort":
            print("Trop de poussière")
            alerte = True
        elif poussiere[i] == "faible":
            alerte = False
        else:
            print("Niveau de poussiere mal rentree")

        # Retour final
        if not alerte:
            print(f"Tout est sous contrôle pour l'otrdinateur {i}!")
        else:
            print("Environnement non optimal")




if __name__ == "__main__":
    nbrdordi = int(input("Combien d'ordinateurs?"))
    liste_temp = []
    liste_pou = []
    liste_humi = []
    for i in range(nbrdordi):
        temp = float(input(f"Entrez la temperature de l'ordinateur {i+1} : "))
        poussiere = input(f"entrez le niveau de poussiere de l'ordinateur {i+1} : ")
        humidite = float(input(f"Entrez l'humidité' de l'ordinateur {i+1} : "))
        liste_temp.append(temp)
        liste_pou.append(poussiere)
        liste_humi.append(humidite)
environnement_optimal(liste_temp , liste_pou, liste_humi)