:-dynamic conecta/2.
conecta('INICIO','B').
conecta('B','A').
conecta('B','F').
conecta('B','C').
conecta('A','E').
conecta('F','G').
conecta('C','D').
conecta('C','G').
conecta('D','H').
conecta('G','H').
conecta('H','FINAL').
conectando_a(A,B):-conecta(A,B);conecta(B,A).
eliminando_a(A,B):-retract(conecta(A,B));retract(conecta(B,A)).
camino(A,_):-conecta(A,'FINAL'),write('FINAL'),write('<-'),write(A),write(' De ').
camino(ViejoPos,NuevoPos):-eliminando_a(ViejoPos,NuevoPos),camino(NuevoPos,_),write(' '),write(NuevoPos),write('<-'),write(ViejoPos),write(' De ').