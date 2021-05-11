//https://www.acmicpc.net/problem/20115
//에너지 드링크

#include<iostream>
#include<vector>
#include<algorithm>

#define INF 2147000000

using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    // freopen("input.txt","rt",stdin);
    int n ; cin>>n;
    int highest=0;
    long double res;
    long long total=0;
    for(int i=0 ; i<n; i++){
        int tmp; cin>>tmp;
        if(tmp>highest) highest=tmp;
        total+=tmp;
    }
    total-=highest;

    res=highest+((long double)total/2);
    cout<<res;



    return 0;
}