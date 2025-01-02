# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

print("Starting asteroids!")
from constants import *
from player import Player  # Import the Player class from player.py
from asteroid import Asteroid  # Import the Asteroid class from asteroid.py
from asteroidfield import AsteroidField  # Import the AsteroidField class from asteroidfield.py
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")
fps = pygame.time.Clock()
dt = 0

updatable_group = pygame.sprite.Group()
drawable_group = pygame.sprite.Group()

AsteroidField.containers = (updatable_group)  # Set containers attribute


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    shot_group = pygame.sprite.Group()    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shot_group)  # Instantiate Player
    asteroid_field = AsteroidField() # Instantiate AsteroidField

    asteroid_field.containers = (updatable_group, drawable_group)  # Set containers attribute

    updatable_group.add(player)
    drawable_group.add(player)

    asteroid_group = pygame.sprite.Group()

    Asteroid.containers = (asteroid_group, drawable_group, updatable_group)

    updatable_group.add(asteroid_field)

    updatable_group.add(shot_group)
    drawable_group.add(shot_group)



    
    #Game Loop
    while True:

        dt = fps.tick(60) / 1000  # This gives us delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        
        #player.update(dt)
        for updatable in updatable_group:
            
            updatable.update(dt)

        #shot_group.update(dt)
        for shot in shot_group:
            #print("Updating shot")
            shot.update(dt)

        #Check for collisions
        for asteroid in asteroid_group:
            if player.collides_with(asteroid):
                print("Game Over!")
                return
            
            for shot in shot_group:
                if asteroid.collides_with(shot):
                    new_asteroid_1, new_asteroid_2 = asteroid.split()
                    shot.kill()
                    if new_asteroid_1 is not None:
                        asteroid_group.add(new_asteroid_1, new_asteroid_2)
                        drawable_group.add(new_asteroid_1, new_asteroid_2)
                        updatable_group.add(new_asteroid_1, new_asteroid_2)
                    break
    
        BLACK = (0, 0, 0)
        #screen.fill(BLACK)
        screen.fill("black")
        #player.draw(screen)
        for drawable in drawable_group:
            drawable.draw(screen)

        #add these to work elswehere later
        for shot in shot_group:
            shot.draw(screen)

        pygame.display.flip()


        









#This line ensures the main() function is only called
#when this file is run directly
if __name__ == "__main__":
    main()