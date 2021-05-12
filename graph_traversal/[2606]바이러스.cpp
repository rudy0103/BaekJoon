//https://www.acmicpc.net/problem/2606
//바이러스
#include<iostream>
#include<vector>
#include<algorithm>

#define INF 2147000000

using namespace std;

int ch[101];
vector<int> vec[101];

void DFS(int a){
    if(ch[a]==0){
        ch[a]=1;
        for(int i = 0; i<vec[a].size();i++){
            int next=vec[a][i];
            if(ch[next]==0)
            {
                DFS(next);
            }
        }
    }else{
        return ;
    }
}




int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    // freopen("input.txt","rt",stdin);
    int n; cin>>n;
    int m; cin>>m;
    int i,s,d;

    for( i = 0; i<m; i++){
        cin>>s;
        cin>>d;
        vec[s].push_back(d);
        vec[d].push_back(s);
    }

    DFS(1);

    int cnt=0;
    for( i = 2 ; i<=n; i++){
        if(ch[i]==1) cnt++;
    }
    cout<<cnt;


    return 0;
}