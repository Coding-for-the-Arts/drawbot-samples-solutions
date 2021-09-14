"""
Random Printmuster

Das Programm zeichnet nichts auf die Fläche, sondern schreibt in die Konsole.
"""

for i in range(10):
    randomNumber = random()
    if randomNumber > 0.2:
        print(" * " + "%")
    else:
        print(" % " + "#" )

"""
- Versuche, Schritt für Schritt nachzuvollziehen, was beim ausführen dieses Scripts passiert.
- Eine (kleine) Herausforderung: Kannst du ein eigens, komplexeres Muster generieren?
- Schaffst du es z.B. diesen Output auf der Konsole auszugeben?

*** %%% *** %%%
%%% *** %%% ***
*** %%% *** %%%
%%% *** %%% ***

- Eine (grössere) Herausforderung: Pyramiden zu generieren.
(Tipp für Forgeschrittene: Loop im Loop)
"""