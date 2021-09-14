"""
Überlagerung
"""

newPage(1000, 1000)

fill(1)
stroke(0)
strokeWidth(4)

step = 40
for i in range(10):
    translate(step, step)
    rect(0, 0, 400, 300)
    
"""
- Füge auf einer Zeile zwischen translate() und rect() eine Rotation ein, z.B. rotate(-2)
"""