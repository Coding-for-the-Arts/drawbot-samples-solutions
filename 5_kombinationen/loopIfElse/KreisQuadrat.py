"""
If-Else: Kreis oder Quadrat? 
"""

newPage(300, 300)

diameter = 20
middle = height() / 2
step = int(width() / diameter)

for i in range(step):
    if True:
        oval(diameter * i, middle, diameter, diameter)
    else: 
        print("False")

   
"""
Frage: 
    - Was geschieht nach if ...?
    - Was geschieht wenn du den Wert zu 'False' änderst? 
    - Was geschieht wenn statt 'True' zu 'i > 14' schreibst?

Aufgabe: 
    - Ändere den Code so, dass jeder zweite Kreis 
      zu einem Quadrat wird.
    
Tipp: 
    - Mit dem Operator % (Modulo) kannst du herausfinden,
      ob eine Zahl gerade oder ungerade ist. 
      Bsp. 9%3 == 0    -> TRUE    9 lässt sich durch 3 teilen 
           5%3 == 0    -> FALSE   5 lässt sich nicht durch 3 teilen 
                     
Bemerkung: 
      Die Funktion int(...) verwandelt eine Fliesskommazahl (Float) in einen 
      ganzzahligen Wert (Integer).
      Bsp. num1 = 5.9 
           print(num1)      -> 5.9
           num2 = int(num1)  
           print(num2)      -> 5      
"""

# # Lösung:
# for i in range(step):
#     if (i%2 == 0):
#          oval(diameter*i, middle, diameter, diameter)
#     else: 
#         rect(diameter*i, middle, diameter, diameter)