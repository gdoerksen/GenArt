def setup():
    size(1000,1000)
    background(255, 255, 255)
    
    noStroke()
    fill(15, 15, 15, 5)
    for i in range(30):
        circle(550, 550, 300 - i*5)
    
    noStroke()
    fill(176, 224, 230)
    circle(500,500,300)
