//https://www.acmicpc.net/problem/11399
//ATM

#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>

#define INF 2147000000

using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    // freopen("input.txt","rt",stdin);
    int n; cin>>n;
    int res=0;
    priority_queue<int, vector<int>, greater<int>> Q;
    
    for(int i = 0; i<n; i++){
        int pi; cin>>pi;
        Q.push(pi);
    }
    Q.push(0);
    int cum=0;
    while(!Q.empty()){
        int tmp=Q.top();
        cum+=tmp;
        res+=cum;
        Q.pop();
    }

    cout<<res;

    return 0;
}