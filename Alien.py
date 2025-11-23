import pgzrun,random
TITLE="Shoot the Alien"
WIDTH=550
HEIGHT=350
msg=" "
alien=Actor("alien")#creating alien using actor funtion
def draw():
    screen.clear()
    screen.fill(color=(0,225,30))
    alien.draw()#to make alien visible on screen
    screen.draw.text(msg,center=(275,175),fontsize=30,color="Black")
 #to place alien randomly on the screen   
def place_alien():
    alien.x=random.randint(30,WIDTH-60)
    alien.y=random.randint(30,HEIGHT-60)


def on_mouse_down(pos):
    global msg
    if alien.collidepoint(pos):
        msg="Good shot! Congrats!"
        place_alien()
    else:
        msg="Bad luck! Try again!" 
place_alien()


pgzrun.go()
