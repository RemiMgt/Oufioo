import pygame

class Vie(pygame.sprite.Sprite):

    def __init__(self, game,  URL_Image, nom_perso, coord_images) :
        super().__init__()
        self.game = game

        self.image1 = pygame.image.load(URL_Image)
        self.image2 = pygame.image.load(URL_Image)
        self.image3 = pygame.image.load(URL_Image)

        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect3 = self.image3.get_rect()

        self.taille_image = 50

        self.image1 = pygame.transform.scale(self.image1, (self.taille_image, self.taille_image))
        self.image2 = pygame.transform.scale(self.image2, (self.taille_image, self.taille_image))
        self.image3 = pygame.transform.scale(self.image3, (self.taille_image, self.taille_image))

        self.rect1.x = coord_images[0]
        self.rect2.x = coord_images[1]
        self.rect3.x = coord_images[2]
        self.rect1.y = 10
        self.rect2.y = 10
        self.rect3.y = 10

        self.tableau_vie_restant = [self.image1, self.image2, self.image3]
        
        self.nom_perso = nom_perso

    def remove(self) :
        if self.nom_perso == "mario" :
            del self.tableau_vie_restant[-1]
        elif self.nom_perso == "luigi" :
            del self.tableau_vie_restant[1]