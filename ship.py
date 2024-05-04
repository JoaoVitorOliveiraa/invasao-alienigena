import pygame

class Ship:
    """Classe para cuidar da espaçonave"""

    def __init__(self, ai_game):
        """Inicializa a espaçonave e defina sua posição inicial"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Sobe a imagem da espaçonave e obtém seu rect 
        self.image = pygame.image.load("C:/Users/Pichau/Documents/João/Livro_Curso_Intensivo_de_Python/Capitulos/Capitulo_12/alien_invasion/images/ship.bmp")
        self.rect = self.image.get_rect()

        # Começa cada espaçonave nova no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Armeza um float para a posição horizontal exata da espaçonave
        self.x = float(self.rect.x)

        # Armeza um float para a posição vertical exata da espaçonave
        self.y = float(self.rect.y)

        # Flags de movimento; começa com uma espaçonave que não está se movendo
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """Atualiza a posição da espaçonave com base nas flags de movimento"""
        # Atualiza o valor do x da espaçonave, não o rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_x
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_x

        # Atualiza o valor do y da espaçonave, não o rect
        if self.moving_top and self.rect.top > 0:
            self.y -= self.settings.ship_speed_y
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed_y

        # Atualiza o objeto rect de self.x
        self.rect.x = self.x

        # Atualiza o objeto rect de self.y
        self.rect.y = self.y

    def blitme(self):
        """Desenha a espaçonave em sua localização atual"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centraliza a espaçonave na tela"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)