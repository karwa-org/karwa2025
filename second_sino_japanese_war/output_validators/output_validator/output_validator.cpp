#include "validation.h"
#include <vector>
#include <iostream>
#include <queue>
// For DYNAMIC OUTPUT PROBLEMS:
// This program will be called as
// output_validator input answer < team_output
//
// Please check the grammar of the team output using the Validator class.
// See input_validator.cpp for information on how to use the Validator class.
// You should also check the validity of the answer here.
// For example, check that a tree printed by the team is a tree indeed.

// For INTERACTIVE PROBLEMS:
// Write your output validator as usual, but make sure to flush all standard
// output. Call `v.set_WA_handler(lambda)` to gracefully handle failures when
// parsing team output. You could e.g. send a '-1' to the submission to tell it
// to stop running.

using namespace std;

const int INF = numeric_limits<int>::max()/2;

int girth(vector<vector<int>>& adj, int source) {
    vector<int> d(adj.size(), INF);
    d[source] = 0;
    queue<int> q;
    q.push(source);

    int shortest_cycle = INF;

    while(!q.empty()){
        int current = q.front(); q.pop();
        for(auto& v : adj[current]) {
            if(v == current) continue;
            if(d[v] == INF){
                d[v] = d[current] + 1;
                q.push(v);
            }else {
                shortest_cycle = min(shortest_cycle, d[current] + d[v] + 1);
                continue;
            }
        }
    }

    return shortest_cycle;
}

int main(int argc, char *argv[]) {
    // Set up the input and answer streams.
    std::ifstream in(argv[1]);
    std::ifstream ans(argv[2]); // Only for custom checker.
    OutputValidator v(argc, argv);

    int n, m, p; in >> n >> m >> p;
    vector<vector<int>> adj(n);
    vector<bool> candidates(n);

    for(int i = 0; i < m; i++){
        int t; in >> t;
        candidates[t] = true;
    }

    for(int i = 0; i < p; i++) {
        int u, v; in >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int jury_ans; ans >> jury_ans;
    int contestant_ans = v.read_integer("ans", 0, 10000);

    if (candidates[contestant_ans] != true) {
        v.WA("The given city is not a candidate city. got :", contestant_ans, " expected :", jury_ans);
    }

    // Check if contestant answer is the best one by computing the girth of the graph :)
    int contestant_girth = girth(adj, contestant_ans);
    int jury_girth = girth(adj, jury_ans);

    if (contestant_girth != jury_girth) {
        v.WA("The given city is not the best. got :", contestant_ans, " expected : ", jury_ans);
    }
}
