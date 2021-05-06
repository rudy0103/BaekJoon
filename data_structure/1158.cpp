//https://www.acmicpc.net/problem/1158
//요세푸스 문제 
#include<queue>
#include<iostream>


using namespace std;

int main(){

    // freopen("input.txt","rt",stdin);
    queue<int> Q;
    queue<int> R;
    int n,k,tmp;
    int i,j;
    int cnt=0;
    cin>>n>>k;

    for( i = 1; i<=n; i++) Q.push(i);


    while(!Q.empty()){
        
        tmp=Q.front();
        Q.pop();
        cnt++;
        if(cnt==k){
            cnt=0;
            R.push(tmp);
        }else{
            Q.push(tmp);
        }

    }
    
    cout<<"<";
    for( i=1;i<=n;i++){
        tmp=R.front();
        R.pop();
        cout<<tmp;
        if(i!=n) cout<<", ";
    }
    cout<<">";
    


    return 0;
}