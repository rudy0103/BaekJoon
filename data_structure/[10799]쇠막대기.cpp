//https://www.acmicpc.net/problem/10799
//쇠막대기

#include<iostream>
#include<stack>
#include<string>




using namespace std;

int main(){

    ios::sync_with_stdio(false);
    cin.tie(0);
    // freopen("input.txt","rt",stdin);
    string str;
    stack<char> S;
    char last;
    cin>>str;
    int cnt=0;


    for(int i =0; i<(int)str.length(); i++){
        if(str[i]=='('){
            S.push('(');
            last=S.top();
        }
        else{
            S.pop();
            if(last=='('){
                cnt=cnt+S.size();

            }else cnt++;
            last=')';

        }
    }

    cout<<cnt;



    return 0;
}