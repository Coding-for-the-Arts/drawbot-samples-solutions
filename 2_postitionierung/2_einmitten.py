"""
Form einmitten

- Kannst du das Quadrat einmitten?
- Kannst du posX und posY so definieren, dass es auch dann
  eingemittet wird, wenn die Masse der Fläche sich ändern.
  z.B. newPage("A4Landscape"), newPage(1000, 1000)
"""

newPage("A4")

print("Breite:", width())
print("Höhe:", height())

side = 300
posX = width()/2-side/2
posY = height()/2-side/2

fill(1, 0, 0)
rect(posX, posY, side, side)
