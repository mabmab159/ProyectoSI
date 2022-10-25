:-dynamic tiene/1.
lista([]):-enfermedad(E),write(E).
lista([H|T]):-assert(tiene(H)),lista(T).
test(X) :-limpiar,lista(X).% write( 'Hola mundo cruel ' ),write(X).

enfermedad('E1'):-(tiene(s1);tiene(s2)),tiene(s3), (tiene(s4), tiene(s5), tiene(s6)) , tiene(s7), tiene(s8).
enfermedad('E2'):-(tiene(s1);tiene(s2)),tiene(s3),tiene(s10), tiene(s11), tiene(s12), tiene(s13).
enfermedad('E3'):- tiene(s3), tiene(s10), (tiene(s11),tiene(s12), tiene(s13)) , (tiene(s14), tiene(s15)) , tiene(s16).
enfermedad('E4'):-tiene(s3), tiene(s6), (tiene(s10); tiene(s16)), (tiene(s14); tiene(s15)), tiene(s17), tiene(s18), tiene(s19).
enfermedad('E5'):-tiene(s1), tiene(s3), tiene(s10) , tiene(s13) , tiene(s14) , tiene(s16).
enfermedad('E6'):-(tiene(s1);tiene(s2)),(tiene(s12);tiene(s13)),tiene(s3),tiene(s16),tiene(s10),tiene(s20).
enfermedad('E7'):- tiene(s3), (tiene(s4); tiene(s5)), tiene(s10), tiene(s13), tiene(s16).
enfermedad('E8'):- (tiene(s1);tiene(s2)), tiene(s3), tiene(s9), tiene(s12), tiene(s15), tiene(s16).

enfermedad(_):-fail.
limpiar:-retract(tiene(_)),fail.
limpiar.
