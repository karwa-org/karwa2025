/*
 * Solution en O(q * log(q) + n log(n)) with c++ upper_bound
 * @EXPECTED_RESULTS@: CORRECT
 */

#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

#define int long long

using namespace std;

signed main() {
    int n, q; cin >> n >> q;

    vector<int>a(n);
    for(auto&i : a ) cin >> i;

    vector<pair<int, int>> b(q);
    for(int i = 0; i < q; i++) {
        cin >> b[i].first;
        b[i].second = i;
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    vector<int> output(q);

    int offset = 0;
    for(int i = 0; i < n && offset < q; i++) {
        while(b[offset].first <= a[i] && offset < q) {
            int ans = a[i];
            if((i-1) >= 0){
                if(abs(ans-b[offset].first) > abs(a[i-1]-b[offset].first)){
                    ans = a[i-1];
                }
            }
            if((i+1) < n) {
                if(abs(ans-b[offset].first) > abs(a[i+1]-b[offset].first)){
                    ans = a[i+1];
                }
            }
            output[b[offset].second] = ans;
            offset++;
        }
    }

    while(offset < q) {
        output[b[offset].second] = a[n-1];
        offset++;
    }

    for(auto& i : output) cout << i << " ";
    cout << endl;
}