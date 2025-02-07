# snake-game
This project is a Snake Game with Levels, developed using Pygame, a popular library for building 2D games in Python. The game features different difficulty levels, a scoring system, and game-over logic. Here’s an overview of its key components:

Project Breakdown

1. Game Setup
	•	The game initializes using pygame.init().
	•	The display size is set to 600x400 pixels.
	•	Colors are predefined for various elements like the snake, food, background, and messages.
	•	A game clock (pygame.time.Clock()) is used to control the game’s speed.

2. Snake and Movement
	•	The snake starts at the center of the screen.
	•	Movement is controlled by the arrow keys (UP, DOWN, LEFT, RIGHT).
	•	The snake’s body is stored in a list (snake_List), which grows when food is eaten.

3. Food Generation
	•	The food is randomly placed using the generate_food() function.
	•	When the snake eats food, the food is repositioned, and the snake grows in length.

4. Collision Detection
	•	The game ends if the snake:
	•	Hits the screen boundaries.
	•	Collides with itself.

5. Game Over Handling
	•	When the player loses, a message is displayed:
“You Lost! Press C-Play Again or Q-Quit”
	•	The player can press C to restart or Q to quit.

6. Difficulty Levels
	•	Players can choose from three difficulty levels:
	•	Easy (15 FPS)
	•	Medium (20 FPS)
	•	Hard (25 FPS)
	•	The speed of the snake is determined by the chosen difficulty.

7. User Input for Difficulty
	•	The game asks the player to select a difficulty level before starting.
	•	If an invalid option is chosen, the game defaults to “Easy”.



