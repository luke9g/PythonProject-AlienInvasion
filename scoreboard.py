import pygame.font


class Scoreboard:
    """Klasa przeznaczona do przedstawiania informacji o punktacji."""

    def __init__(self, ai_game):
        """Inicjalizacja atrybutów dotyczących punktacji."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Ustawienia czcionki.
        self.text_color = (60, 60, 60)
        self.font = pygame.font.SysFont(None, 48)

        # Przygotowanie początkowych obrazów z punktacją.
        self.prep_score()

    def prep_score(self):
        """Umieszczenie punktacji we wygenerowanym obrazie w prawym górnym rogu ekranu."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Umieszczenie punktacji w prawym górnym rogu ekranu.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Wyświetlenie punktacji na ekranie."""
        self.screen.blit(self.score_image, self.score_rect)
