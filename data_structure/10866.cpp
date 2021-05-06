//https://www.acmicpc.net/problem/10866
//덱


#include<iostream>
#include<string>
#include<deque>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    // freopen("input.txt","rt",stdin);
    int n; cin>>n;
    deque<int> Q;



    for(int i =1 ; i<=n; i++){
        string instruction;
        cin>>instruction;

        if(instruction=="push_back"){
            int item;
            cin>>item;
            Q.push_back(item);
        }
        if(instruction=="push_front"){
            int item;
            cin>>item;
            Q.push_front(item);
        }
        else if(instruction=="pop_front"){
            if(!Q.empty()){
                cout<<Q.front()<<'\n';
                Q.pop_front();
            }else cout<<-1<<'\n';
        }
        else if(instruction=="pop_back"){
            if(!Q.empty()){
                cout<<Q.back()<<'\n';
                Q.pop_back();
            }else cout<<-1<<'\n';
        }
        else if(instruction=="size"){
            cout<<(int)Q.size()<<'\n';
        }
        else if(instruction=="empty"){
            cout<<Q.empty()<<'\n';
        }
        else if(instruction=="front"){
            if(Q.empty()) cout<<-1<<'\n';
            else cout<<Q.front()<<'\n';
        }
        else if(instruction=="back"){
            if(Q.empty()) cout<<-1<<'\n';
            else cout<<Q.back()<<'\n';
        }
    }
    

    return 0;
}