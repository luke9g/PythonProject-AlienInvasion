import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """Klasa przeznaczona do przedstawiania informacji o punktacji."""

    def __init__(self, ai_game):
        """Inicjalizacja atrybutów dotyczących punktacji."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats

        # Ustawienia czcionki.
        self.text_color = (60, 60, 60)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_images()

    def prep_images(self):
        """Przygotowanie obrazów z punktacją, poziomem gry i liczbą pozostałych statków."""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Umieszczenie aktualnego wyniku gracza w prawym górnym rogu ekranu."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10

    def prep_high_score(self):
        """Umieszczenie najlepszego wyniku gry na środku ekranu, przy górnej krawędzi."""
        rounded_high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Umieszczenie aktualnego poziomu gry w prawym górnym rogu ekranu, pod punktacją."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 5

    def prep_ships(self):
        """Umieszczenie pozostałej liczby statków gracza w lewym górnym rogu ekranu."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 5
            self.ships.add(ship)

    def check_high_score(self):
        """Sprawdzenie, czy mamy nowy najlepszy wynik osiągnięty dotąd w grze."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Wyświetlenie punktacji na ekranie."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
