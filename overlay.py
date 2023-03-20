import pygame


class Overlay:
    def __init__(self, player):
        self.player = player
        self.display_surf = pygame.display.get_surface()
        self.health_surf = pygame.image.load("graphics/health.png").convert_alpha()

    def display(self):
        for h in range(self.player.health):
            x = 10 + h * (self.health_surf.get_width() + 4)
            y = 10
            self.display_surf.blit(self.health_surf, (x, y))
