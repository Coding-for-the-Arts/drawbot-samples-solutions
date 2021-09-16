"""
Random Printmuster

- Schaffst du es z.B. diesen Output auf der Konsole auszugeben?

*** %%% *** %%%
%%% *** %%% ***
*** %%% *** %%%
%%% *** %%% ***

- Eine (grössere) Herausforderung: Pyramiden zu generieren.

* 
* * 
* * * 
* * * * 
* * * * * 

"""

newPage(300, 300)

# Pattern
for i in range(4):
    randomNumber = random()
    if (i%2 ==0):
        print(" *** " + " %%% " + " *** " + " %%% ")
    else:
         print(" %%% " + " *** " + " %%% " + " *** ")


# Pyramid
for i in range(6):
    for j in range(i):
        print('*', end=' ')
    print('')

