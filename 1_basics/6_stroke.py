"""
Linienfarbe
"""

newPage(1000, 1000)

fill(None)
stroke(0, 0, 1)

strokeWidth(2)

line((0, 0), (width(), height()))
oval(100, 100, 800, 800)

"""
- Mit der Funktion stroke() kannst du die Linienfarbe einstellen.
- Mit dem Wert "None" als Argument von fill() oder stroke()
  kannst du eine Farbe «abschalten».
- Probiere einige Formen so zu positionieren, dass sie sich überlagern.
- Schalte die Füll- und Linienfarben an/aus.
"""
