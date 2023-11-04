import random
from colorama import Fore, Style

nb_min: int = 1
nb_max: int = 10
global score
global joueur_1, joueur_2

""" La Classe Joueur ClJoueur """
class ClJoueur:
    def __init__(self, nom="", sc=0, jx=0, dj=False, ttv=0, miz=0):
        self.nom = nom
        self.score = sc
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


""" 
    Les méthodes ------------------------
""" 
def proposer(ii:int, joueur:str):
    tentatives = 0 
    s = 0
    while True:
        prixPropose = int(input("\tDonnez le juste prix : " ))
        tentatives += 1
        if prixPropose < prix:
            print(Fore.RED + Style.NORMAL + '\tLe just prix est plus haut' + Fore.WHITE)
        if prixPropose > prix:
            print(Fore.BLUE + Style.NORMAL + '\tLe juste prix est plus bas' + Fore.WHITE)
        if prixPropose == prix:
            s = int(score / tentatives)  
            print("\tBravo ! {}, juste prix trouvé {} en {} essais, votre score = {} !".format(joueur, prix, tentatives, s)) 
            
            break
    return s


def jouer(num_jeu: int, j1: ClJoueur, j2:ClJoueur):      
    
    """" Augmenter le nombre de jeux pour chacun des joueurs """
    j1.jeux += 1
    j2.jeux += 1

    """ Qui commence à jouer le 1er """
    quiJoueEn1er = int( random.randint(1, 2))
    print("Qui ?, tiré au sort le : {}".format(quiJoueEn1er)) 
    joueur = j1.nom  if quiJoueEn1er==1 else j2.nom if quiJoueEn1er==2 else "joueur indefinit"
    print ("le joueur qui va commencer cette partie du jeu, c'est le <{}> \n".format(joueur))

    """ Début du jeu """     
    print("<{}> Devinez le juste prix ! \nLe prix est compris entre 1 et 10 inclus.".format(joueur))
    print("-->Jeu n° : {} - Joueur({}) n° : {}".format(num_jeu, joueur, quiJoueEn1er)) 

    """" Réinitialiser la possibilité de jouer pour les 2 joueurs """
    j1.dejaJoue = False
    j2.dejaJoue = False

    for i in [1, 2]:
        print("je suis dans le FoR pour le {}".format(i))
        match quiJoueEn1er:
            case 1:
                #expression_1
                if(j1.dejaJoue == False):
                    print("Joueur i qui joue")
                    sc = proposer(1, joueur) 
                    j1.score += sc
                    j1.dejaJoue = True
                    quiJoueEn1er += 1
            case 2:
                #expression_2
                if(j2.dejaJoue == False):
                    print("Joueur i qui joue")
                    sc = proposer(2, joueur)
                    j2.score += sc
                    j2.dejaJoue = True
                    quiJoueEn1er -= 1
            case _:
                #expression_par_defaut
                print("je suis dans le autre ********************")
                print( "option non valide {}!".format(quiJoueEn1er) )
        # Fin de match
    # Fin de for
            
    return j1, j2



""" 
    Corps du programme (jeu) ---------------------------
""" 
score: int = 1000 

nb_jeux = int(input("Saisir combien de fois se fasse ce jeu ? __ ")) 

""" Un prix au hazard """
prix = random.randint(nb_min, nb_max)

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
    x = jouer( i, joueur_1, joueur_2  )  
    
    i += 1
    # Fin de while

    """ Afficher les jeux avec les score  """
    print("\tscore j1 : {}".format( joueur_1.score ))
    print("\tscore j2 : {}".format( joueur_2.score ))
    print("Et le vaiqueur, c'est le joueur {}".format("joueur 1" if joueur_1.score > joueur_2.score else "joueur 2"))

print("La Partie est terminée !")