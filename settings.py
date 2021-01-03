class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja ustawień gry."""
        # Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ustawienia dotyczące statku
        self.ship_speed = 1.5

        # Ustawienia dotyczące pocisku
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Ustawienia dotyczące obcego
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # Wartość fleet_direction wynosząca 1 oznacza ruch w prawo, a -1 w lewo.
        self.fleet_direction = 1
