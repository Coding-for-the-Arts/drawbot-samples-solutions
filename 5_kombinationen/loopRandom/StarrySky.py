"""
Random Starry Sky

- Was passiert, wenn du Zeile 13 zu oval(dia, dia, dia, dia) änderst? 
- Warum braucht es für die x- und y-Position seperate Zufallswerte?
"""

newPage(300, 300)

fill(0)
rect(0, 0, 300, 300)

for i in range (200):
    dia = random() * 3
    fill(random())
    oval(dia, dia, dia, dia)
    
    