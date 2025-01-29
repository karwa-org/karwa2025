/*
 * Solution en O(n*q)
 * @EXPECTED_RESULTS@: timelimit
 * Should only pass the first and second  group
 */
#include <iostream>
#include <vector>
#include <algorithm>

#define int long long

using namespace std;

signed main() {
    int n, q; cin >> n >> q;

    vector<int> a(n);
    for (auto& i : a) cin >> i;
    sort(a.begin(), a.end());

    for (int i = 0; i < q; i++) {
        int val; cin >> val;
        int idx = 0;

        while(idx < n && a[idx] <= val) {
            idx++;
        }
          if(idx == n) {
            cout << a[n-1] << endl;
        }else if(idx == 0){
            cout << a[0] << endl;
        }else {
            int prev = a[idx-1];
            int current = a[idx];

            if (abs(prev - val) <= abs(current - val)) cout << prev << endl;
            else cout << current << endl;
        }
    }
}