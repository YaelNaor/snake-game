import random
import pygame
import colors
import settings


class Snake:
    def __init__(self, start_x: int, start_y: int, block_count: int):
        self.x = start_x
        self.y = start_y
        self.block_count = block_count
        self.x_change = 0
        self.y_change = 0
        self.snake_body = []
        self.width_border = settings.WINDOW_WIDTH / 20
        self.height_border = settings.WINDOW_HEIGHT / 20
        self.food_x = random.randrange(settings.WINDOW_WIDTH)
        self.food_y = random.randrange(settings.WINDOW_HEIGHT)

    def handle_event(self, event):
        if event.key == pygame.K_LEFT:
            if not self.x_change == 10:
                self.x_change = -10
                self.y_change = 0
        elif event.key == pygame.K_RIGHT:
            if not self.x_change == -10:
                self.x_change = 10
                self.y_change = 0
        elif event.key == pygame.K_UP:
            if not self.y_change == 10:
                self.y_change = -10
                self.x_change = 0
        elif event.key == pygame.K_DOWN:
            if not self.y_change == -10:
                self.y_change = 10
                self.x_change = 0

    def update(self):
        self.x += self.x_change
        self.y += self.y_change

        snake_head = (self.x, self.y)

        self.snake_body.append(snake_head)

        if self.block_count < len(self.snake_body):
            self.snake_body.pop(0)

        # return_value = False
        for block in self.snake_body[:-1]:
            if snake_head == block:
                return True

        if self.x < 0 or self.y < 0 or self.x > settings.WINDOW_WIDTH or self.y > settings.WINDOW_HEIGHT:
            return True

        # eating the food
        if abs(self.x - self.food_x) < 10 and abs(self.y - self.food_y) < 10:
            # Calculated to prevent food from appearing in the sides
            self.food_x = random.randrange(self.width_border, settings.WINDOW_WIDTH - self.width_border)
            self.food_y = random.randrange(self.height_border, settings.WINDOW_HEIGHT - self.height_border)
            self.block_count += 1

        return False

    def draw(self, window):
        pygame.draw.rect(window, colors.PINK, [self.food_x, self.food_y, 10, 10])
        for block in self.snake_body:
            x, y = block
            pygame.draw.rect(window, colors.RED, [x, y, 10, 10])
