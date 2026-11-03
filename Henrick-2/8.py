# vários if soltos rodam de forma independente, então o Python vai testar um por um. Se três condições forem verdadeiras, ele vai executar as três.
# Já o if / elif / else funciona em cadeia. O Python vem testando de cima para baixo e, na primeira condição que der certo, ele executa e simplesmente ignora todo o resto.

nota = float(input("Digite a nota do aluno (0 a 10): "))

if nota >= 9:
    print("A")
elif nota >= 7:
    print("B")
else:
    print("C")
