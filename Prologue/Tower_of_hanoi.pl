 / * Coded by Shashwat Raj
Prologue program of solving Tower-of-Hanoi*/

/* When exactly one disk is there in Tower of Hanoi*/
move(1,X,Y,_) :-
    write('Move top disk from '),
    write(X),
    write(' to '),
    write(Y),
    nl.

/* When N no. of disk are there in Tower of Hanoi*/
move(N,X,Y,Z) :-
  N>1,
  M is N-1,
  move(M,X,Z,Y),
  move(1,X,Y,_),
  move(M,Z,Y,X).
