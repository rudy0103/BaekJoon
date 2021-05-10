//https://www.acmicpc.net/problem/14916
//거스름돈

#include<iostream>
#include<vector>
#include<algorithm>

#define INF 2147000000

using namespace std;


int main(){
    // freopen("input.txt","rt",stdin);
    int n; cin>>n;
    vector<int> vec(n+1,INF);
    int arr[]={2,5};

    vec[0]=0;
    for(int i = 0; i<2; i++){
        int tmp= arr[i];
        for(int j=tmp;j<=n;j++){
            vec[j]=min(vec[j-tmp]+1,vec[j]);
        }
    }
    
    
    if(vec[n]!=INF){
        cout<<vec[n];
    }else cout<<-1;







    return 0;
}