import pygame


class Animation():

    def __init__(self, life):
        self.life = life


class Button():

    def __init__(self, pos=(0,0), size=25):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(0, 255, 255)
        self.alpha = 255
        self.dead = False
        self.surface = self.update_surface()
        self.area = (self.pos, (self.pos[0] + self.size, 
                                self.pos[1] + self.size)) # min x, min y, max x, max y

    def update_surface(self):
        surf = pygame.Surface((self.size*0.8, self.size*0.8))
        surf.fill(self.color)
        return surf

    def draw(self, surface):
        if self.dead:
            return
        self.surface.set_alpha(self.alpha)        
        surface.blit(self.surface, self.pos)


def main():

    pygame.init()
    pygame.display.set_caption("Ozymandias")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        button = Button()
        button.draw(screen)
        pygame.display.update()




if __name__ == "__main__":
    main()