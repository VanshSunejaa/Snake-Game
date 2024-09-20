import pygame
import random
from pygame.locals import QUIT, KEYDOWN
from pygame import K_ESCAPE, K_DOWN, K_LEFT, K_RIGHT, K_UP

# Define constants
BLOCK_SIZE = 20
FPS = 10
APPLE_SIZE = BLOCK_SIZE

class Block:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()  # Use convert_alpha for transparency
        self.x = x
        self.y = y

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def set_position(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # Initial positions
        self.direction = K_RIGHT  # Initial direction
        self.grow = False

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

    def walk(self):
        head_x, head_y = self.body[0]
        if self.direction == K_DOWN:
            head_y += BLOCK_SIZE
        elif self.direction == K_UP:
            head_y -= BLOCK_SIZE
        elif self.direction == K_LEFT:
            head_x -= BLOCK_SIZE
        elif self.direction == K_RIGHT:
            head_x += BLOCK_SIZE

        new_head = (head_x, head_y)
        self.body = [new_head] + self.body[:-1]

        if self.grow:
            self.body.append(self.body[-1])  # Add new segment
            self.grow = False

    def change_direction(self, new_direction):
        if (new_direction == K_LEFT and self.direction != K_RIGHT) or \
           (new_direction == K_RIGHT and self.direction != K_LEFT) or \
           (new_direction == K_UP and self.direction != K_DOWN) or \
           (new_direction == K_DOWN and self.direction != K_UP):
            self.direction = new_direction

    def check_collision(self, apple_pos):
        return self.body[0] == apple_pos

    def check_self_collision(self):
        return self.body[0] in self.body[1:]

    def check_boundary_collision(self, width, height):
        head_x, head_y = self.body[0]
        return head_x < 0 or head_x >= width or head_y < 0 or head_y >= height

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        pygame.display.set_caption("Pygame Snake Game")
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("resources/background.jpg").convert()  # Load background image
        self.snake = Snake()
        self.apple = Block("resources/apple.jpg", *self.random_apple_pos())
        self.score = 0
        self.running = True

    def random_apple_pos(self):
        x = random.randint(0, (self.surface.get_width() - APPLE_SIZE) // APPLE_SIZE) * APPLE_SIZE
        y = random.randint(0, (self.surface.get_height() - APPLE_SIZE) // APPLE_SIZE) * APPLE_SIZE
        return (x, y)

    def draw(self):
        self.surface.blit(self.background, (0, 0))  # Draw the background image
        self.snake.draw(self.surface)
        self.apple.draw(self.surface)
        # Draw the score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))  # White color for score
        self.surface.blit(score_text, (10, 10))
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.running = False
            elif event.key in [K_DOWN, K_LEFT, K_RIGHT, K_UP]:
                self.snake.change_direction(event.key)
        elif event.type == QUIT:
            self.running = False

    def draw_game_over(self):
        self.surface.blit(self.background, (0, 0))  # Draw the background image
        font = pygame.font.SysFont(None, 72)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        self.surface.blit(game_over_text, (self.surface.get_width() // 4, self.surface.get_height() // 3))
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)

            self.snake.walk()

            # Check if snake has eaten the apple
            if self.snake.check_collision((self.apple.x, self.apple.y)):
                self.score += 1
                self.snake.grow = True
                self.apple.set_position(*self.random_apple_pos())

            # Check for collisions
            if self.snake.check_self_collision() or self.snake.check_boundary_collision(self.surface.get_width(), self.surface.get_height()):
                self.draw_game_over()
                pygame.time.wait(2000)  # Pause to display game over screen
                self.running = False  # End the game

            self.draw()
            self.clock.tick(FPS)  # Control the speed of the snake

        pygame.quit()

# Start the game
if __name__ == "__main__":
    game = Game()
    game.run()
