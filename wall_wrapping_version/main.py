from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score
#========================== *  Window Setup  * ==========================
window = Screen()
window.bgcolor("black")
window.setup(width = 900,height = 500)
#========================== *  CONSTANTS  * ==========================
WIDTH = int(window.window_width()/2)
HEIGHT = int(window.window_height()/2)

FOOD_EATING_DISTANCE = 15
SCORE_BOUNDARY_OFFSET = 8
FOOD_BOUNDARY_OFFSET = 18

CLEAR_MESSAGE_POSITION = (0,HEIGHT-20)
SCORE_POSITION= (0, -HEIGHT + SCORE_BOUNDARY_OFFSET)
GAME_OVER_MESSAGE_POSITION = ( 0,30 )

SNAKE_STEPS = 3
SNAKE_ACCELERATION = .4
INITIAL_NUMBER_OF_PARTS  = 10
HEAD_STRETCH_SIZE = .95
BODY_STRETCH_SIZE = .75
SNAKE_BODY_STRETCH = 2 #number of segments the body of the snake increases by
SNAKE_SPEED = 0 #fastest

BIG_FOOD_SCORE = 3
SMALL_FOOD_SCORE = 1

SCREEN_SLEEP_DURATION = .013
#========================== * Stop window update * ==========================
window.tracer(0)
#========================== * Classes Instantiation * ==========================
score = Score(CLEAR_MESSAGE_POSITION,
              SCORE_POSITION,
              GAME_OVER_MESSAGE_POSITION
              )
snake = Snake(SNAKE_STEPS,
              SNAKE_ACCELERATION,
              SNAKE_SPEED,
              INITIAL_NUMBER_OF_PARTS,
              HEAD_STRETCH_SIZE,
              BODY_STRETCH_SIZE,
              WIDTH,
              HEIGHT
              )
food = Food(WIDTH,HEIGHT,FOOD_EATING_DISTANCE)
#========================== *(snake head definition)* ==========================
head = snake.head #to detect the snake collision with the walls and the food eating
#========================== ******************** ==========================
#========================== *  Main Function  * ==========================
#========================== ********************* ==========================
def main() :
    window.listen()

    window.onkey(snake.move_right, "Right")
    window.onkey(snake.move_left, "Left")
    window.onkey(snake.move_up, "Up")
    window.onkey(snake.move_down, "Down")
    window.onkey(score.clear_max_score, "space")

    while True:

        snake.wrap()
        snake.move()

        if head.distance(food) < FOOD_EATING_DISTANCE :
            #When the snake eats the food
            #The user gains points
            #The snake gets longer
            # The snake gets faster

            if food.get_size() == 1:
                score.increase_score(BIG_FOOD_SCORE)
            else:
                score.increase_score(SMALL_FOOD_SCORE)

            food.repositioning()

            for _ in range(SNAKE_BODY_STRETCH):
                snake.add_segment()

            snake.snake_accelerate()

        score.update_scoreboard()

        if snake.self_collision():
            # If the snake ate itself, the game is over
            window.bgcolor("red")
            score.game_over()
            break
        time.sleep(SCREEN_SLEEP_DURATION)
        window.update()

if __name__ == "__main__" :
    main()
    while window.textinput(title = "Again?",
                           prompt = "Would you like to play again(y/n)") == "y":
        snake.reset()
        window.bgcolor("black")
        score.reset_score()
        main()

window.exitonclick()