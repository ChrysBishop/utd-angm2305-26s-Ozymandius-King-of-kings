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
        self.isClicked = False

    def update(self):
        if(self.isClicked == True):
            self.size = 0

        pass

    def update_surface(self):
        surf = pygame.Surface((self.size*0.8, self.size*0.8))
        surf.fill(self.color)
        return surf

    def draw(self, surface):
        if self.dead:
            return
        self.surface.set_alpha(self.alpha)        
        surface.blit(self.surface, self.pos)


class Sequence():

    def __init__(self):
        self.seqNum = 0

def is_within_area(areax, areay, size, mousex, mousey):
    if((mousex >= areax and mousex <= areax + size) and
       (mousey >= areay and mousey <= areay + size)):
        return True
    else:
        return False

def main():

    pygame.init()
    pygame.display.set_caption("Ozymandias")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    img = pygame.image.load('test.png')
    button = Button()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_within_area(button.area[0][0], button.area[0][1], 
                                  button.size, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) == True:
                    button.isClicked = True
                    screen.blit(img,(0,0))

            if event.type == pygame.QUIT:
                running = False
            if button.isClicked == True:
                button.isClicked = False

        button.draw(screen)
        pygame.display.update()




if __name__ == "__main__":
    main()