#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Graph {
    int V; 
    vector<int> *adj; 
    
public:
    Graph(int V) {
        this->V = V;
        adj = new vector<int>[V];
    }
    
    void addEdge(int u, int v) {
        adj[u].push_back(v); 
    }

    vector<int> traverse(){
        for(auto x: adj){
            for(auto y:x){
                
            }
        }
    }
    
    // DFS function
    bool dfs(int u, vector<bool>& visited, vector<bool>& recStack, stack<int>& st) {
        visited[u] = true;
        recStack[u] = true; 
        
      
        for (int v : adj[u]) {
            if (!visited[v]) {
                if (!dfs(v, visited, recStack, st))
                    return false; 
            }
            else if (recStack[v]) {
                return false; 
            }
        }
        
        recStack[u] = false; 
        st.push(u); 
        return true;
    }
    
    vector<int> topologicalSort() {
        vector<bool> visited(V, false);
        vector<bool> recStack(V, false); 
        stack<int> st;
        
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                if (!dfs(i, visited, recStack, st)) {
                    cout << "Cycle detected! Cannot do topological sort." << endl;
                    return {};
                }
            }
        }
        
       
        vector<int> result;
        while (!st.empty()) {
            result.push_back(st.top());
            st.pop();
        }
        return result;
    }
};


void test1() {
    cout << "=== Test 1: Simple Linear ===" << endl;
    Graph g(3);
    g.addEdge(0, 1); // 0 -> 1
    g.addEdge(1, 2); // 1 -> 2
    
    vector<int> result = g.topologicalSort();
    
    cout << "Topological Order: ";
    for (int node : result) {
        cout << node << " ";
    }
    cout << endl;
   
}

void test2() {
    cout << "\n=== Test 2 ===" << endl;
    Graph g(6);
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);
    

    vector<int> result = g.topologicalSort();
    
    cout << "Topological Order: ";
    for (int node : result) {
        cout << node << " ";
    }
    cout << endl;
    
}

void test3() {
    cout << "\n=== Test 3 ===" << endl;
    Graph g(3);
    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 0); 
    
    vector<int> result = g.topologicalSort();
    
    if (result.empty()) {
        cout << "No valid order - cycle detected!" << endl;
    }
}


void test4() {
    cout << "\n=== Test 4 ===" << endl;
    Graph g(6);
    
   
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(1, 3); 
    g.addEdge(2, 4); 
    g.addEdge(2, 5); 
    g.addEdge(3, 4);
    
    vector<int> result = g.topologicalSort();
    
    cout << "Course Order: ";
    for (int course : result) {
        cout << course << " ";
    }
    cout << endl;
}

int main() {
    cout << "DFS Topological Sort" << endl;
    cout << "====================================" << endl;
    
    test1(); 
    test2();
    test3();
    test4();
    return 0;
}