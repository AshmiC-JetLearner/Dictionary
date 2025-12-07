import pgzrun
import random, time
WIDTH=600
HEIGHT=500
score=0
game_over=False
jerry=Actor("Jerry")
tom=Actor("Tom")

tom.pos=(100,100)
jerry.pos=(400,300)
msg=" "

def draw():
    screen.blit("kitchen",0,0)
    tom.draw()
    jerry.draw()
    screen.draw.text("Score: "+(score),color="black",topleft=(10,10))
    if game_over:
        screen.fill("yellow")
        global msg
        msg="Time's up!/n" \
        " Your final score:"
        screen.draw.text(msg+str(score),midtop(WIDTH/2,20),fontsize=50,color="red")
    


pgzrun.go()
