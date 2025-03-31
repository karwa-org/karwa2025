#include <stdio.h>
#include <ostream>
#include <iostream>
#include <math.h>
#include <cassert>
#include <vector>
#include <functional>
#include <queue>
#include <string_view>
#include <algorithm>

#define int long long
#define double long double

using namespace std;

const int INF = numeric_limits<int>::max() / 2;
vector<int> a;

void solve() {
    int n;  cin >> n;
    a.resize(n);
    for(auto &i : a) 
        cin >> i;
        
    vector<vector<int>> dp(n, vector<int>(n, INF)); 
    vector<int> pa(n);
    pa[0] = a[0];
    for(int i = 1; i < n; i++) {
        pa[i] = pa[i-1] + a[i];
    }
    
    for(int i = 0; i < n; i++){
        dp[i][i] = 0;
    }
    
    for(int len = 2; len <= n; len++){
        for(int i = 0; i <= n - len; i++){
            int j = i + len - 1;
            int sum = (i == 0 ? pa[j] : pa[j] - pa[i-1]);
            for(int k = i; k < j; k++){
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + sum);
            }
        }
    }
    
    cout << dp[0][n-1] << "\n";
}

signed main() {
    solve();
    return 0;
}
