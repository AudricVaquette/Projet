#Audric Vaquette Mezyan Hammam
#Jeu du Mastermind

#Importation bibliothèque
import random

#Définition des fonctions
def code_secret():
    """permet de générer le code secret que le
    joueur doit trouver"""
    L=[]
    S=['rg','bu','j','rs','n','bc','v']#rg=rouge bu=bleu j=jaune rs=rose n=noir bc=blanc v=vert
    for i in range(4):
        a=random.choice(S)
        L.append(a)
        y=S.index(a)
        S.pop(y)
    return L

def code_joueur ():
    """Créer le code du joueur en ajoutant les couleurs à la liste C """
    C=[]
    for i in range (4):
        n=str(input('Entrez une couleur du code'))
        C.append(n)
    return C

def reponse(code_secret,code_joueur):
    """vérifie la réponse du joueur
    parmètre : code_secret :table
               code_joueur :table"""
    bp=0
    mp=0
    f=0
    for i in range (4):
        if code_joueur[i]==code_secret[0]:
            if i==0:
                bp=bp+1
            else:
                mp=mp+1
        elif code_joueur[i]==code_secret[1]:
            if i==1:
                bp=bp+1
            else:
                mp=mp+1
        elif code_joueur[i]==code_secret[2]:
            if i==2:
                bp=bp+1
            else:
                mp=mp+1
        elif code_joueur[i]==code_secret[3]:
            if i==3:
                bp=bp+1
            else:
                mp=mp+1 
        else:
            f=f+1
    if code_joueur==code_secret:
        print('vous avez gagné')
    else:
        print(bp,'est/sont bien placée(s),',mp,'est/sont bon mais mal placée(s),',f,'est/sont faux')
#programme principale
code_s=code_secret()
x=0
a=[]
while a!=code_s and x<=10: 
    x=x+1
    a=code_joueur()
    reponse(code_s,a)
