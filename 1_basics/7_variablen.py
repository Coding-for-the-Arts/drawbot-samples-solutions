"""
Drei Formen mit der gleichen Y-Position

Eine Variable zum Wiederverwenden eines Wertes.
"""

newPage(1000, 1000)

posY = 0

rect(100, posY, 150, 150)

oval(400, posY, 150, 150)

polygon((700, posY), (880, posY), (790, 150), close=True)

"""
«posY» ist eine Variable.
Das Gleichzeichen bewirkt eine Wertzuweisung: Die Variable
wird mit einem Wert assoziiert.
Auf diese Weise kannst du den gleichen Wert an mehr als 
einer Stelle im Programm verwenden.

- Ändere den Wert von posY, so dass die Formen 400 Einheiten
  Abstand vom unteren Rand haben.
- Es entsteht ein Fehler beim Dreieck. Kannst du die Spitze
  des Dreiecks wieder korrekt positionieren?
- Kannst du es so programmieren, dass sich die Spitze
  des Dreiecks automatisch richtig positioniert, wenn du
  posY änderst?

Terminologie: «Wertzuweisung»
"""