% State (monkey_hor_pos, monkey_ver_pos, box_pos,hasBanana)

%
move(state(middle,onBox,middle,noBanana),grasp, state(middle,onBox,middle,hasBanana)).
move(state(P1,onfloor,P1,HasB),climb, state(P1,onBox,P1,HasB)).
move(state(P1,onfloor,P1,HasB),push(P1,P2), state(P2,onfloor,P2,HasB)).
move(state(P1,onfloor,Box,HasB),walk(P1,P2), state(P2,onfloor,Box,HasB)).
canget(state(_,_,_,hasBanana)).
canget(S1):- move(S1,M,S2),canget(S2),write(M),nl.


%query
%canget(state(atdoor,onfloor,atwindow,noBanana)).
%Canget(state(atdoor,inair,atwindow,noBanana)).
%canget(state(atdoor,onBox,atdoor,noBanana)).
