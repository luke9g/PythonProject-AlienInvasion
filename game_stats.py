class GameStats:
    """Monitorowanie statystyk w grze."""

    def __init__(self, ai_game):
        """Inicjalizacja statystyk."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Flaga aktywności gry
        self.game_active = True

    def reset_stats(self):
        """Inicjalizacja tych statystyk, które mogą zmieniać się w trakcie gry."""
        self.ships_left = self.settings.ship_limit
