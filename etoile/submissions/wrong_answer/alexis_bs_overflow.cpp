#include <stdio.h>
#include <ostream>
#include <iostream>
#include <math.h>
#include <cassert>

#define int long long
#define double long double

using namespace std;

signed main() {
    int n; cin >> n;
    
    int left = 0;
    int right = n;
    int ans = 0;
    while (left <= right) {
        int mid = (left + right) / 2;
        
        int cnt = mid*mid + (mid-1) * (mid - 1);

        if (cnt > n) {
            right = mid-1;
        }else {
            ans = max(ans, mid);
            left = mid+1;
        }
    }
    
    cout << ans-1 << endl;

}