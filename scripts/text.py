import pygame

class Text:
    def __init__(self, font, size, text, color, pos):

        self.window = pygame.display.get_surface()

        self.font = pygame.font.Font(font, size)
        self.text = self.font.render(text, True, color)
        self.position = pos

        self.text_rect = self.text.get_rect(center=pos)

    def draw(self):
        self.window.blit(self.text, self.position)


    def draw_center(self):
        self.window.blit(self.text, self.text_rect)