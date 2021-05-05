//https://www.acmicpc.net/problem/2164
//카드 2

#include<iostream>
#include<deque>


using namespace std;

int main(){
    deque<int> Q;

    // freopen("input.txt","rt",stdin);
    int n; cin>>n;
    int tmp;

    for(int i = 1; i<=n; i++){
        Q.push_back(i);
    }

    while(!Q.empty()){
        tmp = Q.front();
        Q.pop_front();
        if(Q.empty()) break;
        tmp=Q.front();
        Q.pop_front();
        Q.push_back(tmp);

    }

    cout<<tmp;





    return 0;
}