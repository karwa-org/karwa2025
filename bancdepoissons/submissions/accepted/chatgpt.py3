def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    positions = list(map(int, data[1:n+1]))
    speeds = list(map(int, data[n+1:2*n+1]))
    c = int(data[2*n+1])
    
    EPS = 1e-9  # tolérance pour la comparaison des flottants
    
    # On trie les poissons par position décroissante (le plus proche de la cible en premier)
    poissons = sorted(zip(positions, speeds), key=lambda x: x[0], reverse=True)
    
    fleets = 0  # nombre de bancs qui atteignent la cible
    cur_time = 0.0  # temps d'arrivée du groupe actuellement constitué
    
    for pos, sp in poissons:
        # Calcul du temps d'arrivée en tenant compte d'une vitesse nulle
        if sp == 0:
            t = float('inf') if pos < c else 0.0
        else:
            t = (c - pos) / sp
        
        # Si le temps d'arrivée est supérieur (avec une marge EPS) au temps du groupe courant,
        # cela signifie que ce poisson ne rattrapera pas le groupe et forme donc un nouveau banc.
        if t - cur_time > EPS:
            fleets += 1
            cur_time = t
            
    print(fleets)

if __name__ == "__main__":
    main()
