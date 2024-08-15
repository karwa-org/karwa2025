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
