//https://www.acmicpc.net/problem/2346
//풍선 터트리기
#include<iostream>
#include<deque>
#include<vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    // freopen("input.txt","rt",stdin);

    int n; cin>>n;
    int i,k;
    int cnt,now;
    deque<pair<int,int>> Q;
    vector<int>::iterator it;

    for(i = 1; i<=n; i++){
        int tmp;
        cin>>tmp;
        Q.push_back(make_pair(tmp,i));
    }

    while(!Q.empty()){
        cnt=Q.front().first;
        now=Q.front().second;
        Q.pop_front();
        cout<<now<<" ";


        if(cnt>0){
            for( k = 1; k<cnt; k++){
                Q.push_back(make_pair(Q.front().first,Q.front().second));
                Q.pop_front();
            }
        }
        else{
            cnt=-cnt;
            for( k = 1; k<=cnt; k++){
                Q.push_front(make_pair(Q.back().first,Q.back().second));
                Q.pop_back();
            }
            

        }
    }








    return 0;
}
