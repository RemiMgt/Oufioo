import pygame

class Projectile(pygame.sprite.Sprite) :

    def __init__(self, game, direction ,qui) :
        super().__init__()
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.game = game
        self.player_actuel = qui
        self.direction = direction
        self.vitesse = 16

        if qui == "mario" :
            self.rect.x = self.game.player1.rect.x + 40
            self.rect.y = self.game.player1.rect.y + 40
        elif qui == "luigi" :
            self.rect.x = self.game.player2.rect.x + 40
            self.rect.y = self.game.player2.rect.y + 40

    def remove(self) :
        self.game.all_projectile.remove(self) #Détruire le projectile courant

    def move(self) :

        if self.player_actuel == "mario" :
            if self.direction == "droite" :
                if not self.game.check_collision_sprite(self, self.game.player2) :
                    if self.rect.x <= 1600 :    
                        self.rect.x = self.rect.x + self.vitesse
                    else :
                        self.remove()
                else :
                    self.game.ouff.play()
                    self.remove()
                    self.game.player2.vie -= 1
                    #Ajouter bruitage vies
            elif self.direction == "gauche" :
                if not self.game.check_collision_sprite(self, self.game.player2) :
                    if self.rect.x >= 0 :
                        self.rect.x = self.rect.x - self.vitesse
                    else :
                        self.remove()
                else :
                    self.game.ouff.play()
                    self.remove()
                    self.game.player2.vie -= 1

        elif self.player_actuel == "luigi" :
            if self.direction == "droite" :
                if not self.game.check_collision_sprite(self, self.game.player1) :
                    if self.rect.x <= 1600 :
                        self.rect.x = self.rect.x + self.vitesse
                    else :
                        self.remove()
                else :
                    self.game.ouff.play()
                    self.remove()
                    self.game.player1.vie -= 1
            if self.direction == "gauche" :
                if not self.game.check_collision_sprite(self, self.game.player1) :
                    if self.rect.x >= 0 :
                        self.rect.x = self.rect.x - self.vitesse
                    else :
                        self.remove()
                else :
                    self.game.ouff.play()
                    self.remove()
                    self.game.player1.vie -= 1
    