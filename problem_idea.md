# Where is my wifi
En gros il y a des antennes wifis sur le même axe (1D) (si on augmente la dimension alors faut utiliser un kd-tree / (quad/oct-tree) )
On a Q query qui demandent quelle est l'antenne la plus proche avec un point donné

Solution -> set avec lower_bound ou bien array avec binary_search
Complexitée `O(n + q*log(n))`

# Pas encore de nom
J'ai lu un article wikipedia sur les intersection graphs où on passe de la géométrie aux graphes (comme Rubber booth) on pourrait faire qqch d'intéressant avec ça ? 
En mode il y a des nations qui sont représentés par des cercles, si jamais deux nations s'overlapent alors on fait un truc genre la nation A est énemie avec la Nation B
Si on ajoute une notation d'amis / énemis alors ça veut dire qu'on peut colorier notre graphe en 2 couleures et que faire avec ? maybe trop compliqué pour le karwa ? 
Ajouter Un concepte d'ordre d'amitié ? Ou bien un groupe resteint ?

# gardes 
En gros notre personnage est dans un labyrinthe et il doit sortir du labyrinthe sauf qu'il y a K gardes qui font des rondes. il faut dire si c'est possible de s'échapper.

# Post facebook 
je suis tombé sur un post facebook https://www.facebook.com/share/p/PPofCQ2MS2UL2Uc8/ et en vrais il y a moyen de faire un problème avec un graphe et des queries en mode je possède un rein, j'ai 10k euro j'ai 5 pieds et on veut savoir c'est quoi le résultat si on suit le graphe.

# Coprime
Un truc tout con, on donne un intervale A et B, il faut trouver deux nombres qui sont co-prime. À prover mais à priori ça devrait simplemet ^etre a et a+1.

# Anniversaire

En gros Aymeric a eu une superbe idée on a des sets de mots par exemple "abc", "pomme", "poire", "fraise" et le but c'est de savoir le nombre minimum de set de mots pour pouvoir former un autre mot par exemple combien de set je dois choisir si je veux former "alexis".
