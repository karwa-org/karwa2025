#include <stdio.h>
#include <ostream>
#include <iostream>
#include <iostream>

#define int long long
#define double long double

using namespace std;


void solve() {
    int n, x; cin >> n >> x;
    if((n%x)==0) cout << n << endl;
    else cout << n+(x-(n%x)) << endl;
}

signed main() {
    solve();
    return 0;
}