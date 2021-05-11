//https://www.acmicpc.net/problem/1931
//회의실 배정

#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>

#define INF 2147000000

using namespace std;
int maximum;
int n;


struct Meeting{
    int start;
    int end;

    bool operator<(const Meeting &b){
        if(start!=b.start) return start<b.start;
        if(end!=b.end) return end<b.end;

    }
};

vector<Meeting> vec(n);

int dy[100000];


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    // freopen("input.txt","rt",stdin);
    cin>>n;
    int start,end;
    for(int i=0; i<n; i++){
        cin>>start>>end;
        Meeting a;
        a.start=start;
        a.end=end;
        vec.push_back(a);
    }

    sort(vec.begin(),vec.end());

    int res=0;

    int k = 0;
    while (k<n)
    {
        int s = vec[k].start;
        int e = vec[k].end;
        int maximum=0;
        int pos=k;
        
        for(int i = k; i>=0; i--){
            if(vec[i].end<=s){
                if(dy[i]>maximum){
                    pos=i;
                    maximum=dy[i];
                }
                if(vec[i].end<vec[pos].start) break;
            }
        }
        dy[k]=dy[pos]+1;
        if(dy[k]>res) res=dy[k];
        k++;

    }
    
    // for(int i = 0 ; i<n ; i++){
    //     cout<<dy[i]<<" ";
    // }
    // cout<<endl;


    cout<<res;


    return 0;
}