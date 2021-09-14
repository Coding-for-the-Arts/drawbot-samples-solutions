"""
Linienfarbe

- Probiere einige Formen so zu positionieren, dass sie sich überlagern.
- Schalte die Füll- und Linienfarben an/aus.
"""

newPage(1000, 1000)

fill(None)
stroke(0, 0, 1)

strokeWidth(2)
line((178, 82), (width(), height()))
line((0, 0), (width(), height()))
oval(100, 100, 800, 800)
oval(160, 160, 800, 800)
fill(1, 0, 0)
oval(268, 160, 800, 800)