import random

def rejouer(q: str):  #Fonction qui permet de rejouer.
    yes = ["oui", "yes", "o", "y"]
    no = ["non", "no", "n"]
    while True:
        r = input(q)
        if r.lower() in yes:
            return True
        elif r.lower() in no:
            return False
        print("La réponse n'est pas valide, entrez oui on non.", end="\n\n")

def tirage_mot():   #Fonction qui tire le mot dans le fichier -> liste.txt
    fichier = open("liste.txt", "r")
    mt = list()
    for m in fichier.readlines():
        mt.append(m.replace("\n", ""))
    mot = random.choice(mt)
    fichier.close()
    return mot

def afficher(mot): #Fonction qui permet d'espace les underscores ou les lettres.
    return " ".join(mot)

def find(mot, caractere):   #Fonction qui permet de trouver la postion precise d'un caractere dans un mot.
    return [index for index, lettre in enumerate(mot) if lettre == caractere]

def pendu():    #Fonction qui principal
    mot_global = tirage_mot() #Variable qui contient le mot à trouver.
    #print(mot_global)
    affichage = ["_" for i in mot_global]  # On met des _ à la place des lettres.
    for index in find(mot_global, mot_global[0]):
        #On remplace plusieurs lettres si la première lettre apparait plusieurs fois.
        affichage[index] = mot_global[0]
        
    tentative = 8   #Variable qui contient le nombre de tentative ici -> 8
    lettres_jouées = "" #Variable qui va contenir les lettres jouées.

    print("########################################")
    print("############ Le jeu du pendu ###########")   #Affichage avec print pour égailler.
    print("######################################## \n")

    while tentative >= 0: #Boucle principal qui permet le déroulement du jeu.

        if "_" not in affichage: #Condition qui arrete la boucle si il n'y a plus le caratere "_" dans la liste afficher. 
            print("Bravo vous avez trouvé le mot :", mot_global, end="\n\n")
            break

        elif tentative == 0: #Condition qui arrete la boucle quand il reste 0 tentative.
            print("Vous avez perdu, le mot était :", mot_global, end="\n\n")
            break

        else: 
            print("Nombre de tentatives :", tentative, end="\n\n")      #Affichage avec print pour informer le joueur, du nbr de tentatives restantes,
            print("Mot à deviner : ", afficher(affichage), end="\n\n")  #du mot à deviner,
            print("Lettres jouées :", lettres_jouées, end="\n\n")       #des lettres jouées.

            proposition = input("Proposez une lettre : ").lower() #Variable local, elle permet de prendre la lettre que le joeur veux jouer.

            if len(proposition) > 1 :                       #Conditions qui vérifies si le joueur met bien un caractes de type lettre et si il en met bien un seul.
                print ("Erreur! Un charactères est permis!")#
                
            elif proposition not in ["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n"] :
                print ("Erreur! Ce-ci n'etait pas un charactère !")

            else :     
                print(" ")

                for index in find(mot_global, proposition):  #On cherche le/les emplacements de la lettre proposer et on remplace les underscores par cette lettre.
                    affichage[index] = proposition

                if proposition not in affichage and proposition not in lettres_jouées: #Conditon qui vérifie que la proposition n'est pas dans affichage et lettres jouées.
                    tentative -= 1                                                     #Enleve un tentative si la condition est vérifiée.
                    if tentative > 2:                                                  
                        lettres_jouées = lettres_jouées + proposition.upper()   #Ajoute la lettre à la liste des lettres jouées.
                        print("Try again !", end="\n\n")

                    else:
                        lettres_jouées = lettres_jouées + proposition.upper()    #Change le print quand il reste qu'une seule et unique chance.
                        print("Derniere chance !", end="\n\n")

pendu()
while rejouer("Voulez-vous rejouer ?"):
    pendu()
