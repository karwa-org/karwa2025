/*
 * Solution en O(q * log(n) + n log(n)) with c++ upper_bound
 * @EXPECTED_RESULTS@: CORRECT
 */

#include <stdio.h>
#include <iostream>
#include <set>

#define int long long

using namespace std;


signed main() {
    int n, q; cin >> n >> q;

    set<int> a;
    for (int i = 0; i < n; i++){
        int v; cin >> v;
        a.insert(v);
    }

    for (int i = 0; i < q; i++) {
        int val; cin >> val;
        auto it = a.upper_bound(val);
        if(it == a.end()){
            cout << *prev(it) << endl;
        } else {
            if(it == a.begin()) {
                cout << *it << endl;
                continue;
            }
            int first = abs(val - *it);
            int second = abs(val - *prev(it));
            if(first <= second) {
                cout << *it << endl;
            }else {
                cout << *prev(it) << endl;
            }
        }
    }
}