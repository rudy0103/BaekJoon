//https://www.acmicpc.net/problem/1931
//회의실 배정

#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>

#define INF 2147000000

using namespace std;
int n;

struct Meeting{
    int start;
    int end;

    bool operator<(const Meeting &b){
        if(end!=b.end) return end<b.end;
        if(start!=b.start) return start<b.start;

    }
};

vector<Meeting> vec(n);


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
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

    int last_end=0;
    while (k<n)
    {
        if(vec[k].start>=last_end) {
            res++;
            last_end=vec[k].end;
        }
        k++;
    }
    
    cout<<res;

    return 0;
}