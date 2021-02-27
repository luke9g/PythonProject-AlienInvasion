import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Klasa przeznaczona do zarządzania statkiem kosmicznym."""

    def __init__(self, ai_game):
        """Inicjalizacja statku kosmicznego i jego położenia początkowego."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.ai_game = ai_game

        # Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Każdy nowy statek kosmiczny pojawia się na dole ekranu.
        self.rect.midbottom = self.screen_rect.midbottom

        # Położenie poziome statku jest przechowywane w postaci liczby zmiennoprzecinkowej.
        self.x = float(self.rect.x)

        # Atrybuty wskazujące na poruszanie się statku.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Uaktualnienie położenia statku na podstawie atrybutu wskazującego na jego ruch."""
        # Uaktualnienie wartości współrzędnej X statku, a nie jego prostokąta.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed * self.ai_game.dt
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed * self.ai_game.dt

        # Uaktualnienie obiektu rect na podstawie wartości self.x.
        # Współrzędne obiektu rect są przechowywane w postaci liczby bez części dziesiętnej.
        self.rect.x = self.x

    def center_ship(self):
        """Umieszczenie statku na środku przy dolnej krawędzi ekranu."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Wyświetlenie statku kosmicznego w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)
