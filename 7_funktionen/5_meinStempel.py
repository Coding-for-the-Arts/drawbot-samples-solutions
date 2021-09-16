"""
Dein Stempel

- Ändere die Funktion so, dass eine interessantere Formenkonfiguration zeichnet.
- Rufe sie aus einer Schleife heraus aus und drucke sie mehrfach auf die Fläche.
- Rotiere das Koordinatensystem jeweils um einige Grad, bevor du «stempelst».
"""

def myStamp(x, y):
    x1 = x + 50
    y1 = y + 50
    x2 = x + 50
    y2 = y - 50
    x3 = x - 50
    y3 = y - 50
    x4 = x - 50
    y4 = y + 50
    rect(x1, y1, 10, 10)
    rect(x2, y2, 10, 10)
    rect(x3, y3, 10, 10)
    rect(x4, y4, 10, 10)

newPage(1000, 1000)

for i in range(500):
    rotate(3)
    myStamp(i, i*2)



#Alternative
def myStamp(x, y):
    x1 = x + 50
    y1 = y + 50
    x2 = x + 50
    y2 = y - 50
    x3 = x - 50
    y3 = y - 50
    x4 = x - 50
    y4 = y + 50
    rect(x1, y1, 10, 10)
    rect(x2, y2, 10, 10)
    rect(x3, y3, 10, 10)
    rect(x4, y4, 10, 10)

newPage(1000, 1000)

for i in range(100):
    rotate(3)
    myStamp(random()*1000, random()*1000)


