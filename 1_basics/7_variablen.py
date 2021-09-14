"""
Drei Formen mit der gleichen Y-Position

- Ändere den Wert von posY, so dass die Formen 400 Einheiten
  Abstand vom unteren Rand haben.
- Es entsteht ein Fehler beim Dreieck. Kannst du die Spitze
  des Dreiecks wieder korrekt positionieren?
- Kannst du es so programmieren, dass sich die Spitze
  des Dreiecks automatisch richtig positioniert, wenn du
  posY änderst?
"""

newPage(1000, 1000)

posY = 0

rect(100, posY, 150, 150)

oval(400, posY, 150, 150)

# posY muss zum Y-Wert der Spitze addiert werden
polygon((700, posY), (880, posY), (790, 150), close=True)