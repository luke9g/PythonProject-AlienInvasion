import pygame.font


class Button:
    """Klasa reprezentująca przycisk."""

    def __init__(self, ai_game, msg):
        """Inicjalizacja atrybutów przycisku."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Zdefiniowanie wymiarów i właściwości przycisku.
        self.width, self.height = 200, 50
        self.button_color = (0, 100, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Utworzenie prostokąta przycisku i wyśrodkowanie go.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Przygotowanie komunikatu wyświetlanego przez przycisk
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Umieszczenie komunikatu we wygenerowanym obrazie i wyśrodkowanie tekstu na przycisku."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Wyświetlenie przycisku, a nastepnie jego komunikatu"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
