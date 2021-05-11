//https://www.acmicpc.net/problem/11508
//2+1 세일

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
    priority_queue<int,vector<int>, less<int>> Q;
    int n ; cin>>n;

    for(int i = 0 ;i<n; i++){
        int tmp; cin>>tmp;
        Q.push(tmp);
    }
    int total_cost=0;
    int cnt=0;
    while (!Q.empty())
    {
        int tmp= Q.top();
        Q.pop();
        cnt++;
        if(cnt==3){
            cnt=0;
        }
        else{
            total_cost+=tmp;
        }
    }
    cout<<total_cost;
    





    return 0;
}