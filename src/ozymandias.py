import pygame


class Animation():

    def __init__(self, id=0):
        self.life = 100
        self.id = id
        self.hasPlayed = False

    def play_animation(self, animNumber, screen):
        animNumber = self.id 
        img = pygame.image.load('test.png')
        match animNumber:
            case 0:
                button = Button()
                button.draw(screen)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if button.is_click_within_area(button.area[0][0], button.area[0][1], 
                                                button.size, pygame.mouse.get_pos()[0], 
                                               pygame.mouse.get_pos()[1]) == True:
                            screen.blit(img, (0,0))
            case 1:
                button = Button((50, 50))
                button.draw(screen)
                if button.is_click_within_area(button.area[0][0], button.area[0][1], 
                                                button.size, pygame.mouse.get_pos()[0], 
                                                pygame.mouse.get_pos()[1]) == True:
                     pygame.QUIT

    def set_played_true(self):
        self.hasPlayed = True


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

    def is_click_within_area(self, areax, areay, size, mousex, mousey):
        if((mousex >= areax and mousex <= areax + size) and
       (mousey >= areay and mousey <= areay + size)):
            return True
        else:
            return False


class Sequence():

    def __init__(self, screen):
        self.scene_list = [Animation(i) for i in range(2)]
        self.screen = screen
        self.sequenceId = 0

    def run_seq(self):
        for i in self.scene_list:
            if i.id == self.sequenceId:
                i.play_animation(i.id, self.screen)
            break

    def update(self):
        self.sequenceId += 1


def main():

    pygame.init()
    pygame.display.set_caption("Ozymandias")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    sequence = Sequence(screen)
    #button = Button((50, 50))
    
    running = True
    
    while running:
        for event in pygame.event.get():
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if button.is_click_within_area(button.area[0][0], button.area[0][1], 
            #                                    button.size, pygame.mouse.get_pos()[0], 
            #                                    pygame.mouse.get_pos()[1]) == True:
            #         pygame.QUIT
            if event.type == pygame.QUIT:
                running = False
        sequence.run_seq()
        #button.draw(screen)
        pygame.display.update()




if __name__ == "__main__":
    main()