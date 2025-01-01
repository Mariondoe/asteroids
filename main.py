# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

print("Starting asteroids!")
from constants import *
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")
fps = pygame.time.Clock()
dt = 0

updatable_group = pygame.sprite.Group()
drawable_group = pygame.sprite.Group()

from player import Player  # Import the Player class from player.py

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Instantiate Player

    updatable_group.add(player)
    drawable_group.add(player)
    
    #Game Loop
    while True:

        dt = fps.tick(60) / 1000  # This gives us delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        
        #player.update(dt)
        for updatable in updatable_group:
            updatable.update(dt)

        BLACK = (0, 0, 0)
        #screen.fill(BLACK)
        screen.fill("black")
        #player.draw(screen)
        for drawable in drawable_group:
            drawable.draw(screen)

        pygame.display.flip()


        #Limit the game to 60 frames per second
        #clock.tick(60)
        #dt = fps.tick() / 1000









#This line ensures the main() function is only called
#when this file is run directly
if __name__ == "__main__":
    main()