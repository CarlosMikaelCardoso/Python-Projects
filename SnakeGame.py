from tkinter import *
import random

GAME_WIDTH = 1000
GAME_HEIGHT = 600
SPEED = 80
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = [[0, 0] for _ in range(BODY_PARTS)]
        self.squares = []

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="Snake")
            self.squares.append(square)

    def move(self, x, y):
        self.coordinates.insert(0, [x, y])
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        self.squares.insert(0, square)

    def grow(self):
        x, y = self.coordinates[0]
        self.move(x, y)

    def shrink(self):
        del self.coordinates[-1]
        canvas.delete(self.squares[-1])
        del self.squares[-1]

    def get_head_position(self):
        return self.coordinates[0]

class Food:
    def __init__(self):
        self.randomize_position()
        self.food_id = canvas.create_oval(self.coordinates[0], self.coordinates[1],
                                          self.coordinates[0] + SPACE_SIZE, self.coordinates[1] + SPACE_SIZE,
                                          fill=FOOD_COLOR, tag="food")

    def randomize_position(self):
        max_x = int(GAME_WIDTH / SPACE_SIZE) - 1
        max_y = int(GAME_HEIGHT / SPACE_SIZE) - 1
        self.coordinates = [random.randint(0, max_x) * SPACE_SIZE,
                            random.randint(0, max_y) * SPACE_SIZE]

def next_turn(snake, food):
    if not game_running:
        return

    x, y = snake.get_head_position()

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Mover a cobra primeiro
    snake.move(x, y)

    # Verificar colisões após a cobra se mover
    if check_collisions(snake):
        game_over()
        return

    # Verificar se a cobra comeu a comida
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score {}".format(score))
        print("Food eaten, score:", score)

        # Deletar comida antiga
        canvas.delete("food")

        # Recriar comida
        food.randomize_position()
        food.food_id = canvas.create_oval(food.coordinates[0], food.coordinates[1],
                                          food.coordinates[0] + SPACE_SIZE, food.coordinates[1] + SPACE_SIZE,
                                          fill=FOOD_COLOR, tag="food")
        print("New food position:", food.coordinates)

        # Crescer a cobra
        snake.grow()
        print("Snake grew. New size:", len(snake.coordinates))
    else:
        # Diminuir o rabo se não houver comida
        snake.shrink()

    # Continuar o loop
    window.after(SPEED, next_turn, snake, food)



def change_direction(new_direction):
    global direction
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

def check_collisions(snake):
    x, y = snake.get_head_position()

    # Checar colisão com paredes
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        print("Collision with wall at:", x, y)  # Depuração
        return True

    # Checar colisão com o corpo da cobra
    if [x, y] in snake.coordinates[1:]:
        print("Collision with self at:", x, y)  # Depuração
        return True

    return False


def game_over():
    global game_running
    game_running = False
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")
    restart_button = Button(window, text="Restart", font=('consolas', 20), command=restart_game)
    restart_button.pack()

def restart_game():
    global score, direction, game_running
    score = 0
    label.config(text="Score {}".format(score))
    canvas.delete(ALL)
    global snake, food
    snake = Snake()
    food = Food()
    direction = 'down'
    game_running = True
    next_turn(snake, food)

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'
game_running = True

label = Label(window, text="Score {}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()
print("Food created. game_running:", game_running)

next_turn(snake, food)

window.mainloop()
