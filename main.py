import pygame, sys, time
from settings import *
from sprites import Background, Macaw, Obstacle, Ground
 
class Game:
    def __init__(self):
        
        # setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Macaw Mad!')
        self.clock = pygame.time.Clock()
        self.active = True
        
        #sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        
        #scale factor
        background_height = pygame.image.load('../graphics/environment/layer-1-sky.png').get_height()
        # background_width = pygame.image.load('../graphics/environment/layer-1-sky.png').get_width()
        # print(background_height)
        # print(background_width)
        self.scale_factor = WINDOW_HEIGHT / background_height
    
        #sprite setup
        Background(self.all_sprites,self.scale_factor)
        Ground([self.all_sprites,self.collision_sprites],self.scale_factor*1.5)
        self.macaw = Macaw(self.all_sprites,self.scale_factor*1.75)
        
        #timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer,1000)
        
        # font-style
        self.font = pygame.font.Font('../graphics/font/cartoon-font.ttf', 36)
        self.score = 0
        
        #menu
        self.menu_surf = pygame.image.load('../graphics/ui/menu.png').convert_alpha()
        self.scaled_menu_surf = pygame.transform.scale(self.menu_surf,pygame.math.Vector2(self.menu_surf.get_size())/1.5)
        self.menu_rect = self.scaled_menu_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
        
    def collisions(self):
        if pygame.sprite.spritecollide(self.macaw,self.collision_sprites,False,pygame.sprite.collide_mask)\
        or self.macaw.rect.top <= -10:
            self.active = False
 
    def display_score(self):
        if self.active:
            self.score = pygame.time.get_ticks()//1000
        
        score_surf = self.font.render(str(self.score),True, 'brown')
        score_rect = score_surf.get_rect(midtop = (WINDOW_WIDTH/2, WINDOW_HEIGHT/10))
        self.display_surface.blit(score_surf,score_rect)
 
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.macaw.jump()
                if event.type == self.obstacle_timer:
                    Obstacle([self.all_sprites,self.collision_sprites],self.scale_factor*3)
            
            # game logic
            self.display_surface.fill('black')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)
            self.display_score()
            
            if self.active:
                self.collisions()
            else:
                self.display_surface.blit(self.scaled_menu_surf,self.menu_rect)
            
            pygame.display.update()
            self.clock.tick(FRAMERATE)
 
if __name__ == '__main__':
    game = Game()
    game.run()