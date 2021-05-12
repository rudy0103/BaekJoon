//https://www.acmicpc.net/problem/13164
//행복 유치원

#include<iostream>
#include<vector>
#include<algorithm>

#define INF 2147000000

using namespace std;
int n ; 
int vec[300001];

bool Count_group(int min_cost, int n, int k){
    int cnt=1;
    int cost=min_cost;
    int left=0;
    int right=0;
    while(cost>=0 && left<n-1 && right<n-1){
        if(vec[right+1]-vec[left]<=cost){
            while(vec[right+1]-vec[left]<=cost){
                right++;
            }
        }
        else {
            cost-=vec[right]-vec[left];
            left=right+1;
            right=left;
            cnt++;
            if(cnt>k) return false;
        }
    }
    if(cnt <= k){
        return true;
    }
    else return false;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("input.txt","rt",stdin);
    cin>>n;
    int k ; cin>>k;
    for(int i=0; i<n; i++){
        cin>>vec[i];
    }

    int left = 0;
    int right = vec[n-1]-vec[0];
    int min_cost=vec[n-1]-vec[0];

    while(left<=right){
        int mid=(left+right)/2;
        if(Count_group(mid,n,k)){
            min_cost=mid;
            right=mid-1;
        }else{
            left=mid+1;
        }
    }
    cout<<min_cost;


    return 0;
}