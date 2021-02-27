import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Klasa przeznaczona do zarządzania pociskami wystrzewaliwanymi przez statek"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.ai_game = ai_game

        # Utworzenie prostokąta pocisku w punkcie (0,0), a następnie zdefiniowanie dla niego
        # określonego położenia.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Położenie pocisku jest zdefiniowane za pomocą wartości zmiennoprzecinkowej.
        self.y = float(self.rect.y)

    def update(self):
        """Poruszanie pociskiem po ekranie."""
        # Uaktualnienie położenia pocisku
        self.y -= self.settings.bullet_speed * self.ai_game.dt
        # Uaktualnienie położenia prostokąta pocisku
        self.rect.y = self.y

    def draw_bullet(self):
        """Wyświetlenie pocisku na ekranie."""
        pygame.draw.rect(self.screen, self.color, self.rect)
