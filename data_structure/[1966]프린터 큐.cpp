//https://www.acmicpc.net/problem/1966
//프린터 큐

#include<iostream>
#include<queue>

using namespace std;



int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    // freopen("input.txt","rt",stdin);

    int t ; cin>>t;
    

    for(int i = 1; i<= t; i++){
        int n; cin>>n;
        int pos; cin>>pos;
        queue<pair<int,int>> Q;
        priority_queue<int> pQ;

        for(int j=0; j<n ;j++){
            int tmp; cin>>tmp;
            Q.push(make_pair(tmp,j));
            pQ.push(tmp);
        }
        int cnt=0;
        while(true){
            if(Q.front().first==pQ.top()){
                cnt++;
                if(Q.front().second==pos) break;
                Q.pop();
                pQ.pop();
                
            }else{
                int a=Q.front().first;
                int b=Q.front().second;
                Q.pop();
                Q.push(make_pair(a,b));
            }

        }
        cout<<cnt<<endl;
        
    }





    return 0;
}