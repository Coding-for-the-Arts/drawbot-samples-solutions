"""
Vier Quadrate in RGB

Die Funktion translate() verschiebt den Nullpunkt des Koordinatensystems.
"""

newPage(300, 300)

x = 0
y = 0
dia = width() / 2

fill(1, 0, 0)
stroke(0)
rect(x, y, dia, dia)

# 1. Translate
translate(30, 30)

fill(0, 1, 0)
rect(x, y, dia, dia)

# 2. Translate
translate(30, 30)

fill(0, 0, 1)
rect(x, y, dia, dia)

# 3. Translate
translate(30, 30)

fill(1, 1, 1)
rect(x, y, dia, dia)
print("x: ", x, " y: ", y)

"""
Fragen: 
    - Warum haben x und y auf Zeile 35 den Wert 0? 
    - Wie weit hat sich der Nullpunkt am Ende des Programms vom seinem Ursprung entfernt?
    
Aufgabe: 
    - Versuche die Quadrate mit translate() nebeneinander anzuordnen, 
      so dass sie die gesamte Fläche ausfüllen. 
  
Tipp: 
    - Benutze width() und height() um die Verschiebungen zu berechnen
"""



# # Lösung

# size(300,300)
# newPage(300, 300)

# dia = width()/2

# x=0
# y=0

# fill(1,0,0)
# stroke(0)
# rect(x, y, dia, dia);


# # 1. Translate
# translate(width()/2,0)

# fill(0,1,0)
# rect(x, y, dia, dia);


# # 2. Translate
# translate(0,height()/2)

# fill(0,0,1)
# rect(x, y, dia, dia);


# # 3. Translate
# translate(-width()/2,0)

# fill(1,1,1)
# rect(x, y, dia, dia);
