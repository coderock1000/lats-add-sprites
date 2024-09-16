import pygame 
import random

pygame.init()

sprite_color_change_event = pygame.USEREVENT + 1
background_color_change_event = pygame.USEREVENT + 2

blue = pygame.Color("blue")
yellow = pygame.Color("yellow")
red = pygame.Color("red")

orange = pygame.Color("orange")
white = pygame.Color("white")
black = pygame.Color("black")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = (random.choice([-1,1]), random.choice([-1,1]))
    def update(self):
        self.rect.move_ip(self.velocity)
        boundry_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundry_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundry_hit = True
        if boundry_hit:
            pygame.event.post(pygame.event.Event(sprite_color_change_event))
            pygame.event.post(pygame.event.Event(background_color_change_event))

    def change_color(self):
        self.iage.fill(random.choice([orange, white, black]))

def change_background_color():
    global bg_color 
    bg_color = random.choice([blue, yellow, red])

all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(white, 20, 30)
sp1.rect.x = random.randint(0,400)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)
screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("boundry sprite")
bg_color = blue 
screen.fill(bg_color)
exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == sprite_color_change_event:
            sp1.change_color()
        elif event.type == background_color_change_event:
            change_background_color()
    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()
