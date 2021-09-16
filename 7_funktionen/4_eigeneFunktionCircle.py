"""
Funktionen als Werkzeuge

Kannst du die Funktion so umschreiben, dass der Kreis immer auf der
Position x/y eingemittet wird?  
"""

def circle(x, y, dia):
    # zeichnet einen Kreis an Position x/y
    # mit Durchmesser dia
    oval(x-dia/2, y-dia/2, dia, dia)

newPage(1000, 1000)
circle(width()/2, height()/2, 200)