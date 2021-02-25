class GameStats:
    """Monitorowanie statystyk w grze."""

    def __init__(self, ai_game):
        """Inicjalizacja statystyk."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Flaga aktywności gry
        self.game_active = False

        # Najlepszy wynik osiągnięty w grze
        self.high_score = self._load_score(ai_game.high_score_filename)

    @staticmethod
    def _load_score(filename):
        """Zwraca wynik zapisany w pliku."""
        try:
            with open(filename) as file:
                return int(file.read())
        except FileNotFoundError:
            return 0
        except ValueError:
            return 0

    def reset_stats(self):
        """Inicjalizacja tych statystyk, które mogą zmieniać się w trakcie gry."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
