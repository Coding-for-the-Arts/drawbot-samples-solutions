"""
Einmitten und rotieren

- Kannst du das Rechteck einmitten, indem du die ersten beiden Argumente der Funktion rect() änderst?
"""

newPage(1000, 1000)

posX = width() / 2
posY = height() / 2

rectSide = 200

translate(posX, posY)
rotate(30)

rect(0-rectSide/2, 0-rectSide/2, rectSide, rectSide)

