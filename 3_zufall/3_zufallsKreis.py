"""
Ein Kreis zufälliger Grösse an zufälliger Position.

- Kannst du die Variablen randomX und randomY so ändern, dass der Kreis nie über den Rand der Fläche ragt?
"""

newPage("A4")

pageWidth = width()
pageHeight = height()

randomDiameter = random() * pageWidth

randomX = random() * (pageWidth - randomDiameter)
randomY = random() * (pageHeight - randomDiameter)

oval(randomX, randomY, randomDiameter, randomDiameter)

