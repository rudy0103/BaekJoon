//https://www.acmicpc.net/problem/2217
//로프

#include<iostream>
#include<vector>
#include<algorithm>

#define INF 2147000000

using namespace std;


int main(){
    // freopen("input.txt","rt",stdin);
    int n ; cin>>n;
    int max=0;
    vector<int> vec(n);

    for(int i=0; i<n; i++){
        cin>>vec[i];
        if(vec[i]>max) max=vec[i];
    }
    sort(vec.begin(),vec.end());

    int k=0;
    while(n>0){
        if(vec[k]*n > max){
            max=vec[k]*n;
        }
        n--;
        k++;
    }
    
    cout<<max;

    return 0;
}