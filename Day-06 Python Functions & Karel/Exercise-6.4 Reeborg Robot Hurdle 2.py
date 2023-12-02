# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
def turn_right_move_fun():
    turn_left()
    turn_left()
    turn_left()
    move()
def move_left_move_fun():
    move()
    turn_left()
    move()
def jump():
    move_left_move_fun()
    turn_right_move_fun()
    turn_right_move_fun()
    turn_left()

while not at_goal():
    jump()
