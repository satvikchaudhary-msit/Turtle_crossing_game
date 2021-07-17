import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    #Detecting collisions with car
    for car_obj in car.car_obj:
        if car_obj.distance(player) < 20:
            game_is_on = False
            score.game_over()

    #Detecting Level Complete
    if player.ycor() > 280:
        player.starting_position()
        car.increase_carspeed()
        score.level_up()





screen.exitonclick()
