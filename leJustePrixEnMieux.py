#!/usr/bin/python3


import random
import os
import sys
from colorama import Fore, Style

global score, prix, joueur_1, joueur_2
nb_min: int = 1
nb_max: int = 10
score: int = 500 

""" La Classe Joueur ClJoueur """
class ClJoueur:
    def __init__(self, nom="", sc=0, totalscores=0, jx=0, dj=False, ttv=0, miz=0):
        self.nom = nom
        #self.score = sc
        self.scores = []  # liste pour l'historique des scores.
        self.totalDesScores = totalscores
        self.jeux = jx
        self.dejaJoue: bool = False
        self.tentatives: int = ttv
        self.porteMonnaie: int = miz
    
    def chargerPorteMonnaie(self, montant: int):        
        self.porteMonnaie = montant
        return self.porteMonnaie

    def viderPorteMonnaie(self):
        self.porteMonnaie = 0

    def verifierPorteMonnaie(self):
        return self.porteMonnaie

    def ajouterScore(self, score):
        # Ajoutez le score actuel à la liste d'historique des scores.
        self.scores.append(score)
        self.sommeDesScores(score)
    
    def sommeDesScores(self, score):
        self.totalDesScores += score
    

""" 
    Les méthodes ------------------------
""" 

def afficherHistoriqueScores(j1:ClJoueur, j2:ClJoueur):
    # Longueur des listes des scores
    l1 = len(j1.scores)
    l2 = len(j2.scores)

    # Affichez l'historique des scores sous forme de tableau sur la console.
    print("Historique des scores de {} et {}".format(j1.nom, j2.nom))
    print(" +--------------------------------------------+")
    print(" |   Jeu   | Score {}       | Score {}          |".format(j1.nom, j2.nom))
    print(" +--------------------------------------------+")
    
    for jeu, (sc1, sc2) in enumerate(zip(j1.scores, j2.scores)):
        print(f" |   {jeu:2d}    |   {sc1:5d}       |   {sc2:5d}          |")
    print(" +--------------------------------------------+")
    print(" |   Total |    {}        |    {}           |".format(j1.totalDesScores, j2.totalDesScores))
    print(" +--------------------------------------------+")



def ditesUnPrix(ii:int, joueur:str, prix: int):
    tentatives = 0 
    s = 0

    while True:
        prixPropose = int(input((Fore.YELLOW if ii==1 else Fore.GREEN) + Style.NORMAL + "\n\t{} : donnez le juste prix : ".format(joueur)  + Fore.WHITE))
        tentatives += 1
        if (prixPropose < prix):
            print(Fore.RED + Style.NORMAL + '\tLe just prix est plus haut' + Fore.WHITE)
        if (prixPropose > prix):
            print(Fore.BLUE + Style.NORMAL + '\tLe juste prix est plus bas' + Fore.WHITE)
        if (prixPropose == prix):
            s = int(score / tentatives)  
            print("\tBravo ! {}, juste prix trouvé {} en {} essais, votre score = {} !".format(joueur, prix, tentatives, s)) 
            
            break
    return s


def jouer(num_jeu: int, j1: ClJoueur, j2:ClJoueur, prix: int):      
    
    """" Augmenter le nombre de jeux pour chacun des joueurs """
    j1.jeux += 1
    j2.jeux += 1

    """ Qui commence à jouer le 1er """
    quiJoueEn1er = int( random.randint(1, 2))
    print("Qui commence ?, tiré au sort le n° : {}".format(quiJoueEn1er)) 
    joueur = j1.nom  if quiJoueEn1er==1 else j2.nom if quiJoueEn1er==2 else "joueur indefinit"
    print("foct jouer(), joueur : {}".format(joueur))
    """ Début du jeu """     
    print("Le prix est compris entre 1 et 10 inclus.".format(joueur))
    print("-->Jeu n° : {} - Joueur({}) n° : {}".format(num_jeu, joueur, quiJoueEn1er)) 

    """" Réinitialiser la possibilité de jouer pour les 2 joueurs """
    j1.dejaJoue = False
    j2.dejaJoue = False

    for i in [1, 2]:        
        joueur = j1.nom  if quiJoueEn1er==1 else j2.nom if quiJoueEn1er==2 else "joueur indefinit"
        match quiJoueEn1er:
            case 1:
                #expression_1
                if(j1.dejaJoue == False):
                    
                    sc = ditesUnPrix(i, joueur, prix) 
                    #j1.score += sc
                    j1.ajouterScore(sc)
                    j1.dejaJoue = True
                    quiJoueEn1er += 1
            case 2:
                #expression_2
                if(j2.dejaJoue == False):                    
                    sc = ditesUnPrix(i, joueur, prix)
                    #j2.score += sc
                    j2.ajouterScore(sc)
                    j2.dejaJoue = True
                    quiJoueEn1er -= 1
            case _:
                #expression_par_defaut
                print( "option non valide {}!".format(quiJoueEn1er) )
        # Fin de match
    # Fin de for
            
    return j1, j2

def errorManaging():
    if len(sys.argv) == 1:   # aucun argument n'a été passé au programme en dehors de son propre nom.
        return (0)

    if (sys.argv[1] == "-h") and (len(sys.argv) == 2):
        print("\nUSAGE\n\t./leJustePrixEnMieux")
        print("\t./leJustePrixEnMieux [-h]\n")
        print("DESCRIPTION")
        print("\tProgramme de simulation du jeux (le Juste Prix) amélioré !")
        return (1)
     
    if len(sys.argv) >= 2:
        print("ERREUR\n\tTrop d'arguments ou argument non valide à la ligne de commande. \n\tVoir usage (option -h).\n")
        return (1)
   


def main():

    """ 
        Corps du programme (jeu) ---------------------------
    """ 

    """" Gestion des erreurs """
    codeErreur = errorManaging()
    if (codeErreur != 0):
        exit(1)
    
    

    nb_jeux = int(input("Saisir combien de fois se fasse ce jeu ? __ ")) 

    """ Un prix au hazard """
    prix: int = random.randint(nb_min, nb_max)

    """ Construction (Inscription) des joueurs """
    """" Un joueur est défini par : """
    """" 
        - Un nom,                                                 : nom
        - Un score qu'il a réalisé,                               : score
        - Un nombre de jeux qu'il a joués,                        : nb_jeux
        - Un flag s'il a joué son tour ou pas encore,             : dejaJoue
        - combien de tentatives avant de trouver le juste prix,   : tentatives
        - Combien il a misé d'argent au départ                    : porteMonnaie
    """
    joueur_1 = ClJoueur(str(input("Votre prénom (j1) : ")), 0, 0, False, 0, 0)
    joueur_2 = ClJoueur(str(input("Votre prénom (j2) : ")), 0, 0, False, 0, 0)

    i = 1
    while i <= nb_jeux:
        # lancer le jeux nb_jeux fois
        x = jouer( i, joueur_1, joueur_2, prix )

        i += 1
        # Fin de while

    """" Affichage du tableau des scores """
    print("\nScore global des jeux : ") 
    afficherHistoriqueScores(joueur_1, joueur_2)
    print("Et le vaiqueur, c'est {}".format(joueur_1.nom if joueur_1.totalDesScores > joueur_2.totalDesScores else joueur_2.nom))

    print("La Partie est terminée !")


""" 
    Entrée du programme : méthode main
"""
if __name__ == '__main__':
    # Clearing the Screen
    os.system('cls')
    main()