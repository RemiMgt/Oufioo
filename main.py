#!/usr/bin/env python3

#Importation :
import pygame
import pygame, sys
from pygame.locals import *
from game import Game

pygame.init()
pygame.mixer.init()

#Variables :
longueur = 1600
hauteur = 900
boucle = True
statut = "menu"
tableau_animation = [True] * 40 + [False] * 40
index_tableau = 0
gagnant_actuel = "gagnant"

#Images :
mario_gagnant = pygame.image.load("assets/mario_gagnant.png")
mario_gagnant = pygame.transform.scale(mario_gagnant, (550, 550))
mario_gagnant_rect = mario_gagnant.get_rect()
mario_gagnant_rect.x = 0
mario_gagnant_rect.y = 130

luigi_gagnant = pygame.image.load("assets/luigi_gagnant.png")
luigi_gagnant = pygame.transform.scale(luigi_gagnant, (550, 570))
luigi_gagnant_rect = luigi_gagnant.get_rect()
luigi_gagnant_rect.x = 0
luigi_gagnant_rect.y = 130

#Création de la fenêtre : 
pygame.display.set_caption("Oufioo")
fenetre = pygame.display.set_mode((longueur, hauteur))

#Menu :
fond_ecran_menu = pygame.image.load("assets/fond_ecran.jpg")
fond_ecran_menu = pygame.transform.scale(fond_ecran_menu, (longueur, hauteur))
black = (0, 0, 0)
texte_play = pygame.image.load("assets/texte_play.png")

#Jeux :
fond_ecran_jeux = pygame.image.load("assets/fond_ecran_jeux.jpg")
fond_ecran_jeux = pygame.transform.scale(fond_ecran_jeux, (longueur, hauteur))

#Musiques :
musique_menu = pygame.mixer.Sound("sounds/musique_menu.ogg")
musique_jeux = pygame.mixer.Sound("sounds/musique_jeux.ogg")
musique_menu.play(-1)

#Cursor :
cursor = pygame.image.load("assets/projectile.png")
cursor = pygame.transform.scale(cursor, (60, 60))

#Instance de la classe game :
game = Game()

#Boucle du jeux :
while boucle : 
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #print(mouse_x, mouse_y)
    #print(game.avant_saut_y1
    print(statut)

    #Menu :
    if statut == "menu" :
        fenetre.blit(fond_ecran_menu, (0, 0))
        #Cursor :
        fenetre.blit(cursor, (mouse_x - 30, mouse_y - 30))
        if tableau_animation[index_tableau] == True :
            fenetre.blit(texte_play, (1000, 625))
        index_tableau += 1
        if index_tableau == len(tableau_animation) - 1 :
            index_tableau = 0
        #Le gagnant :
        if gagnant_actuel == "mario" :
            fenetre.blit(mario_gagnant, mario_gagnant_rect)
            mario_gagnant_rect.x += 10
        elif gagnant_actuel == "luigi" :
            fenetre.blit(luigi_gagnant, luigi_gagnant_rect)
            luigi_gagnant_rect.x += 10

    #Jeux :
    elif statut == "jeux" :
        fenetre.blit(fond_ecran_jeux, (0, 0))
        fenetre.blit(game.player1.image, game.player1.rect)
        fenetre.blit(game.player2.image, game.player2.rect)
        for projectile in game.all_projectile :
            projectile.move()
        game.all_projectile.draw(fenetre)

        #Déplacement :
        if game.pressed.get(pygame.K_d) == True and game.player1.rect.x <= 1525 :
            game.player1.droite()
            game.direction_player1 = "droite"
            game.player1.show_droite()
            
        if game.pressed.get(pygame.K_q) == True and game.player1.rect.x >= 0:
            game.player1.gauche()
            game.direction_player1 = "gauche"
            game.player1.show_gauche()

        if game.pressed.get(pygame.K_m) == True and game.player2.rect.x <= 1538:
            game.player2.droite()
            game.direction_player2 = "droite"
            game.player2.show_droite()
            
        if game.pressed.get(pygame.K_k) == True and game.player2.rect.x >= 10:
            game.player2.gauche()
            game.direction_player2 = "gauche"
            game.player2.show_gauche()

        #Pour les sauts avant :
        #Joueur 1 :
        if game.entrain_de_sauter1 == False :
            if game.player1.rect.y >= 600 and game.player1.rect.y <= 615 :
                game.avant_saut_y1 = 606
            if game.player1.rect.y >= 320 and game.player1.rect.y <= 463 :
                game.avant_saut_y1 = 380
            if game.player1.rect.y >= 121 and game.player1.rect.y <= 312 :
                game.avant_saut_y1 = 228
        #Joueur 2 :
        if game.entrain_de_sauter2 == False :
            if game.player2.rect.y >= 600 and game.player2.rect.y <= 615 :
                game.avant_saut_y2 = 606
            if game.player2.rect.y >= 320 and game.player2.rect.y <= 463 :
                game.avant_saut_y2 = 380
            if game.player2.rect.y >= 121 and game.player2.rect.y <= 312 :
                game.avant_saut_y2 = 228
            

        #Sauts : 
        #Joueur 1 :
        if game.monte_player1 == True :
            if game.player1.rect.y <= game.avant_saut_y1 - game.player1.hauteur_saut :
                game.monte_player1 = False
                game.descente_player1 = True
            else :
                game.player1.rect.y -= game.player1.speed_saut
                game.entrain_de_sauter1 = True

        if game.descente_player1 == True :
            game.player1.rect.y += game.player1.gravite
            if game.player1.rect.y >= game.avant_saut_y1 :
                game.monte_player1 = False
                game.descente_player1 = False
                game.entrain_de_sauter1 = False
            if game.player1.rect.y >= 380 and (game.player1.rect.x >= 758 and game.player1.rect.x <= 1101) : #Plateforme 1
                game.monte_player1 = False
                game.descente_player1 = False
                game.entrain_de_sauter1 = False
            if game.player1.rect.y >= 227 and (game.player1.rect.x >= 1167 and game.player1.rect.x <= 1510) : #Plateforme 2
                if game.player1.rect.y >= 240 :
                    if game.player1.rect.y >= game.avant_saut_y1 :
                        game.monte_player1 = False
                        game.descente_player1 = False
                        game.entrain_de_sauter1 = False
                    else :
                        game.monte_player1 = False
                        game.descente_player1 = True
                        game.entrain_de_sauter1 = True
                else :
                    game.monte_player1 = False
                    game.descente_player1 = False
                    game.entrain_de_sauter1 = False

        #Joueur 2 :
        if game.monte_player2 == True :
            if game.player2.rect.y <= game.avant_saut_y2 - game.player2.hauteur_saut :
                game.monte_player2 = False
                game.descente_player2 = True
            else :
                game.player2.rect.y -= game.player2.speed_saut
                game.entrain_de_sauter2 = True

        if game.descente_player2 == True :
            game.player2.rect.y += game.player2.gravite
            if game.player2.rect.y >= game.avant_saut_y2 :
                game.monte_player2 = False
                game.descente_player2 = False
                game.entrain_de_sauter2 = False
            if game.player2.rect.y >= 380 and (game.player2.rect.x >= 758 and game.player2.rect.x <= 1101) : #Plateforme 1
                game.monte_player2 = False
                game.descente_player2 = False
                game.entrain_de_sauter2 = False
            if game.player2.rect.y >= 227 and (game.player2.rect.x >= 1167 and game.player2.rect.x <= 1510) : #Plateforme 2
                if game.player2.rect.y >= 240 :
                    if game.player2.rect.y >= game.avant_saut_y2 :
                        game.monte_player2 = False
                        game.descente_player2 = False
                        game.entrain_de_sauter2 = False
                    else :
                        game.monte_player2 = False
                        game.descente_player2 = True
                        game.entrain_de_sauter2 = True
                else :
                    game.monte_player2 = False
                    game.descente_player2 = False
                    game.entrain_de_sauter2 = False

        #Pour les vies :
        #Mario :
        if game.player1.vie == 3 :
            fenetre.blit(game.vie_mario.tableau_vie_restant[0], game.vie_mario.rect1)
            fenetre.blit(game.vie_mario.tableau_vie_restant[1], game.vie_mario.rect2)
            fenetre.blit(game.vie_mario.tableau_vie_restant[2], game.vie_mario.rect3)
        if game.player1.vie == 2 :
            fenetre.blit(game.vie_mario.tableau_vie_restant[0], game.vie_mario.rect1)
            fenetre.blit(game.vie_mario.tableau_vie_restant[1], game.vie_mario.rect2)
        if game.player1.vie == 1 :
            fenetre.blit(game.vie_mario.tableau_vie_restant[0], game.vie_mario.rect1)

        #Luigi :
        if game.player2.vie == 3 :
            fenetre.blit(game.vie_luigi.tableau_vie_restant[0], game.vie_luigi.rect1)
            fenetre.blit(game.vie_luigi.tableau_vie_restant[1], game.vie_luigi.rect2)
            fenetre.blit(game.vie_luigi.tableau_vie_restant[2], game.vie_luigi.rect3)
        if game.player2.vie == 2 :
            fenetre.blit(game.vie_luigi.tableau_vie_restant[1], game.vie_luigi.rect1)
            fenetre.blit(game.vie_luigi.tableau_vie_restant[2], game.vie_luigi.rect2)
        if game.player2.vie == 1 :
            fenetre.blit(game.vie_luigi.tableau_vie_restant[0], game.vie_luigi.rect1)


        #Quand on tombe :
        #Pour mario :
        if game.entrain_de_sauter1 == False and game.monte_player1 == False and game.descente_player1 == False :
            if game.avant_saut_y1 == 380 : #Si sur plateforme 1 :
                if game.player1.rect.x <= 758 or game.player1.rect.x >= 1100 :
                    if game.player1.rect.y <= 606 :
                        game.player1.rect.y += game.player1.speed
            #Si sur plateforme 2 : //problème
            if game.player1.rect.x <= 1167 or game.player1.rect.x >= 1507 :
                if game.player1.rect.y <= 380 :
                    game.player1.rect.y += game.player1.speed
        #Pour luigi :
        if game.entrain_de_sauter2 == False and game.monte_player2 == False and game.descente_player2 == False :
            if game.avant_saut_y2 == 380 : #Si sur plateforme 1 :
                if game.player2.rect.x <= 758 or game.player2.rect.x >= 1100 :
                    if game.player2.rect.y <= 606 :
                        game.player2.rect.y += game.player2.speed
            if game.player2.rect.x <= 1167 or game.player2.rect.x >= 1507 :
                if game.player2.rect.y <= 380 :
                    game.player2.rect.y += game.player2.speed

        if game.player1.vie == 0 :
            gagnant_actuel = "luigi"
            luigi_gagnant_rect.x = 0
            game = Game()
            statut = "menu"
            musique_jeux.stop()
            musique_menu.play(-1)
        if game.player2.vie == 0 :
            gagnant_actuel = "mario"
            mario_gagnant_rect.x = 0
            game = Game()
            statut = "menu"
            musique_jeux.stop()
            musique_menu.play(-1)

    pygame.display.flip()

    #Events :
    for event in pygame.event.get() :
        
        if event.type == pygame.QUIT :
            print("Oufff")
            boucle = False
            pygame.quit()

        if event.type == pygame.KEYDOWN :
            #Déplacements :
            game.pressed[event.key] = True

            if event.key == pygame.K_ESCAPE :
                print("Oufff")
                boucle = False
                pygame.quit()

            #Jeux :
            if statut == "jeux" :
                if event.key == pygame.K_z :
                    if game.entrain_de_sauter1 == False :
                        game.monte_player1 = True

                if event.key == pygame.K_o :
                    if game.entrain_de_sauter2 == False :
                        game.monte_player2 = True

                if event.key == pygame.K_SPACE :
                    game.ajout_projectile(game.direction_player1, "mario")

                if event.key == pygame.K_RETURN :
                    game.ajout_projectile(game.direction_player2, "luigi")

            #Menu :
            if statut == "menu" :
                if event.key == pygame.K_RETURN :
                    statut = "jeux"
                    musique_menu.stop()
                    musique_jeux.play(-1)

        if event.type == pygame.KEYUP :
            game.pressed[event.key] = False