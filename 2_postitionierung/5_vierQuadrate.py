"""
Vier Quadrate in RGB

Versuche die Quadrate mit translate() nebeneinander anzuordnen, 
so dass sie die gesamte Fläche ausfüllen. 
"""

newPage(300, 300)

dia = width()/2

x=0
y=0

fill(1,0,0)
stroke(0)
rect(x, y, dia, dia);


# 1. Translate
translate(width()/2,0)

fill(0,1,0)
rect(x, y, dia, dia);


# 2. Translate
translate(0,height()/2)

fill(0,0,1)
rect(x, y, dia, dia);


# 3. Translate
translate(-width()/2,0)

fill(1,1,1)
rect(x, y, dia, dia);


