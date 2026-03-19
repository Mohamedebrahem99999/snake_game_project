from turtle import Turtle
class Score(Turtle):
    def __init__(self,score_position,game_over_message_position,clear_message_position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("yellow")
        self.clear_message_position = clear_message_position
        self.score_position = score_position
        self.game_over_message_position = game_over_message_position
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(self.score_position)
        self.write(f"Max Score = {self.get_highscore()}    Score = {self.score}",
                    align="center",
                    font=("Courier", 17, "normal"))
        self.goto(self.clear_message_position)
        self.write(f"Press Space To Clear Highscore",
                   align="center",
                   font=("Courier", 12, "normal"))

    def increase_score(self,score):
        self.score += score

    def game_over(self):
        self.clear()
        self.goto(self.game_over_message_position)
        if self.get_highscore() < self.score:
            self.save_highscore()

        self.write(f"Game Over\nScore = {self.score}\nMax Score = {self.get_highscore()}",
                   align = "center",
                   font = ("Courier", 30, "normal"))

    def get_highscore(self):
        with open("score.txt", "r") as my_file:
            content = my_file.read().strip()
            return int(content) if content else 0

    def save_highscore(self):
        with open(r"score.txt", "w") as my_file:
            my_file.write(str(self.score))

    def clear_max_score(self):
        """clears the maximum score and resets it to zero"""
        with open("score.txt", "w") as my_file:
            my_file.write(str(0))

    def reset_score(self):
        self.clear()
        self.score = 0
        self.update_scoreboard()