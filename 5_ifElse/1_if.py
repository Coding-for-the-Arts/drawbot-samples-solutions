"""
Bedingungen

Dieses Programm zeichnet nichts auf die Fläche, sondern schreibt in die Konsole.
"""

randomValue = random()

print("Dieser Text wird immer in die Konsole geschrieben.")

if randomValue > 0.5:
    print("Dieser Text wird nur mit 50%-iger Wahrscheinlichkeit in die Konsole geschrieben.")

"""
Mit "if" wird eine Bedingung formuliert, die durch den Computer evaluiert werden kann.
Das Ergebnis dieser Evaluation lautet "wahr" (True) oder "falsch" (False).

In diesem Fall wird Zeile 10 nur ausgeführt, wenn die Variable randomValue einen
Wert enthält, der grösser als 0.5 ist.

Beachte, dass Zeilen des Programms, die nur ausgeführt werden,
wenn die Bedingung erfüllt ist, eingezogen sind.
"""