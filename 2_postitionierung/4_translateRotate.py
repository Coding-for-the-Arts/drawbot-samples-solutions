"""
Einmitten und rotieren
"""

newPage(1000, 1000)

posX = width() / 2
posY = height() / 2

rectSide = 200

translate(posX, posY)
rotate(30)

rect(0, 0, rectSide, rectSide)

"""
- Kannst du das Rechteck einmitten, indem du die ersten beiden Argumente der Funktion rect() änderst?
- Was passiert, wenn du die Zeilen mit translate() und rotate() vertauschst?
- Wie erklärst du dir die Auswirkungen von translate() und rotate()?
"""