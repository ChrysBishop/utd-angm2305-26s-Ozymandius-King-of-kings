import pygame

    ## Week 1: 
    # figure out resolution (600 x 600) some screens may be larger than the resolution, in which we can pan around
    # create elements (images)
       # 
    # mouse work

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




if __name__ == "__main__":
    main()