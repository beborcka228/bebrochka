y = 0  
def setup() :
    size(600,600)
def draw():
    global y
    x = 0
    while x < width:
        fill(random(100,250),random(100,250) ,random(100,250))
        rect (x,y,30,30)
        y = y + 30
    x = x - 3
    if x > height:
        noLoop()
