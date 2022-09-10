from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r'C:\DATA\PHYTON COURSE\StudioVisual Code\PROJECTS\100days_of_code\Snake_game_turtle_module\data.txt') as data:
            self.high_score = int(data.read())
        
        
        self.goto(0, 280)
        self.penup()        
        self.color("orange")
        self.hideturtle()
        self.write_score()
        
    

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High score: {self.high_score} ", align=ALIGNMENT, font=FONT)
    
    def update_score(self):
        self.score+=1
        #self.clear()
        self.write_score()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r'C:\DATA\PHYTON COURSE\StudioVisual Code\PROJECTS\100days_of_code\Snake_game_turtle_module\data.txt', "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()


       
        

        
        
        