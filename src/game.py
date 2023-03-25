import pygame, sys, time
from components import Board, Snake, Food # components
  
SIZE = (500, 500)
GRID_LINES = 20

CUBE_SIZE_X = SIZE[0] // GRID_LINES
CUBE_SIZE_Y = SIZE[1] // GRID_LINES

pygame.init()

class Game:
    def __init__(self) -> None:
        
        self.surface = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Snake ... by Your Mom")

        self.clock = pygame.time.Clock()
        self.clock_speed = 9

        self.board = Board(self.surface, SIZE, GRID_LINES, CUBE_SIZE_X, CUBE_SIZE_Y)
        self.board.create_grid()

        self.snake = Snake(self.surface, SIZE, GRID_LINES, CUBE_SIZE_X, CUBE_SIZE_Y)
        self.snake.start_snake()

        self.food = Food(self.surface, SIZE, GRID_LINES, CUBE_SIZE_X, CUBE_SIZE_Y)
        self.food.start_food() 

    def update(self) -> None:
        self.board.reset_surface()
        self.board.draw_score()
        self.board.draw_grid()

    def play(self) -> tuple():
        # move snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.speed_y = -1
                    self.snake.speed_x = 0
                if event.key == pygame.K_DOWN:
                    self.snake.speed_y = 1
                    self.snake.speed_x = 0
                if event.key == pygame.K_LEFT:
                    self.snake.speed_y = 0
                    self.snake.speed_x = -1
                if event.key == pygame.K_RIGHT:
                    self.snake.speed_y = 0
                    self.snake.speed_x = 1

        # collision
        if not self.snake.is_alive():
            game_over = True
            return game_over, self.board.score

        # eat food
        if self.food.pos_x == self.snake.pos_x and self.food.pos_y == self.snake.pos_y:
            self.board.score += 1
            if self.board.score % 5 == 0:
                self.clock_speed += 1

            self.snake.add_body()
            self.food.start_food()

        # spawn food
        self.food.spawn()

        # spawn and move snake
        self.snake.update_snake()
        self.snake.pos_x += self.snake.speed_x * CUBE_SIZE_X
        self.snake.pos_x %= SIZE[0]
        self.snake.pos_y += self.snake.speed_y * CUBE_SIZE_Y
        self.snake.pos_y %= SIZE[1]

        # update game
        pygame.display.flip()
        self.clock.tick(self.clock_speed)

        game_over = False
        return game_over, self.board.score

    def game_over(self) -> None:
        self.board.end()
        self.snake.update_snake()
        print(f'Score: {self.board.score}')
        time.sleep(2)

    def reset(self) -> None:
        self.snake.start_snake()
        self.food.start_food() 
        self.board.score = 0