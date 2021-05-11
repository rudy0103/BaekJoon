//https://www.acmicpc.net/problem/20365
//블로그2
#include<iostream>
#include<vector>
#include<algorithm>

#define INF 2147000000

using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    // freopen("input.txt","rt",stdin);
    int n; cin>>n;
    char first;
    cin>>first;
    char last=first;
    int cnt=1;
    for(int i=0 ; i<n-1; i++){
        char tmp; cin>>tmp;
        if(tmp!=first){
            if(tmp!=last){
                cnt++;
            }
        }
        last=tmp;
    }

    cout<<cnt;

    return 0;
}