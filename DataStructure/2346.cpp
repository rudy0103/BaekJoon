//https://www.acmicpc.net/problem/2346
//풍선 터뜨리기

#include<iostream>
#include<deque>
#include<vector>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    freopen("input.txt","rt",stdin);

    int n; cin>>n;
    deque<pair<int,int>> Q;
    vector<int> vec;
    vector<int>::iterator it;

    for(int i = 1; i<=n; i++){
        int tmp;
        cin>>tmp;
        Q.push_back(make_pair(tmp,i));
    }

    while(!Q.empty()){
        int cnt=Q.front().first;
        int now=Q.front().second;
        Q.pop_front();
        vec.push_back(now);

        if(cnt>0){
            for(int k = 1; k<cnt; k++){
                int a =Q.front().first;
                int b =Q.front().second;
                Q.pop_front();
                Q.push_back(make_pair(a,b));
            }
        }
        else{
            cnt=-cnt;
            for(int k = 1; k<=cnt; k++){
                int a = Q.back().first;
                int b = Q.back().second;
                Q.pop_back();
                Q.push_front(make_pair(a,b));
            }
            

        }
    }

    for(it=vec.begin();it<vec.end();it++){
        cout<<*it<<" ";
    }








    return 0;
}
