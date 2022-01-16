x = 0
y = 0

def setup():
    size (600,600)
    rectMode(CENTER)
def draw():
    global x,y
    background (255,255,255)
    fill (255,255,0)
    if mousePressed:
        if mouseX > (x-25) and mouseX < (x+25) and mouseY > (y-25) and mouseY < (y+25) :
            mouseDragged()
    rect(x,y,50,50)
def mouseDragged():
    global y,x
    x = mouseX
    y = mouseY
    if x > width:
        x = width
    if x < 0:
        x = 0
    if y >height:
        y = height
    if y < 0:
        y = 0
