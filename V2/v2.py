# crée par la Triforce Informatique
from tkinter import*
from random import*
import time
import make_background
import Data_questions
#   fenetre et toile de background sur laquelle sont dessines les cases
width ,height = 1535 , 800

fenetre = Tk()
fenetre.geometry( str(largeur)+"x"+str(hauteur) )
background = Canvas( fenetre , width=largeur , height=hauteur ,bg="white" )
fenetre.wm_state(newstate="normal")
fenetre.title('Jeu du BAC')
background.place( x=0 , y=0 )                                                         #   place le canevas sur la fenetre

#   tous les dessins (rectangles et textes) sur la toile de background (Canvas)

# make background 
case = make_background(background);
#   cases

#   liste de questions par matière

# Fonctions:

def temps():
    heure.set(time.strftime('%H:%M:%S'))                                        # fonction indiquant l'heure
    fenetre.after(1000,temps)

def lancer1():
    ''' lance un de a six faces '''
    global n1
    global couleur1
    if n1 < 118 :
        de1 = randint(1,6)
        n1 = n1 + de1
        labelResultat.config( text= str(de1)+" au lancé de dé" )
        if n1>119 :
            n1 = 119
            poserQuestionFiliere()
        couleur1 = background.itemcget( case[n1] , 'fill' )
        coordonneeCase = background.coords( case[n1] )                                #   coordonnees de la case n
        x1Case = int(coordonneeCase[0])                                         #   abscisse (en haut a gauche) de la case n
        y1Case = int(coordonneeCase[1])                                         #   ordonnee (en haut a gauche) de la case n
        background.coords( joueur1 , x1Case+5 , y1Case+5 , x1Case+25 , y1Case+25 )
        if couleur1=='white' :
            prisonnier()
        else :
            poserQuestion()

def poserQuestion() :
    ''' pose une question   '''
    #   choix aleatoire d'une question
    global numeroCouleur
    global numeroQuestion
    numeroCouleur = couleur.index( couleur1 )                                   #   numero de cette couleur du joueur1
    nbQuestionCetteCouleur = len( question[numeroCouleur])                      #   nombre de questions pour cette couleur
    numeroQuestion = randint( 0 , nbQuestionCetteCouleur-1 )                    #   choix aleatoire d'un numero de question
    #   modification des textes
    etQuestion.config( text = question[numeroCouleur][numeroQuestion][0] )      #   question posée
    bouton1.config( text =  question[numeroCouleur][numeroQuestion][1] )        #   réponse A proposée
    bouton2.config( text =  question[numeroCouleur][numeroQuestion][2] )        #   réponse B proposée
    bouton3.config( text =  question[numeroCouleur][numeroQuestion][3] )        #   réponse C proposée

##  fonction ajoutee
def poserQuestionFiliere() :
    ''' pose une question dans chaque filiere '''
    global numeroCouleur
    global numeroQuestion
    if n1==119 :
        background.coords( joueur1 , 1060 , 570 , 1080 , 590 )                        #   deplacement du pion
        numeroCouleur = couleur.index( "orangered" )                            #   couleur de la case S
    elif n1==120 :
        background.coords( joueur1 , 1060 , 420 , 1080 , 440 )                        #   deplacement du pion
        numeroCouleur = couleur.index( "deepskyblue" )                          #   couleur de la case L
    elif n1==121 :
        background.coords( joueur1 , 1060 , 270 , 1080 , 290 )                        #   deplacement du pion
        numeroCouleur = couleur.index( "chocolate" )                            #   couleur de la case ES
    elif n1==122 :
        background.coords( joueur1 , 1060 , 120 , 1080 , 140 )                        #   deplacement du pion
        heureFin = time.strftime('%H:%M:%S')
        print( "heure de fin de partie :" , heureFin )
        if points>10 :
            texteFinal = "Bravo, vous avez eu votre baccalauréat !"
        else :
            texteFinal = "Dommage vous êtes recalé, vous devez repasser le baccalauréat"
        etQuestion.config( text = texteFinal )                                  #   message de fin
        bouton1.destroy()
        bouton2.destroy()
        bouton3  .destroy()
        btValider.destroy()
        resultatJoueur.destroy()
    if n1<122 :
        nbQuestionCetteCouleur = len( question[numeroCouleur])                  #   nombre de questions pour cette couleur
        numeroQuestion = randint( 0 , nbQuestionCetteCouleur-1 )                #   choix aleatoire d'un numero de question
        etQuestion.config( text = question[numeroCouleur][numeroQuestion][0] )
        bouton1.config( text =  question[numeroCouleur][numeroQuestion][1] )
        bouton2.config( text =  question[numeroCouleur][numeroQuestion][2] )
        bouton3.config( text =  question[numeroCouleur][numeroQuestion][3] )

##  fin de la fonction

def validation():
    ''' valide le choix et permet de continuer a poser des questions    '''
    global nbValidations
    global points
    global n1
    if n1<119 :
        nbValidations = nbValidations+1                                         #   le nombre de clics sur le bouton valider est incremente
        if (nbValidations%2==1) :                                               #   si le nombre de clics est impair
            if (choix.get() == question[numeroCouleur][numeroQuestion][4]) :    #   si le choix correspond a la bonne reponse
                etSelection.config( text="VRAI" )
                points = points + 1                                             #   on gagne un point a chaque bonne reponse
            else :                                                              #   si le choix ne correspond pas a la bonne reponse
                etSelection.config( text="FAUX, la bonne réponse était " + question[numeroCouleur][numeroQuestion][4] )
            resultatJoueur.config(text = 'score : '+ str(points))
            btValider.config( text="Lancer" )
        else :
            lancer1()
            etSelection.config( text="Choisissez une réponse" )
            btValider.config( text="Valider" )
    ##  nouvelle partie de la fonction
    else :                                                                      #   validation avec les dernières cases
        if (choix.get() == question[numeroCouleur][numeroQuestion][4]) :        #   si le choix correspond a la bonne reponse
            etSelection.config( text="VRAI" )
            n1 = n1 + 1                                                         #   on passe a la case suivante
        else :                                                                  #   si le choix ne correspond pas a la bonne reponse
            etSelection.config( text="FAUX, essayez à nouveau" )
            points = points - 1                                                 #   on perd un point a chaque mauvaise reponse
        resultatJoueur.config(text = 'score : '+ str(points))
        poserQuestionFiliere()
    ##  fin de la nouvelle partie

def selection() :
    selection = "Vous avez choisi la réponse " + choix.get()
    etSelection.config( text=selection )                                        #   modifie le texte de l'etiquette
    labelResultat.config( text="" )                                             #   efface le resultat du de


def lancerPrison():                                                             # Lance un dé en prison
    global dePrison
    dePrison = randint(1,6)
    resultatPrison.config( text = str(dePrison) )
    prisonnier()

def prisonnier() :                                                              # fonction Prison
    global n1
    coordonneeCase = background.coords( case[123] )
    x1Case = int(coordonneeCase[0])
    y1Case = int(coordonneeCase[1])
    background.coords( joueur1 , x1Case+5 , y1Case+5 , x1Case+25 , y1Case+25 )
    couleur1 = background.itemcget( case[123] , 'fill' )
    btValider.place_forget()
    boutonPrison.place(x = 680, y = 710)
    resultatPrison.place(x = 700, y = 740)
    if dePrison==6 :
        n1 = n1-1
        coordonneeCase = background.coords( case[n1-1] )
        x1Case = int(coordonneeCase[0])
        y1Case = int(coordonneeCase[1])
        background.coords( joueur1 , x1Case+5 , y1Case+5 , x1Case+25 , y1Case+25 )
        boutonPrison.place_forget()
        btValider.place(x = 1320, y = 300)

if __name__=='__main__' :

    #   joueur1
    x, y = 50, 770
    joueur1 = background.create_oval(x, y, x+20, y+20, fill = 'gold')
    n1 = 0                                                                      #   numero de la case du joueur1
    couleur1 = 'white'

    #   affiche le résultat du dé
    labelResultat = Label(fenetre , text = "" , fg = 'black' , bg = 'white')
    labelResultat.place( x=1400 , y=300 )

    #   score du joueur
    resultatJoueur = Label(fenetre, text = "", fg = 'black', bg = 'white')
    resultatJoueur.place( x = 1205, y = 350)

    heure = StringVar()                                                         #   variable de controle de type chaine de caracteres
    etHeure = Label(fenetre, textvariable=heure)
    etHeure.place( x=950 , y=10 )                                               #   pour faire apparaitre l'heure dans la fenetre
    temps()

    points = 0                                                                  #  nombre de points
    couleur = [ "red", "green", "blue", "purple", "black", "yellow", "orange", "orangered", "deepskyblue", "chocolate", "navy" ]
    question = [ questionRouge, questionVerte, questionBleue, questionViolette, questionNoire, questionJaune, questionOrange, questionS, questionL, questionES, Prison ]
    numeroCouleur = -1                                                          #   initialisation arbitraire
    numeroQuestion = -1                                                         #   initialisation arbitraire

    #   composants de la fenetre
    etQuestion = Label(fenetre, text = "question" )
    etQuestion.place(x = 1205, y = 10)

    choix = StringVar()                                                         #   variable de controle de type chaine de caracteres
    bouton1 = Radiobutton(fenetre, text = "reponse A", variable = choix, value = 'A', command = selection)
    bouton1.place(x = 1290, y = 100)
    bouton2 = Radiobutton(fenetre, text = "reponse B", variable = choix, value = 'B', command = selection)
    bouton2.place(x = 1290, y = 150)
    bouton3 = Radiobutton(fenetre, text = "reponse C", variable = choix, value = 'C', command = selection)
    bouton3.place(x = 1290, y = 200)
    etSelection = Label( fenetre, text="Faites votre choix" )                   #   etiquette indiquant la selection
    etSelection.place(x = 1270, y = 250)

    nbValidations = -1                                                          #   initialisation à -1 car on clique d'abord sur 'commencer' avant de lancer le premier dé
    btValider = Button(fenetre, text = "Commencer", command = validation)
    btValider.place(x = 1320, y = 300)

    boutonPrison = Button(fenetre, text = "Lancer", command = lancerPrison)
    resultatPrison = Label(fenetre, text = "", fg = 'red', bg = 'white')
    dePrison = 0

    heureDebut = time.strftime('%H:%M:%S')
    print( "heure de debut de partie :" , heureDebut )
    fenetre.mainloop()
