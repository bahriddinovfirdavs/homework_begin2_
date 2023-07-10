S=float(input())
p=3.14   # S=p*D**2/4=>D=(4*S/p)**1/2
D=(4*S/p)**1/2
L=p*D
S=p*D*D/4
print(L,D)