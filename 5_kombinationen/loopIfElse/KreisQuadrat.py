"""
If-Else: Kreis oder Quadrat? 

Ändere den Code so, dass jeder zweite Kreis zu einem Quadrat wird.
"""

newPage(300, 300)

diameter = 20
middle = height() / 2
step = int(width() / diameter)

for i in range(step):
    if (i%2 == 0):
         oval(diameter*i, middle, diameter, diameter)
    else: 
        rect(diameter*i, middle, diameter, diameter)