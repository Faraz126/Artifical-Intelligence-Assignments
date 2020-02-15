% teaches(T, C, L) says that teacher 'T' is teaching course 'C' which is
% a lab based 'L' (true/false) course.

teaches(saleha,ai,false).
teaches(saleha,db,true).
teaches(waqar,graphics,false).
teaches(waqar,oop,true).
teaches(umair,gameprog,true).
teaches(samad,dl,true).
teaches(samad,prob,false).
teaches(musabbir,la,false).
teaches(shahid,algo,false).
teaches(nadia,pfun,true).
%hasDone(S,C) says that students 'S' has done course 'C'
hasDone(s1,pfun).
hasDone(s1,oop).
hasDone(s1,db).
hasDone(s2,pfun).
hasDone(s2,oop).
hasDone(s2,db).
hasDone(s3,pfun).
hasDone(s3,oop).
hasDone(s4,pfun).
hasDone(s4,oop).
hasDone(s4,db).
hasDone(s4,la).
%prereq(C1,C2) says that course C1 is a prereq of course C2.
prereq(pfun,oop).
prereq(pfun,db).
prereq(oop,ai).
prereq(oop,dl).
prereq(la,graphics).

solution(S):-
     S = [[s1, C1],
     [s2, C2],
     [s3, C3],
     [s4, C4],
     [s5, C5]],
     member([s1, C1],S), teaches(_,C1,L1), L1 = true,
     not(hasDone(s1, C1)),
     (not(prereq(_,C1)) ; prereq(P1, C1), hasDone(s1,P1)),

    member([s2, C2],S), teaches(_,C2,L2), L2 = false,
    C2 \= C1, not(hasDone(s2, C2)),
    (not(prereq(_, C2)); prereq(P2, C2), hasDone(s2, P2)),

    member([s3, C3],S), teaches(T3,C3,_), T3 \= saleha,
    C3 \= C2, C3 \= C1, not(hasDone(s3, C3)),
    (not(prereq(_,C3)); prereq(P3, C3), hasDone(s3, P3)),

    member([s4, C4],S), teaches(T4,C4,_), T4 = waqar,
    C4 \= C3, C4 \= C2, C4 \= C1,not(hasDone(s4, C4)),
    (not(prereq(_,C4)); prereq(P4, C4), hasDone(s4, P4)),

    member([s5, C5],S), teaches(_,C5,L5), L5 = true,
    C5 \= C4, C5 \= C3, C5 \= C2, C5 \= C1, not(hasDone(s5, C5)),
    (not(prereq(_,C5)); prereq(P5, C5), hasDone(s5, P5)).



% Please write your rules here....
%





























