bg = 0
count = 0
fps = 0

def  setup():
    size(600,600)
def draw():
    

    global bg, count, fps
    fps = fps + 1
    background(bg)
    fill(255)
    rectMode(CENTER)
    rect(300,300,100,50)
    fill (0,0,0)
    textAlign(CENTER, CENTER)
    text (count,300,300)
    text (fps ,200,200)
def mouseClicked():
    global bg, count,fps
    if mouseX > 250 and mouseX < 350 and mouseY > 275 and mouseY < 325:
        count = count + 1000000000
        bg = 255
         
     
     
     
     
