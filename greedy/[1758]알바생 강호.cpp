//https://www.acmicpc.net/problem/1758
//알바생 강호

#include<iostream>
#include<vector>
#include<algorithm>
#include<deque>

#define INF 2147000000

using namespace std;


int main(){
    // freopen("input.txt","rt",stdin);
    int n ; cin>>n;
    deque<int> Q;
    for(int i =0; i<n; i++){
        int a;
        cin>>a;
        Q.push_back(a);
    }
    int k=0;
    long long total=0;

    sort(Q.begin(),Q.end());

    while (!Q.empty())
    {
        int tmp=Q.back();
        Q.pop_back();
        int tip= tmp-k;
        if(tip<0) break;
        k++;
        total+=tip;
    }
    

    cout<<total;


    return 0;
}