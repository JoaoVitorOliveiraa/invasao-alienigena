import pygame

from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    """Classe para representar um único alienígina na frota"""

    def __init__(self, ai_game):
        """Inicializa o alienígina e define sua posição inicial"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load("C:/Users/Pichau/Documents/João/Livro_Curso_Intensivo_de_Python/Capitulos/Capitulo_12/alien_invasion/images/alien3.bmp")
        self.rect = self.image.get_rect()

        # Inicia cada alienígena novo perto do canto superior esquerdo da tela
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height 

        # Armazena a posilção horizontal exata do alienígena
        self.x = float(self.rect.x)

    def update(self):
        """Desloca o alienígena para a direita ou para a esquerda"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Retorna True se o alienígena estiver na borda da tela"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)