import pygame
import game


def main():
    pygame.init()
    snake_game = game.Game('snake')
    snake_game.run()


if __name__ == "__main__":
    main()
