def main():
    import sys
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    positions = list(map(int, input_data[1:n+1]))
    speeds = list(map(int, input_data[n+1:2*n+1]))
    c = int(input_data[2*n+1])
    
    # Calcul du temps pour chaque poisson pour atteindre la cible
    poissons = []
    for i in range(n):
        # Si v == 0, on considère que le poisson ne pourra jamais atteindre la cible
        # On peut utiliser float('inf') pour ce cas.
        t = (c - positions[i]) / speeds[i] if speeds[i] != 0 else float('inf')
        poissons.append((positions[i], t))
    
    # On trie les poissons par ordre décroissant de position
    poissons.sort(key=lambda x: x[0], reverse=True)
    
    groupes = 0
    temps_courant = 0.0
    for pos, t in poissons:
        # Si le poisson met plus de temps que le groupe courant, il ne rattrapera pas
        # et forme donc un nouveau groupe.
        if t > temps_courant:
            groupes += 1
            temps_courant = t
    
    print(groupes)

if __name__ == "__main__":
    main()
