import pygame
import time
import colors
import settings
import snake


class Game:
    def __init__(self, caption: str):
        pygame.display.set_caption(caption)
        self.window = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        self.game_over = False
        self.snake = snake.Snake(300, 300, 1)
        self.clock = pygame.time.Clock()
        self.font_style = pygame.font.SysFont(None, 50)

    def run(self):
        while True:
            self._handle_events()
            self._update_snake()
            self._draw()
            if self.game_over:
                break

        self._show_message(settings.GAME_OVER_TEXT, colors.RED)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                self.snake.handle_event(event)

    def _update_snake(self):
        self.clock.tick(20)
        if not self.game_over:
            self.game_over = self.snake.update()

    def _draw(self):
        self.window.fill(colors.WHITE)
        self.snake.draw(self.window)
        pygame.display.update()

    def _show_message(self, msg, color):
        rendered_msg = self.font_style.render(msg, True, color)
        self.window.blit(rendered_msg, [
            settings.WINDOW_WIDTH / 2 - rendered_msg.get_width() / 2,
            settings.WINDOW_HEIGHT / 2 - rendered_msg.get_height() / 2
        ])
