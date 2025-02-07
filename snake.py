import pygame
import random
import time

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Set display width and height
WIDTH = 600
HEIGHT = 400
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")

# Game clock
clock = pygame.time.Clock()

# Snake block size
BLOCK_SIZE = 10

# Snake speed (can be adjusted according to difficulty)
SPEEDS = {"easy": 15, "medium": 20, "hard": 25}

# Font settings
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display score
def our_score(score):
    value = score_font.render("Your Score: " + str(score), True, BLACK)
    DISPLAY.blit(value, [0, 0])

# Function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    DISPLAY.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Function to draw the snake
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(DISPLAY, GREEN, [x[0], x[1], block_size, block_size])

# Function to generate food
def generate_food():
    return [random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
            random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]

# Main game loop function
def gameLoop(difficulty):
    game_over = False
    game_close = False

    # Initial snake position
    x1 = WIDTH // 2
    y1 = HEIGHT // 2

    # Initial snake movement
    x1_change = 0
    y1_change = 0

    # Snake body (list of coordinates)
    snake_List = []
    Length_of_snake = 1

    # Generate food
    foodx, foody = generate_food()

    # Game speed (based on difficulty)
    speed = SPEEDS[difficulty]

    while not game_over:

        while game_close:
            DISPLAY.fill(BLUE)
            message("You Lost! Press C-Play Again or Q-Quit", RED)
            our_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop(difficulty)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        # Check for boundary collision
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        DISPLAY.fill(BLUE)

        pygame.draw.rect(DISPLAY, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if snake hits itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_List)
        our_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food()
            Length_of_snake += 1

        clock.tick(speed)

    pygame.quit()
    quit()

# Function to select difficulty
def choose_difficulty():
    print("Choose Difficulty: ")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        return "easy"
    elif choice == "2":
        return "medium"
    elif choice == "3":
        return "hard"
    else:
        print("Invalid choice. Defaulting to Easy.")
        return "easy"

# Main function to start the game
if __name__ == "__main__":
    difficulty = choose_difficulty()
    gameLoop(difficulty)