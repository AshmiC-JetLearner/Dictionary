import pgzrun,random
WIDTH=450
HEIGHT=450
def draw():
    r=255
    g=0
    b=random.randint(0,255)
    radius=100
    for i in range(20):
        screen.draw.circle((WIDTH//2,HEIGHT//2),radius,(r,g,b))
        r=r-10
        g=g+10
        radius=radius-5
        #radius -= 5
pgzrun.go()
