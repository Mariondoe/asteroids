# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

print("Starting asteroids!")
from constants import *
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        BLACK = (0, 0, 0)
        screen.fill(BLACK)
        pygame.display.flip()









#This line ensures the main() function is only called
#when this file is run directly
if __name__ == "__main__":
    main()