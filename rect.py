import pgzrun, random
WIDTH=300
HEIGHT=300
def draw():
    r=255
    g=0
    b=random.randint(0,255)
    width=WIDTH-200
    height=HEIGHT-200
    for i in range(8):
        rect=Rect(0,0),(width,height)
        rect.center=(150,150)
        screen.draw.rect(rect,(r,g,b))
        r=r-10
        g=g+10
        width=width-10
        height=height-10

pgzrun.go()
