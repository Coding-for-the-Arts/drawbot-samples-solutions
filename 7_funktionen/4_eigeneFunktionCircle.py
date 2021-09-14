"""
Funktionen als Werkzeuge

Funktionen können dir helfen, Problemstellungen zu vereinfachen.  
"""

def circle(x, y, dia):
    # zeichnet einen Kreis an Position x/y
    # mit Durchmesser dia
    oval(x, y, dia, dia)

newPage(1000, 1000)
circle(width()/2, height()/2, 200)
"""
Der Gewinn durch diese Funktion ist nicht so gross, aber immerhin:
du musst den Durchmesser nur noch einmal angeben, statt zweimal,
wie in der Funktion oval().

Kannst du die Funktion so umschreiben, dass der Kreis immer auf der
Position x/y eingemittet wird?
"""