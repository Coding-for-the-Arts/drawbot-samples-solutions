"""
Ein Kreis zufälliger Grösse an zufälliger Position.
"""

newPage("A4")

pageWidth = width()
pageHeight = height()

randomDiameter = random() * pageWidth

randomX = random() * pageWidth
randomY = random() * pageHeight

oval(randomX, randomY, randomDiameter, randomDiameter)

"""
- Kannst du die Variablen randomX und randomY so ändern, dass der Kreis nie über den Rand der Fläche ragt?
"""