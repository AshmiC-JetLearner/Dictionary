import pgzrun, random, time
WIDTH=600
HEIGHT=500
score=0
game_over=False
bee=Actor("Bee")
flower=Actor("Flower")

bee.pos=(100,100)
flower.pos=(400,300)
msg=" "

def  draw():
    screen.blit("Background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: "+(score),color="black",topleft=(10,10))
    if game_over:
        screen.fill("pink")
        global msg
        msg="Time's up!/n Your final score:"
        screen.draw.text(msg+str(score),midtop(WIDTH/2,20),fontsize=50,color="red")
    


pgzrun.go()
