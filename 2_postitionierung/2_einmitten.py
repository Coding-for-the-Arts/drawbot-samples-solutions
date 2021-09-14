"""
Form einmitten
"""

newPage("A4")

print("Breite:", width())
print("Höhe:", height())

side = 300
posX = 0
posY = 0

fill(1, 0, 0)
rect(posX, posY, side, side)

"""
- Kannst du das Quadrat einmitten?
- Kannst du posX und posY so definieren, dass es auch dann
  eingemittet wird, wenn die Masse der Fläche sich ändern.
  z.B. newPage("A4Landscape"), newPage(1000, 1000)

Tipp:
Die Funktionen width() und height() liefern die Höhe und Breite der Hintergrundläche.
"""