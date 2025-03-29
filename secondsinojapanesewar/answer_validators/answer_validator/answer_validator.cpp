#include "validation.h"

using namespace std;

int main(int argc, char *argv[]) {
    // Set up the input and answer streams.
    std::ifstream in(argv[1]);
    AnswerValidator v(argc, argv);

    int n, m, p; in >> n >> m >> p;
    vector<bool> candidates(n);
    for(int i = 0; i < m; i++) {
        int k; in >> k;
        candidates[k] = true;
    }

    vector<vector<int>> adj(n);
    for(int i = 0; i < p; i++) {
        int u, t; in >> u >> t;
        adj[u].push_back(t);
        adj[t].push_back(u);
    }

    int answer = v.read_integer("num_of_cycles", 1, m);
    v.newline();

    vector<bool> is_cycle(n);
    for(int i = 0; i < answer; i++) {
        int cycle = v.read_integer("cycle", 0, n);
        if (is_cycle[cycle]) {
            v.WA("Cannot have the same cycle: ", cycle);
            return 43;
        }

        is_cycle[cycle] = true;
        //cerr << i << " " << (answer-1) << endl;
        if (i != (answer-1)) {
            v.space();
        }
    }
    v.newline();
    return 0;
}
