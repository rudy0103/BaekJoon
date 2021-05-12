//https://www.acmicpc.net/problem/11047
//동전 0

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
    int k; cin>>k;
    priority_queue<int> Q;
    for(int i = 0 ; i<n ; i++){
        int c; cin>>c;
        if(c<k){
            Q.push(c);
        }else{
            break;
        }
    }
    int cnt=0;
    while (!Q.empty() || k >0)
    {
        int coin = Q.top();
        int p=k/coin;
        if(k/coin>=1){
            cnt+=k/coin;
            k-=(coin*(k/coin));
        }else{
            Q.pop();
        }

    }
    
    cout<<cnt;




    return 0;
}