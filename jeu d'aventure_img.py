"""
Programme réalisé par Charré Valentin et Nolan Watrin
"""
import pygame
from time import *

#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((640, 360))
pygame.display.set_caption("Jeu d'aventure")
font = pygame.font.Font('FormulaBold.ttf', 20)
font2 = pygame.font.Font('FormulaBold.ttf', 20)

#images
entree = pygame.image.load("entree.jpg")
salleamanger = pygame.image.load("salleamanger.jpg")
cuisine = pygame.image.load("cuisine.jpg")
garage = pygame.image.load("garage.jpg")
jardin = pygame.image.load("jardin.jpg")
cabanon = pygame.image.load("cabanon.jpg")
salon = pygame.image.load("salon.jpg")
caveFerme = pygame.image.load("caveferme.jpg")
caveOuvert = pygame.image.load("caveouvert.jpg")


#map
mapVierge = pygame.image.load("vierge.png")
mapEntree = pygame.image.load("entree.png")
mapSalleamanger = pygame.image.load("salleamanger.png")
mapCuisine = pygame.image.load("cuisine.png")
mapGarage = pygame.image.load("garage.png")
mapJardin = pygame.image.load("jardin.png")
mapCabanon = pygame.image.load("cabanon.png")
mapSalon = pygame.image.load("salon.png")
mapCave = pygame.image.load("cave.png")


#textes
textEntree = font.render("Entrée", True, (0, 0, 0))
textSalleamannger = font.render("Salle à manger", True, (0, 0, 0))
textCuisine = font.render("Cuisine", True, (0, 0, 0))
textGarage = font.render("Garage", True, (0, 0, 0))
textJardin = font.render("Jardin", True, (0, 0, 0))
textCabanon = font.render("Cabanon", True, (0, 0, 0))
textSalon = font.render("Salon", True, (0, 0, 0))
textCaveouvert = font.render("Félécitations, vous avez gagné !", True, (100, 0, 0))
textFindKey = font.render("Vous avez trouvé une clé !", True, (0, 0, 0))
textCaveferme = font.render("Vous vous trouvez dans la cave, voici une énigme", True, (0, 0, 0))
textCaveferme2 = font.render("pour accèder au coffre :", True, (0, 0, 0))
textCaveferme3 = font.render("Je commence la nuit et je finis le matin.", True, (0, 0, 0))


dansQuellePieceEstLePersonnage=1

def decrireLaPiece(piece):
    global haveKey
    if piece == 1:
        fenetre.blit(entree,(0,0))
        fenetre.blit(mapEntree,(530,250))
        fenetre.blit(textEntree,(0,0))
    elif piece == 2:
        fenetre.blit(salleamanger,(0,0))
        fenetre.blit(mapSalleamanger,(530,250))
        fenetre.blit(textSalleamannger,(0,0))
    elif piece == 3:
        fenetre.blit(cuisine,(0,0))
        fenetre.blit(mapCuisine,(530,250))
        fenetre.blit(textCuisine,(0,0))
    elif piece == 4:
        fenetre.blit(caveFerme,(0,0))
        fenetre.blit(mapCave,(530,250))
        fenetre.blit(textCaveferme,(0,0))
        fenetre.blit(textCaveferme2,(0,20))
        fenetre.blit(textCaveferme3,(90,100))
    elif piece == 5:
        fenetre.blit(caveOuvert,(0,0))
        fenetre.blit(mapCave,(530,250))
        fenetre.blit(textCaveouvert,(120,100))
    elif piece == 6:
        fenetre.blit(garage,(0,0))
        fenetre.blit(mapGarage,(530,250))
        fenetre.blit(textGarage,(0,0))
    elif piece == 7:
        fenetre.blit(jardin,(0,0))
        fenetre.blit(mapJardin,(530,250))
        fenetre.blit(textJardin,(0,0))
    elif piece == 8:
        fenetre.blit(cabanon,(0,0))
        fenetre.blit(mapCabanon,(530,250))
        fenetre.blit(textCabanon,(0,0))
    elif piece == 9:
        fenetre.blit(salon,(0,0))
        fenetre.blit(mapSalon,(530,250))
        fenetre.blit(textSalon,(0,0))      


def decision(direction,piece):

    print("Vous désirez allez au",direction)
    memorisePiece=piece

    #Z : le personnage désire aller au nord
    if direction == 'z':
        if piece == 1:
            piece = 6
        elif piece == 6:
            piece = 7
        elif piece == 9:
            piece = 2
        elif piece == 3: 
            piece = 4

    #S : le personnage désire aller au sud
    elif direction == 's':
        if piece == 2:
            piece = 9
        elif piece == 7:
            piece = 6
        elif piece == 6:
            piece = 1
        elif piece == 4:
            piece = 3

    #D : le personnage désire aller à droite
    elif direction == 'd':
        if piece == 8:
            piece = 7
        elif piece == 1:
            piece = 2
        elif piece == 2:
            piece = 3

    #Q : le personnage désire aller à gauche
    elif direction == 'q':
        if piece == 3:
            piece = 2
        elif piece == 2:
            piece = 1
        elif piece == 7:
            piece = 8
    
    #N : le personnage rentre dans la pièce caché
    elif direction == 'n' :
        if piece == 4:
            piece = 5

    if memorisePiece==piece:
        print("Déplacement impossible")
    else:
        print("C'est possible")
    return piece



loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #lecture du clavier
            dansQuellePieceEstLePersonnage=decision(event.unicode,dansQuellePieceEstLePersonnage)
            if event.key == pygame.K_ESCAPE or event.unicode == 'p': #touche p pour quitter
                loop = False
    decrireLaPiece(dansQuellePieceEstLePersonnage)
    # Actualisation de l'affichage
    pygame.display.flip()
pygame.quit()