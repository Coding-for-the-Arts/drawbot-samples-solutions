"""
Variablen schreiben

- Kannst du zwei Rechtecke so positionieren, dass das eine immer
  das untere linke Viertel der Fläche ausfüllt und das andere
  jeweils das obere rechte Viertel?
- Kannst du es so einrichten, dass es auch funktioniert, wenn es
  newPage("A4") heisst?
"""

newPage("A4")

rect1x = 0
rect1y = 0
rect1width = width() / 2
rect1height = height() / 2

rect2x = width() / 2
rect2y = height() / 2
rect2width = width() / 2
rect2height = height() / 2

rect(rect1x, rect1y, rect1width, rect1height)
rect(rect2x, rect2y, rect2width, rect2height)
