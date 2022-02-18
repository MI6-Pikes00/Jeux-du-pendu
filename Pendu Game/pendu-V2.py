from tkinter import *
import random

###########################################################
################### Code du pendu #########################
###########################################################

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

def jeux(): #Fonction principale du programme elle regroupe tout les elements qui permettent que le jeux fonctionne.

########## Définition de tous les variables qui contitue le programme ##########

    global tentative, lettres_jouées, affichage

    mot_global = tirage_mot() 

    affichage = ["_" for i in mot_global]  
    for index in find(mot_global, mot_global[0]):
        affichage[index] = mot_global[0]

    tentative = 8  

    lettres_jouées = []

#################### Fonction qui contitue le jeux ####################

    def replay(): #Fonction qui permet de rejouer.
        Mafenetre.destroy()
        jeux()

    def clearEntry(): #Fonction qui permet de supprimer les caractères dans l'entry apres validation.
        EntryProposition.delete(0,'end')

    def updateAffichage(): #Fonction qui permet de update l'affichage. 
        tentative_affichage.set(tentative)
        affichage_PlayLetter.set("Lettres jouées : " + afficher(lettres_jouées))
        nomFichier = "bonhomme"+str(tentative)+".gif"
        photo=PhotoImage(file=nomFichier)
        image_pendu.config(image=photo)
        image_pendu.image=photo

    def destruction(): #Fonction qui permet de supprimer des elements que l'on a plus besoin apres la victoire ou la defaite.
        BoutonGo.destroy()
        labelPlayLetter.destroy()
        labelProposition.destroy()
        labelTentative.destroy()
        EntryProposition.destroy()
        labelTen.destroy()

    def replay_btn(): #Fonction qui permet de créer le bouton rejouer.
        replay_btn=Button(Mafenetre,text="Replay",command=replay, border=0)
        replay_btn.grid(row=5,column=9, ipadx=20, ipady=10)

    def wining(): #Fonction qui permet de verifier si le joueur a gagner.
        if "_" not in affichage:
            photo=PhotoImage(file="winner.png")
            image_pendu.config(image=photo)
            image_pendu.image=photo
            destruction()
            replay_btn()

    def losing(): #Fonction qui permet de verifier si le joueur a perdu.
        if tentative <= 0:
            mot_affichage.set(mot_global)
            photo=PhotoImage(file="loser.png")
            image_pendu.config(image=photo)
            image_pendu.image=photo
            destruction()
            replay_btn()
        
#################### Fonction principale du jeux ####################

    def pendu(event=None): 
        global tentative, lettres_jouées, affichage
        print(EntryProposition.get())

        if len(EntryProposition.get()) > 1 :
            labelErreur = Label(Mafenetre,text="Pas plus d'une lettre !", font='Arial 15', fg='black', bg='white')
            labelErreur.grid(row=4, column=5)        
            print ("Erreur! Un charactères est permis!") 
            labelErreur.after(1500, labelErreur.destroy)
            clearEntry()
                
        elif EntryProposition.get() not in ["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n"] :
            labelErreur = Label(Mafenetre,text="Ce ci n'etait pas une lettre !", font='Arial 15', fg='black', bg='white')
            labelErreur.grid(row=4, column=5)
            print ("Erreur! Ceci n'etait pas un charactère !")
            labelErreur.after(1500, labelErreur.destroy)
            clearEntry()

        else:
            if EntryProposition.get() in mot_global:    
                for index in find(mot_global, EntryProposition.get()):  
                    affichage[index] = EntryProposition.get()
                    mot_affichage.set(affichage)
                wining()
            elif EntryProposition.get() not in mot_global and EntryProposition.get().upper() not in lettres_jouées: 
                tentative -= 1                                                     
                lettres_jouées.append(EntryProposition.get().upper())
                losing()
                updateAffichage()
        clearEntry()
        print("tentative : " + str(tentative))
        
    print(mot_global)

    ###########################################################
    ################### Fenetre Tkinter #######################
    ###########################################################

    Mafenetre = Tk()
    Mafenetre.title('Le jeu du Pendu')

    ############################# Affichage #############################

    tentative_affichage=StringVar()
    tentative_affichage.set(tentative)

    labelTen = Label(Mafenetre,text='Tentative :', bg='orange', fg='black', font='Arial 25')
    labelTen.grid(row=3, column=2)
    
    labelTentative = Label(Mafenetre,textvariable=tentative_affichage, font='Arial 25', bg='orange', fg='black')
    labelTentative.grid(row=3, column=3)

    mot_affichage=StringVar()
    mot_affichage.set(affichage)
    labelMot = Label(Mafenetre,textvariable=mot_affichage, font='Arial 25', bg='orange', fg='black')
    labelMot.grid(row=1, column=5, pady=25)

    affichage_PlayLetter=StringVar()
    affichage_PlayLetter.set("Lettres jouées : ")
    labelPlayLetter  = Label(Mafenetre,textvariable=affichage_PlayLetter, font='Arial 25', bg='orange', fg='black')
    labelPlayLetter.grid(row=4, column=2)

    photo=PhotoImage(file="bonhomme8.gif")
    image_pendu = Label(Mafenetre, image=photo, border=0, bg='orange', fg='black')
    image_pendu.grid(row=3, column=5)

    ############################# L'entry #############################

    labelProposition = Label(Mafenetre,text='Proposition :', bg='orange', fg='black')
    labelProposition.grid(row=5, column=4)

    EntryProposition = Entry(Mafenetre, fg='white', border=0) 
    EntryProposition.grid(row=5, column=5)  
    EntryProposition.bind("<Return>", pendu)

    ############################# Button #############################

    # Création d'un widget Button (Le bouton Quitter, ferme la fenetre)
    BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy, border=0)
    BoutonQuitter.grid(row=5, column=10, ipadx=20, ipady=10, padx=10, pady=10)

    # Création d'un widget Button (Le bouton Go, lance le programme une fois un entry entrée)
    BoutonGo = Button(Mafenetre,text='Go',command = pendu, border=0)
    BoutonGo.grid(row=5, column=9, ipadx=20, ipady=10, padx=10, pady=10)

    Mafenetre.columnconfigure(5, weight=10)
    Mafenetre.rowconfigure(3, weight=5)
    Mafenetre.config(bg='orange')
    
    Mafenetre.geometry('1000x750')
    Mafenetre.mainloop()

jeux()
