#include "validation.h"

using namespace std;

int main(int argc, char *argv[]) {
    InputValidator v(argc, argv);
    int n = v.read_integer("number_of_cities", 3, 301);
    v.space();
    int m = v.read_integer("number_of_candidates", 1, 301);
    v.space();
    int p = v.read_integer("number_of_edges", 3, (300*(300-1))/2);
    v.newline();

    vector<bool> candidates(n);
    for(int i = 0; i < m; i++) {
        int c = v.read_integer("candidate", 0, n-1);
        if (candidates[c]) {
            v.WA("Cannot have multiple candidate, they must be unique");
        }
        candidates[c] = true;
        if(i != m-1) v.space();
    }
    v.newline();

    vector<vector<int>> adj(n);
    map<pair<int, int>, bool> cnt;
    for(int i = 0; i < p; i++) {
        int u = v.read_integer("u", 0, n-1);
        v.space();
        int vv = v.read_integer("v", 0, n-1);

        if(cnt[make_pair(u,vv)] || cnt[make_pair(vv,u)]) {
            v.WA("The graph must be simple, it is not a multigraph ! for edge: ", u, " and : ", vv);
        }
        cnt[make_pair(u,vv)] = true;
        cnt[make_pair(vv,u)] = true;
        adj[u].push_back(vv);
        adj[vv].push_back(u);
        v.newline();
    }
}
