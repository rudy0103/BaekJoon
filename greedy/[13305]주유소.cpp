#include<iostream>
#include<vector>
#include<algorithm>

#define INF 2147000000

using namespace std;


int main(){
    
    ios::sync_with_stdio(false);
    cin.tie(0);
    // freopen("input.txt","rt",stdin);
    int n; cin>>n;
    vector<int> city;
    vector<int> road;

    for(int i = 0 ; i<n-1; i++){
        int tmp; cin>>tmp;
        road.push_back(tmp);
    }
    for(int i = 0; i<n; i++){
        int tmp; cin>>tmp;
        city.push_back(tmp);
    }


    long long cost =0;
    long long min_cost= INF;
    int now=0;

    while (true)
    {
        if(city[now] < min_cost){
            min_cost=city[now];
        }
        cost+=min_cost*road[now];
        now++;
        if(now==n-1) break;
    }
    

    cout<<cost;

    return 0;
}