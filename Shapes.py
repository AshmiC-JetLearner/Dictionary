import pgzrun,random
WIDTH=450
HEIGHT=450
def draw():
    r=0
    g=255
    b=random.randint(0,255)
    width=WIDTH
    height=HEIGHT-200
    screen.draw.filled_circle((100,100),20,(255,0,0))
    for i in range(20):
        rect=Rect((0,0),(width,height))
        rect.center=(WIDTH//2,HEIGHT//2)
        screen.draw.rect(rect,(r,g,b))
        r += 10
        g -= 10
        width -= 10
        height -= 10
pgzrun.go()
