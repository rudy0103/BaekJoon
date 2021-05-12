//https://www.acmicpc.net/problem/13164
//행복 유치원

#include<iostream>
#include<vector>
#include<algorithm>

#define INF 2147000000

using namespace std;



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("input.txt","rt",stdin);
    int n; cin>>n;
    int k ; cin>>k;
    vector<int> vec;
    int left;
    cin>>left;
    for(int i=0; i<n-1; i++){
        int tmp; cin>>tmp;
        vec.push_back(tmp-left);
        left=tmp;
    }

    int min_cost=0;
    sort(vec.begin(),vec.end());
        for(int i=0; i<n-(k-1)-1;i++){
        min_cost+=vec[i];
    }

    cout<<min_cost;





    return 0;
}