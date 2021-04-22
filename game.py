import pygame
from player import Player
from projectile import Projectile
from vie import Vie

class Game(pygame.sprite.Sprite) :

    mario_profil_droite = pygame.image.load("characters/mario_profil_droite.png")
    mario_profil_gauche = pygame.image.load("characters/mario_profil_gauche.png")
    mario_run_droite = pygame.image.load("characters/mario_run_droite.png")
    mario_run_gauche = pygame.image.load("characters/mario_run_gauche.png")

    luigi_profil_droite = pygame.image.load("characters/luigi_profil_droite.png")
    luigi_profil_gauche = pygame.image.load("characters/luigi_profil_gauche.png")
    luigi_run_droite = pygame.image.load("characters/luigi_run_droite.png")
    luigi_run_gauche = pygame.image.load("characters/luigi_run_gauche.png")

    def __init__(self) :
        self.pressed = {}
        self.all_projectile = pygame.sprite.Group()
        self.monte_player1 = False
        self.descente_player1 = False
        self.monte_player2 = False
        self.descente_player2 = False

        self.direction_player1 = "droite"
        self.direction_player2 = "gauche"
        self.avant_saut_y1 = 0
        self.avant_saut_y2 = 0

        self.entrain_de_sauter1 = False
        self.entrain_de_sauter2 = False

        self.ouff = pygame.mixer.Sound("sounds/ouff.ogg")
        pygame.mixer.Sound.set_volume(self.ouff, 10)

        #Au niveau afifchage :
        self.vie_mario = Vie(self, "assets/vie_mario.png", "mario", [20, 80, 140])
        self.vie_luigi = Vie(self, "assets/vie_luigi.png", "luigi", [1410, 1470, 1530])

        #Gestion des players :
        self.player1 = Player("characters/mario_profil_droite.png", 20, 606, 80, 80, "mario")
        self.player2 = Player("characters/luigi_profil_gauche.png", 1480, 603, 60, 90, "luigi")

    def ajout_projectile(self, direction, qui) :
        self.all_projectile.add(Projectile(self, direction, qui))

    def check_collision_sprite(self, sprite1, sprite2) : #Fonction qui retrun True si il y a collision entre sprite et sprite
        return pygame.sprite.collide_rect(sprite1, sprite2)