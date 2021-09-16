"""
Switch on, switch off

1. Erstelle Variablen für die Hintergrundfarbe und die Farbe des Kreises
    
2. Schaffst du es folgende Bedingung herzustellen? 
    
       'True':  Kreis schwarz, Hintergrund weiss
       'False': Kreis weiss, Hintergrund schwarz
    
3. Kannst du eine Variable erstellen, die als Schalter funktioniert? 
   Wenn du den Wert der Variable änderst, ändert sich auch das Bild.
"""

newPage(100, 100)

switch = False
radius = 20


if (switch):
    background = 0
    figure = 1
else:
    background = 1
    figure = 0

fill(background)
rect(0, 0, width(), height())


fill(figure)
oval(width()/2-radius, height()/2-radius, radius*2, radius*2)


