//https://www.acmicpc.net/problem/1874
//스택 수열

#include<stack>
#include<deque>
#include<iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    freopen("input.txt","rt",stdin);
    stack<int> S;
    deque<char> Q;
    int n; cin>>n;
    int tmp;
    int k = 1;


    for(int i=1;i<=n;i++){
        cin>>tmp;
        if(S.empty()){
            S.push(k);
            // cout<<"push: "<<k<<endl;
            k++;
            Q.push_back('+');
        }
        while(tmp!=S.top() && k<=n){
            S.push(k);
            // cout<<"push: "<<k<<endl;
            k++;
            Q.push_back('+');
            if(k>n) break;
        }
        if(tmp==S.top()){
            S.pop();
            // cout<<"pop: "<<tmp<<endl;
            Q.push_back('-');
        }
        else if(tmp<S.top()) break;
        
    }

    if(S.empty()){
        while (!Q.empty())
        {
            cout<<Q.front()<<'\n';
            Q.pop_front();
        }
        

    }else {
        cout<<"NO"<<'\n';
    }




    return 0;
}