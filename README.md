# Snake Game - Pygame Project

## Overview
This project is a recreation of the classic **Snake Game** using the Python library **Pygame**. Players control a snake to consume apples, growing longer with each apple eaten while avoiding collisions with the snake's own body or the game boundaries. The game keeps track of the player's score and displays a "Game Over" screen upon failure. The project focuses on implementing basic game mechanics, object-oriented programming, and handling real-time events in Python.

## Code Structure

### 1. `Block` Class
- **Purpose**: Represents individual blocks in the game, such as the apple.
- **Key Methods**:
  - `__init__(self, image_path, x, y)`: Initializes a block with its image and position.
  - `draw(self, surface)`: Draws the block on the screen.
  - `set_position(self, x, y)`: Updates the block's position.

### 2. `Snake` Class
- **Purpose**: Controls the snake's body, movement, and interactions.
- **Key Methods**:
  - `__init__(self)`: Initializes the snake's starting position and direction.
  - `draw(self, surface)`: Draws the snake on the screen.
  - `walk(self)`: Moves the snake one step in the current direction.
  - `change_direction(self, new_direction)`: Changes the snake's direction based on player input.
  - `check_collision(self, apple_pos)`: Checks if the snake has eaten the apple.
  - `check_self_collision(self)`: Checks if the snake has collided with itself.
  - `check_boundary_collision(self, width, height)`: Checks if the snake has collided with the game boundaries.

### 3. `Game` Class
- **Purpose**: Manages the game flow, including the game loop, event handling, and rendering.
- **Key Methods**:
  - `__init__(self)`: Initializes the game window, background, and game elements (snake and apple).
  - `random_apple_pos(self)`: Generates random positions for the apple within the game boundaries.
  - `draw(self)`: Renders the background, snake, apple, and score on the screen.
  - `handle_event(self, event)`: Handles user input, such as direction changes or game exit.
  - `draw_game_over(self)`: Displays the "Game Over" screen when the player loses.
  - `run(self)`: The main game loop that updates game elements and checks for collisions.

## Libraries Used
- **Pygame**: The core library used to create the game. Pygame provides functionalities for handling graphics, game loops, real-time events, and audio in Python.

### Key Pygame Functions:
- `pygame.display.set_mode()`: Creates the game window.
- `pygame.draw.rect()`: Draws the snake and other rectangular shapes.
- `pygame.event.get()`: Captures real-time user input (key presses, window close events, etc.).
- `pygame.time.Clock()`: Regulates the game's FPS (Frames Per Second).
- `pygame.image.load()`: Loads images for the game (e.g., background, apple).

## How to Run the Game
1. Ensure that you have Python installed (version 3.7+).
2. Install the Pygame library using pip:
   ```
   pip install pygame
   ```
3. Place the game files in a directory, ensuring the following structure:
   ```
   /snake_game
     ├── game.py
     └── resources
         ├── background.jpg
         └── apple.jpg
   ```
4. Run the game:
   ```
   python game.py
   ```

## Future Enhancements (Optional)
- Adding sound effects when the snake eats an apple or collides with walls.
- Implementing different difficulty levels by adjusting snake speed.
- Adding obstacles for more challenging gameplay.

## Disclaimer
This project is intended **only for learning purposes** and was created to demonstrate the use of Pygame and basic game mechanics. It is not optimized for user experience, and certain features (such as difficulty settings and polished UI) are minimal or absent.
