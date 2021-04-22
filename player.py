import pygame

class Player(pygame.sprite.Sprite) :

    def __init__(self, URLimage, rectx, recty, recadrer_x, recadrer_y, perso) :
        super().__init__()
        self.image = pygame.image.load(URLimage)
        self.image = pygame.transform.scale(self.image, (recadrer_x, recadrer_y))
        self.rect = self.image.get_rect()
        self.rect.x = rectx
        self.rect.y = recty
        self.vie = 3
        self.speed = 12
        self.speed_saut = 16
        self.gravite = 8
        self.recadrer_x = recadrer_x
        self.recadrer_y = recadrer_y
        self.URLimage = URLimage
        self.perso = perso
        self.hauteur_saut = 250
        self.luigi_run_droite = pygame.image.load("characters/luigi_run_droite.png")
        self.luigi_run_gauche = pygame.image.load("characters/luigi_run_gauche.png")
        

        #Gestion du saut :
        self.saut = 0
        self.saut_monte = 0
        self.saut_descendre = 5
        self.nombre_de_sauts = 0
        self.a_sauter = False

    def droite(self) :
        self.rect.x += self.speed

    def gauche(self) :
        self.rect.x -= self.speed


    def show_droite(self) :
        if self.URLimage == "characters/mario_profil_droite.png" :
            self.image = pygame.image.load("characters/mario_profil_droite.png")
            self.image = pygame.transform.scale(self.image, (self.recadrer_x, self.recadrer_y))
        else :
            self.image = pygame.image.load("characters/luigi_profil_droite.png")
            self.image = pygame.transform.scale(self.image, (self.recadrer_x, self.recadrer_y))

    def show_gauche(self) :
        if self.URLimage == "characters/luigi_profil_gauche.png" :
            self.image = pygame.image.load("characters/luigi_profil_gauche.png")
            self.image = pygame.transform.scale(self.image, (self.recadrer_x, self.recadrer_y))
        else :
            self.image = pygame.image.load("characters/mario_profil_gauche.png")
            self.image = pygame.transform.scale(self.image, (self.recadrer_x, self.recadrer_y))
