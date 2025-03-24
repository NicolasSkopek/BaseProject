import pygame

class Text:
    def __init__(self, font, size, text, color, pos):

        self.window = pygame.display.get_surface()

        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(text, True, color)
        self.position = pos

    def draw(self):
        self.window.blit(self.text, self.position)