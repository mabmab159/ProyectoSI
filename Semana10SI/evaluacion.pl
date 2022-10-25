% Ingreso de hechos
:-dynamic sintoma/1.
test(F):-write("impresion de prueba"),write(F).
listar_sintomas([]):-enfermedad(E),write(E).
listar_sintomas([H|T]):-assert(sintoma(H)),listar_sintomas(T).
% Validando reglas
enfermedad("COVID-19"):-sintoma(s1),sintoma(s2),sintoma(s3),sintoma(s4).
enfermedad("Gripe"):-sintoma(s2),sintoma(s3),sintoma(s4),sintoma(s5).
enfermedad("Resfriado"):-sintoma(s4),sintoma(s5).
enfermedad("Virus sincitial respiratorio(VSR)"):-sintoma(s5).
enfermedad(_):-fail.
% Limpiando la memoria
limpiar:-retrac(sintoma(_)),fail.
limpiar.