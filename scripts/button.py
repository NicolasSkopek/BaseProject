import pygame

from scripts.text import Text


class Button:

    def __init__(self, color, x, y, rect_width, rect_height):
        self.window = pygame.display.get_surface()
        self.color = color
        self.rect = pygame.Rect(x, y, rect_width, rect_height)


    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

class ButtonWithText(Button):
    def __init__(self, color, x, y, rect_width, rect_height, font, size, text, text_color, text_position):
        super().__init__(color, x, y, rect_width, rect_height)

        self.text = text
        self.text_color = text_color
        self.text_position = text_position

        self.render = Text(font, size, self.text, self.text_color, self.text_position)

    def draw(self):
        super().draw()
        self.render.draw()