//https://www.acmicpc.net/problem/20300
//서강근육맨

#include<iostream>
#include<vector>
#include<algorithm>
#include<deque>
#define INF 2147000000

using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    // freopen("input.txt","rt",stdin);
    int n; cin>>n;
    deque<long long> Q;

    for(int i=0; i<n; i++){
        long long tmp; cin>>tmp;
        Q.push_back(tmp);
    }
    if(n%2!=0) Q.push_back(0);
    sort(Q.begin(),Q.end());
    long long M=0;
    
    while (!Q.empty())
    {
        long long a = Q.front();
        Q.pop_front();
        long long b = Q.back();
        Q.pop_back();
        long long tmp = a+b;
        if(tmp>M) M=tmp;

    }
        

    cout<<M;


    return 0;
}