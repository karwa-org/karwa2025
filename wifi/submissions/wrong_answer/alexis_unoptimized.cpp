/*
 * Solution en O((nlogn)*q)
 * @EXPECTED_RESULTS@: PARTIALLY-ACCEPTED
 * Should only pass the first group
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

    for (int i = 0; i < q; i++) {
        int val; cin >> val;
        int idx = 0;
        vector<int> tmp = a;
        sort(tmp.begin(), tmp.end());

        while(idx < n && tmp[idx] <= val) {
            idx++;
        }
          if(idx == n) {
            cout << tmp[n-1] << endl;
        }else if(idx == 0){
            cout << tmp[0] << endl;
        }else {
            int prev = tmp[idx-1];
            int current = tmp[idx];

            if (abs(prev - val) <= abs(current - val)) cout << prev << endl;
            else cout << current << endl;
        }
    }
}