% listar([]):-write("FIN").
% listar([H|T]):-write(H),write("-"),listar(T).

% sumar([],0).
% sumar([H|T],S):-sumar(T,S2), S is S2+H.

% encontrar([],_):-write("Valor no encontrado").
% encontrar([H|_],H):-write("Valor encontrado").
% encontrar([_|T],B):-encontrar(T,B).

% mayor([],V):-write("Mayor valor: "),write(V).
% mayor([H|T],V):-H>=V,mayor(T,H).
% mayor([H|T],V):-H<V,mayor(T,V).

:-use_module(library(pce)).

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
esposo(H,M):-progenitor(H,A), progenitor(M,A).
hermanoauxiliar(H1,H2):-progenitor(P,H2), progenitor(P,H1),H1\=H2.
cunadoauxiliar(P1,P2):-esposo(P2,A),hermanoauxiliar(A,P1).
hermano(H1,H2):-(progenitor(P,H2), progenitor(P,H1),H1\=H2)->presentacion(H1,"es hermano de ",H2).
primo(P1,P2):-(tio(T,P1),progenitor(T,P2))->presentacion(P1,"es primo de ",P2).
abuelo(A,N):-(progenitor(P,N), progenitor(A,P))->presentacion(A,"es abuelo de ",N).
cunado(P1,P2):-(esposo(P2,A),hermanoauxiliar(A,P1))->presentacion(P1,"es cunado de ",P2).
concunado(P1,P2):-(esposo(P1,A),hermanoauxiliar(A,B),esposo(B,P2),not(cunadoauxiliar(P1,P2)))->presentacion(P1,"es concunado de ",P2).
tio(T,S):-(progenitor(P,S), hermanoauxiliar(T,P))->presentacion(T,"es tio de ",S).


:-new(D, dialog("Register")),
send(D, append, new(label)),
send(D, append, new(Nombre1, text_item(nombre1))),
send(D, append, new(Nombre2, text_item(nombre2))),
send(D, append, button(hermano, message(@prolog,hermano,Nombre1?selection, Nombre2?selection))),
send(D, append, button(primo, message(@prolog,primo,Nombre1?selection, Nombre2?selection))),
send(D, append, button(abuelo, message(@prolog,abuelo,Nombre1?selection, Nombre2?selection))),
send(D, append, button(cunado, message(@prolog,cunado,Nombre1?selection, Nombre2?selection))),
send(D, append, button(concunado, message(@prolog,concunado,Nombre1?selection, Nombre2?selection))),
send(D, append, button(tio, message(@prolog,tio,Nombre1?selection, Nombre2?selection))),
send(D, open).

% Base de reglas para impresion

presentacion(I1,I2,I3)
:-new(D, dialog("Entrada")),
send(D, append, label(asd, I1)),
send(D, append, label(asd, I2)),
send(D, append, label(asd, I3)),
send(D, append, button(ok, message(D, destroy))),
send(D, default_button, ok),
send(D, open).