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
        int midd = (left + right) / 2;
        double mid = (double)midd;
        double cnt = mid*mid + (mid-1) * (mid - 1);

        if (cnt > n) {
            right = mid-1;
        }else {
            ans = max(ans, midd);
            left = mid+1;
        }
    }
    cout << ans-1 << endl;
}
