class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja ustawień gry."""
        # Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ustawienia dotyczące statku
        self.ship_limit = 3

        # Ustawienia dotyczące pocisku
        self.bullet_width = 3
        self.bullet_height = 18
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Ustawienia dotyczące obcego
        self.fleet_drop_speed = 5

        # Zmiana szybkości gry po przejściu na nowy poziom
        self.speedup_scale = 1.15

        # Zmiana liczby punktów za zestrzelenie obcego po przejściu na nowy poziom
        self.score_scale = 1.5

        # Ustawienia dynamiczne
        self.initialize_dynamic_settings()

        # Czas pauzy gry po utracie statku przez gracza (w milisekundach)
        self.delay = 500

    def initialize_dynamic_settings(self):
        """Inicjalizacja ustawień, które ulegają zmianie w trakcie gry."""
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 0.5
        # Wartość fleet_direction wynosząca 1 oznacza ruch w prawo, a -1 w lewo.
        self.fleet_direction = 1

        # Liczba punktów za zestrzelenie obcego
        self.alien_points = 50

    def increase_speed(self):
        """Zmiana ustawień dotyczących szybkości gry."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        # Zwiększenie liczby punktów za zestrzelenie obcego po przejsciu na nowy poziom
        self.alien_points = int(self.alien_points * self.score_scale)
