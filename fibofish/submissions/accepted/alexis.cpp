#include <stdio.h>
#include <ostream>
#include <iostream>
#include <math.h>
#include <cassert>
#include <vector>
#include <unordered_map>
#include <map>
#include <limits>


#define int long long
#define double long double


using namespace std;

const int INF = numeric_limits<int>::max()/2;


vector<int> fibbo(87, 0);

void solve() {
    int n; cin >> n;
    int idx = fibbo.size()-1;
    int ans = 0;
    while(n > 0  && idx >= 0) {
        if(fibbo[idx] > n) {
            idx--;
            continue;
        }
        n -= fibbo[idx];
        ans += (idx+1);
        idx--;
    }
    cout << ans << endl;
}

signed main() {
    fibbo[0] = 1;
    fibbo[1] = 2;
    for(int i = 2; i < 87; i++) {
        fibbo[i] = fibbo[i-1] + fibbo[i-2];
    }     

    solve();
    return 0;
}