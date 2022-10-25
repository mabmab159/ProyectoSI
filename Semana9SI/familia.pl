% Base de hechos
progenitor(alejandro, fernando).
progenitor(alejandro, raul).
progenitor(sabina, fernando).
progenitor(sabina, raul).
progenitor(fernando, leonardo).
progenitor(fernando, camila).
progenitor(karina,leonardo).
progenitor(karina, camila).
progenitor(raul, andre).
progenitor(raul, eduardo).
progenitor(vanessa, andre).
progenitor(vanessa, eduardo).
% Base de reglas
abuelo(A,N) :- progenitor(P,N), progenitor(A,P).
hermano(H1,H2):- progenitor(P,H2), progenitor(P,H1),H1\=H2.
tio(T,S):- progenitor(P,S), hermano(T,P).
esposo(H,M):- progenitor(H,A), progenitor(M,A).
primo(P1,P2):-tio(T,P1),progenitor(T,P2).
cunado(P1,P2):-esposo(P2,A),hermano(A,P1).
concunado(P1,P2):-esposo(P1,A),hermano(A,B),esposo(B,P2),not(cunado(P1,P2)).