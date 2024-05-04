class Settings:
    """Classe para armazenar as configurações do Jogo Invasão Alienígena"""

    def __init__(self):
        """Inicializa as configurações do jogo"""
        # Configurações de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50,153,230) 

        # Configurações da espaçonave
        self.ship_speed_x = 3.5
        self.ship_speed_y = 3.5
        self.ship_limit = 3

        # Configurações do projétil
        self.bullet_speed = 4.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3    

        # Configurações do alienígena
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction de 1 representa a direita; -1 representa a esquerda
        self.fleet_direction = 1