S, P = map(int,input().split(" "))

#Génération de tous les ensembles d'entiers sommant à S
#Processus itératif, on part de 0 jusqu'à S
partitions = []
partitions.append({()}) #Pour 0
for i in range(1,S+1):  #On génère les partitions de 1 à S
    s = set()
    for j in range(i-1+1):
        for tup in partitions[j]:
            if not tup or (i-j)>=tup[-1]: #pour ne pas générer les mêmes ensembles plusieurs fois
                s.add(tup+(i-j,))
    partitions.append(s)

#On passe en revue toutes les partitions sommant à S
#et on identifie celles dont le produit vaut P
ans = 0
for partition in partitions[S]:
    prod = 1
    for i in partition: prod *= i
    if prod==P: ans+=1
print(ans)