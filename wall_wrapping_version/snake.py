from turtle import Turtle
class Snake:
    def __init__(self,steps,snake_acceleration,speed,initial_number_of_parts,head_stretch_size,body_stretch_size,width,height):
        self.head = None
        self.initial_number_of_steps = steps
        self.steps = steps
        self.snake_acceleration = snake_acceleration
        self.snake_parts = []
        self.speed = speed
        self.initial_number_of_parts = initial_number_of_parts
        self.head_stretch_size = head_stretch_size
        self.body_stretch_size = body_stretch_size
        self.create_snake()
        self.width = width
        self.height = height

    def create_snake(self):
        for _ in range(self.initial_number_of_parts):
            self.add_segment()
        self.head = self.snake_parts[0]
        self.head.shapesize(self.head_stretch_size,self.head_stretch_size)
        self.head.shape("circle")

    def add_segment(self):
        segment = Turtle(shape = "square")
        segment.shapesize(self.body_stretch_size, self.body_stretch_size)
        segment.color("white")
        segment.penup()
        segment.speed(self.speed)
        self.snake_parts.append(segment)
        segment.goto(self.snake_parts[-1].pos())

    def wrap(self):
        """wrapping walls"""
        if self.head.ycor() > self.height:
            self.head.goto(self.head.xcor(), -self.height)
        elif self.head.ycor() < -self.height:
            self.head.goto(self.head.xcor(), self.height)
        elif self.head.xcor() < -self.width:
            self.head.goto(self.width, self.head.ycor())
        elif self.head.xcor() > self.width:
            self.head.goto(-self.width, -self.head.ycor())

    def move(self):
        """moving the snake forward"""
        for ind in range(len(self.snake_parts) - 1, 0, -1):
            self.snake_parts[ind].goto(self.snake_parts[ind-1].pos())
        self.head.forward(self.steps)

    def move_right(self):
        """Orienting the snake right"""
        self.head.setheading(0 if  self.head.heading() != 180 else 180)

    def move_left(self):
        """Orienting the snake left"""
        self.head.setheading(180 if self.head.heading() != 0 else 0)

    def move_up(self):
        """Orienting the snake up"""
        self.head.setheading(90 if self.head.heading() != 270 else -90)

    def move_down(self):
        """Orienting the snake down"""
        self.head.setheading(-90 if self.head.heading() != 90 else 90)

    def snake_accelerate(self):
        """Increases the snake steps, hence its speed"""
        self.steps += self.snake_acceleration

    def self_collision(self):
        """Detects if the snake ate itself"""
        for part in self.snake_parts[1:]:
            if self.head.distance(part) < self.steps-1:
                return True
        return False

    def reset(self):
        for part in self.snake_parts:
            part.hideturtle()
            part.penup()
            part.goto(0,0)
        for part in self.snake_parts[:self.initial_number_of_parts]:
            part.showturtle()
        self.head.setheading(0)
        self.steps = self.initial_number_of_steps

        self.snake_parts = self.snake_parts[:self.initial_number_of_parts]