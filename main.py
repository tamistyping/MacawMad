import pygame, sys, time
from settings import *
from sprites import Background, Ground, Macaw
 
class Game:
    def __init__(self):
        
        # setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Macaw Mad!')
        self.clock = pygame.time.Clock()
        
        #sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        
        #scale factor
        background_height = pygame.image.load('../graphics/layer-1-sky.png').get_height()
        background_width = pygame.image.load('../graphics/layer-1-sky.png').get_width()
        print(background_height)
        print(background_width)
        self.scale_factor = WINDOW_HEIGHT / background_height
    
        #sprite setup
        Background(self.all_sprites,self.scale_factor)
        Ground(self.all_sprites,self.scale_factor*1.5)
        Macaw(self.all_sprites,self.scale_factor*1.75)
 
    def run(self):
        last_time = time.time()
        while True:
            
            # delta time
            dt = time.time() - last_time
            last_time = time.time()
 
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # game logic
            self.display_surface.fill('black')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)
            
            pygame.display.update()
            self.clock.tick(FRAMERATE)
 
if __name__ == '__main__':
    game = Game()
    game.run()