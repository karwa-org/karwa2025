# Where is my wifi
En gros il y a des antennes wifis sur le même axe (1D) (si on augmente la dimension alors faut utiliser un kd-tree / (quad/oct-tree) )
On a Q query qui demandent quelle est l'antenne la plus proche avec un point donné

Solution -> set avec lower_bound ou bien array avec binary_search
Complexitée `O(n + q*log(n))`
