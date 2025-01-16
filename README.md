# 2048-game

2048 is a game made by another developer on github (Gabriele Ciruli).
I am a beginner python developer at this time and with a little help from some guide and a lot of retyping the same fucking thing for 2 hours 
I remade the game (probably worse than he did) and to say the least Im proud and very appreciative that YOU have taken the time to download this and check it out.

GAMEPLAY:

played on a 4x4 "mat"
every time you make a move all the numbers move as far as they can in the direction you pressed
for example if you pressed d:

starting mat__________mat after you press d

0, 0, 2, 0,__________0, 0, 0, 2,

0, 2, 0, 0,__________0, 0, 0, 2,

0, 0, 0, 0,__________0, 0, 0, 0,

0, 0, 0, 0,__________0, 0, 0, 0,


then, the program will generate another 2 value in an empty cell

empty cells are represented with a 0 (I tried to make some code to replace the 0 with a space but it ended up looking confusing)

if any 2 numbers of the same value end up colliding they merge and double (for example in the diagram above if you pressed up or down after the d press the twos would collide and merge to make a 4)

if you get 2048 in any cell you win

if you cant make any more moves you lose

it has a system that checks if you win or lose 

the controls are listed when you start the game.


run the file in your python code editor to play (run 2048.py logic.py is just a bunch of functions that 2048.py uses to make the game work)
